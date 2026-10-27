#!/usr/bin/env python3
"""Ponte entre os posts do repositório e o Metricool.

O agendamento em si é feito pelo Claude com as ferramentas MCP do Metricool;
este script só calcula o próximo horário e monta o JSON `info` exato que
createScheduledPost / updateScheduledPost esperam.

Uso:
    python3 scripts/metricool.py proximo-horario
    python3 scripts/metricool.py payload posts/<slug> --sha <commit> [--rascunho]
    python3 scripts/metricool.py payload-story posts/<slug> --sha <commit> [--rascunho]
"""
import argparse
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

RAIZ = Path(__file__).resolve().parent.parent
ESTRATEGIA = RAIZ / "config" / "estrategia.json"
DIAS = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
LIMITE_LEGENDA = 2200
# Emojis na legenda dão cara de texto de IA (pedido do João): nenhum é aceito.
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F]")
ANTECEDENCIA_MIN_HORAS = 4


def carregar_estrategia():
    return json.loads(ESTRATEGIA.read_text(encoding="utf-8"))


def posts_existentes():
    for p in sorted((RAIZ / "posts").glob("*/post.json")):
        yield p.parent, json.loads(p.read_text(encoding="utf-8"))


def proximo_horario(agora=None):
    """Primeiro dia preferido ainda sem post, no slot da vez (rotação na
    exploração, melhor slot ~70% na otimização). Preenche buracos na agenda."""
    est = carregar_estrategia()
    tz = ZoneInfo(est["metricool"]["timezone"])
    agora = agora or datetime.now(tz)

    ocupados = set()
    for _, post in posts_existentes():
        quando = post.get("agendamento", {}).get("data_hora")
        if quando and post.get("status") not in ("rejeitado", "descartado"):
            ocupados.add(datetime.fromisoformat(quando).astimezone(tz).date())

    h = est["horarios"]
    indice = h.get("proximo_slot_indice", 0)
    if est.get("fase") == "otimizacao" and h.get("melhor_slot") and indice % 10 < 7:
        slot = h["melhor_slot"]
    else:
        slot = h["slots"][indice % len(h["slots"])]
    hora, minuto = map(int, slot.split(":"))

    # Hoje só vale se ainda sobrar tempo para o João aprovar.
    dia = agora.date()
    for _ in range(30):
        quando = datetime(dia.year, dia.month, dia.day, hora, minuto, tzinfo=tz)
        livre = DIAS[dia.weekday()] in est["dias_preferidos"] and dia not in ocupados
        if livre and quando - agora >= timedelta(hours=ANTECEDENCIA_MIN_HORAS):
            return quando, slot
        dia += timedelta(days=1)
    sys.exit("Nenhum dia livre nos próximos 30 dias.")


def avancar_slot():
    est = carregar_estrategia()
    est["horarios"]["proximo_slot_indice"] = est["horarios"].get("proximo_slot_indice", 0) + 1
    ESTRATEGIA.write_text(json.dumps(est, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def creditos(post):
    if post.get("formato") == "noticia" and post.get("capa"):
        usadas = {post["capa"]["imagem"]}
    elif post.get("formato") == "noticia":
        n = post["noticia"]
        pessoas = n.get("placar", []) + [c for c in (n.get("vencedor"), n.get("segundo")) if c]
        usadas = {n.get("imagem"), *(c.get("foto") for c in pessoas)}
    else:
        usadas = {post["capa"]["imagem"], *(s.get("imagem") for s in post["slides"])}
    linhas, livres = [], 0
    for img in post.get("imagens", []):
        if img["id"] not in usadas:
            continue
        if img.get("exige_credito"):
            linhas.append(f"{img['autor']} ({img['licenca']})")
        else:
            livres += 1
    if not linhas:
        return "Imagens: domínio público via Wikimedia Commons."
    unicos = list(dict.fromkeys(linhas))
    demais = " Demais: domínio público." if livres else ""
    return "Imagens via Wikimedia Commons: " + "; ".join(unicos) + "." + demais


def textos_alternativos(post, n):
    """Um texto alternativo por slide (acessibilidade): capa, títulos e CTA."""
    if post.get("formato") == "noticia" and post.get("capa"):
        c = post["capa"]
        inds = "; ".join(f"{i['rotulo']}: {i['valor']}" for i in c.get("indicadores", []))
        return [re.sub(r"<[^>]+>", "", f"{c['titulo_html']}. {c['gancho']} {inds}")]
    if post.get("formato") == "noticia":
        n = post["noticia"]
        if n.get("tema") == "vencedor":
            v, s2 = n["vencedor"], n["segundo"]
            return [f"{v['nome']} ({v.get('partido', '')}) eleito presidente com {v['valor']} dos votos válidos; "
                    f"{s2['nome']} ({s2.get('partido', '')}) {s2['valor']}. {n.get('rodape', '')}."]
        placar = "; ".join(f"{c['nome']} ({c.get('partido', '')}) {c['valor']}" for c in n.get("placar", []))
        return [re.sub(r"<[^>]+>", "", f"{n['titulo_html']}. {placar}. {n.get('subtitulo_html', '')}")]
    capa = re.sub(r"<[^>]+>", "", post["capa"]["titulo_html"])
    textos = [f"Capa: {capa}. {re.sub(r'<[^>]+>', '', post['capa']['gancho'])}"]
    for i, s in enumerate(post["slides"], start=2):
        resumo = s.get("titulo") or " ".join(re.sub(r"<[^>]+>", " ", s["texto_html"]).split()[:20])
        textos.append(f"Slide {i}: {resumo}")
    textos.append("Diplomacia da Guerra — salve este post e siga @diplomaciadaguerra")
    return textos[:n] if len(textos) >= n else textos + [post.get("alt_text", "")] * (n - len(textos))


def montar_legenda(post, est):
    # Posts fora do tema militar (ex.: eleições) podem dispensar as hashtags de base.
    base = est["hashtags_base"] if post.get("usar_hashtags_base", True) else []
    hashtags = list(dict.fromkeys(post.get("hashtags", []) + base))[: est["max_hashtags"]]
    partes = [post["legenda"].strip()]
    if post.get("fontes"):
        partes.append("Fontes: " + ", ".join(f["nome"] for f in post["fontes"]) + ".")
    partes.append(creditos(post))
    partes.append(" ".join(hashtags))
    texto = "\n\n".join(partes)
    achados = EMOJI.findall(texto + post.get("primeiro_comentario", ""))
    if achados:
        sys.exit(f"Legenda/primeiro comentário com emoji ({' '.join(dict.fromkeys(achados))}). Tire os emojis do post.json.")
    if len(texto) > LIMITE_LEGENDA:
        sys.exit(f"Legenda com {len(texto)} caracteres (limite {LIMITE_LEGENDA}). Encurte post.json → legenda.")
    return texto


def payload(post_dir, sha, rascunho):
    est = carregar_estrategia()
    post = json.loads((post_dir / "post.json").read_text(encoding="utf-8"))
    repo = est["repositorio"]
    rel = post_dir.resolve().relative_to(RAIZ).as_posix()
    slides = sorted((post_dir / "slides").glob("*.jpg"))
    if not 1 <= len(slides) <= 20:
        sys.exit(f"{len(slides)} slides em {post_dir}/slides — rode scripts/render.py antes.")
    media = [f"https://raw.githubusercontent.com/{repo['owner']}/{repo['repo']}/{sha}/{rel}/slides/{s.name}"
             for s in slides]

    quando = datetime.fromisoformat(post["agendamento"]["data_hora"])
    info = {
        "autoPublish": True,
        "draft": rascunho,
        "descendants": [],
        "firstCommentText": post.get("primeiro_comentario", ""),
        "hasNotReadNotes": False,
        "media": media,
        "mediaAltText": textos_alternativos(post, len(media)),
        "providers": [{"network": "instagram"}],
        "publicationDate": {"dateTime": quando.strftime("%Y-%m-%dT%H:%M:%S"),
                            "timezone": est["metricool"]["timezone"]},
        "shortener": False,
        "smartLinkData": {"ids": []},
        "text": montar_legenda(post, est),
        "instagramData": {"type": "POST", "collaborators": [], "showReelOnFeed": True,
                          "isAiGenerated": post.get("ia_gerado", False)},
    }
    return {"blogId": est["metricool"]["blog_id"], "date": quando.isoformat(), "info": info}


def payload_story(post_dir, sha, rascunho, atraso_min=2):
    """Story que repete o post do feed (só a capa, sem texto), alguns minutos depois dele."""
    est = carregar_estrategia()
    post = json.loads((post_dir / "post.json").read_text(encoding="utf-8"))
    repo = est["repositorio"]
    rel = post_dir.resolve().relative_to(RAIZ).as_posix()
    if not (post_dir / "story" / "story.jpg").exists():
        sys.exit(f"{post_dir}/story/story.jpg não existe — rode scripts/story.py antes.")
    quando = datetime.fromisoformat(post["agendamento"]["data_hora"]) + timedelta(minutes=atraso_min)
    info = {
        "autoPublish": True,
        "draft": rascunho,
        "descendants": [],
        "firstCommentText": "",
        "hasNotReadNotes": False,
        "media": [f"https://raw.githubusercontent.com/{repo['owner']}/{repo['repo']}/{sha}/{rel}/story/story.jpg"],
        "mediaAltText": [textos_alternativos(post, 1)[0]],
        "providers": [{"network": "instagram"}],
        "publicationDate": {"dateTime": quando.strftime("%Y-%m-%dT%H:%M:%S"),
                            "timezone": est["metricool"]["timezone"]},
        "shortener": False,
        "smartLinkData": {"ids": []},
        "instagramData": {"type": "STORY", "collaborators": [], "showReelOnFeed": True,
                          "isAiGenerated": post.get("ia_gerado", False)},
    }
    return {"blogId": est["metricool"]["blog_id"], "date": quando.isoformat(), "info": info}


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("proximo-horario")
    sub.add_parser("avancar-slot")
    p = sub.add_parser("payload")
    p.add_argument("post_dir")
    p.add_argument("--sha", required=True, help="commit já enviado ao GitHub que contém os slides")
    p.add_argument("--rascunho", action="store_true", help="cria como rascunho (aguardando aprovação)")
    ps = sub.add_parser("payload-story")
    ps.add_argument("post_dir")
    ps.add_argument("--sha", required=True, help="commit já enviado que contém story/story.jpg")
    ps.add_argument("--rascunho", action="store_true")
    args = ap.parse_args()

    if args.cmd == "proximo-horario":
        dt, slot = proximo_horario()
        print(json.dumps({"data_hora": dt.isoformat(), "slot": slot}, ensure_ascii=False))
    elif args.cmd == "avancar-slot":
        avancar_slot()
    elif args.cmd == "payload-story":
        print(json.dumps(payload_story(Path(args.post_dir), args.sha, args.rascunho), ensure_ascii=False, indent=2))
    else:
        print(json.dumps(payload(Path(args.post_dir), args.sha, args.rascunho), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
