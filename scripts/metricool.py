#!/usr/bin/env python3
"""Ponte entre os posts do repositório e o Metricool.

O agendamento em si é feito pelo Claude com as ferramentas MCP do Metricool;
este script só calcula o próximo horário e monta o JSON `info` exato que
createScheduledPost / updateScheduledPost esperam.

Uso:
    python3 scripts/metricool.py proximo-horario
    python3 scripts/metricool.py payload posts/<slug> --sha <commit> [--rascunho]
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


def carregar_estrategia():
    return json.loads(ESTRATEGIA.read_text(encoding="utf-8"))


def posts_existentes():
    for p in sorted((RAIZ / "posts").glob("*/post.json")):
        yield p.parent, json.loads(p.read_text(encoding="utf-8"))


def proximo_horario(agora=None):
    """Próximo dia preferido livre depois do último post já agendado/aprovado,
    no slot da vez (rotação na exploração, melhor slot ~70% na otimização)."""
    est = carregar_estrategia()
    tz = ZoneInfo(est["metricool"]["timezone"])
    agora = agora or datetime.now(tz)

    ocupados = set()
    ultimo = agora
    for _, post in posts_existentes():
        quando = post.get("agendamento", {}).get("data_hora")
        if quando and post.get("status") not in ("rejeitado", "descartado"):
            dt = datetime.fromisoformat(quando).astimezone(tz)
            ocupados.add(dt.date())
            ultimo = max(ultimo, dt)

    h = est["horarios"]
    indice = h.get("proximo_slot_indice", 0)
    if est.get("fase") == "otimizacao" and h.get("melhor_slot") and indice % 10 < 7:
        slot = h["melhor_slot"]
    else:
        slot = h["slots"][indice % len(h["slots"])]
    hora, minuto = map(int, slot.split(":"))

    # Começa no dia seguinte ao último post para respeitar o espaçamento,
    # mas nunca antes de amanhã — o post precisa de tempo para ser aprovado.
    dia = max(ultimo.date(), agora.date()) + timedelta(days=1)
    for _ in range(14):
        if DIAS[dia.weekday()] in est["dias_preferidos"] and dia not in ocupados:
            break
        dia += timedelta(days=1)
    return datetime(dia.year, dia.month, dia.day, hora, minuto, tzinfo=tz), slot


def avancar_slot():
    est = carregar_estrategia()
    est["horarios"]["proximo_slot_indice"] = est["horarios"].get("proximo_slot_indice", 0) + 1
    ESTRATEGIA.write_text(json.dumps(est, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def creditos(post):
    linhas = []
    for img in post.get("imagens", []):
        if img.get("exige_credito"):
            linhas.append(f"{img['autor']} ({img['licenca']})")
    if not linhas:
        return "📷 Imagens: domínio público via Wikimedia Commons."
    unicos = list(dict.fromkeys(linhas))
    return "📷 Imagens via Wikimedia Commons: " + "; ".join(unicos) + ". Demais: domínio público."


def textos_alternativos(post, n):
    """Um texto alternativo por slide (acessibilidade): capa, títulos e CTA."""
    capa = re.sub(r"<[^>]+>", "", post["capa"]["titulo_html"])
    textos = [f"Capa: {capa}. {re.sub(r'<[^>]+>', '', post['capa']['gancho'])}"]
    textos += [f"Slide {i}: {s['titulo']}" for i, s in enumerate(post["slides"], start=2)]
    textos.append("Diplomacia da Guerra — salve este post e siga @diplomaciadaguerra")
    return textos[:n] if len(textos) >= n else textos + [post.get("alt_text", "")] * (n - len(textos))


def montar_legenda(post, est):
    hashtags = list(dict.fromkeys(post.get("hashtags", []) + est["hashtags_base"]))[: est["max_hashtags"]]
    partes = [post["legenda"].strip()]
    if post.get("fontes"):
        partes.append("Fontes: " + ", ".join(f["nome"] for f in post["fontes"]) + ".")
    partes.append(creditos(post))
    partes.append(" ".join(hashtags))
    texto = "\n\n".join(partes)
    if len(texto) > LIMITE_LEGENDA:
        sys.exit(f"Legenda com {len(texto)} caracteres (limite {LIMITE_LEGENDA}). Encurte post.json → legenda.")
    return texto


def payload(post_dir, sha, rascunho):
    est = carregar_estrategia()
    post = json.loads((post_dir / "post.json").read_text(encoding="utf-8"))
    repo = est["repositorio"]
    rel = post_dir.resolve().relative_to(RAIZ).as_posix()
    slides = sorted((post_dir / "slides").glob("*.jpg"))
    if not 2 <= len(slides) <= 20:
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


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("proximo-horario")
    sub.add_parser("avancar-slot")
    p = sub.add_parser("payload")
    p.add_argument("post_dir")
    p.add_argument("--sha", required=True, help="commit já enviado ao GitHub que contém os slides")
    p.add_argument("--rascunho", action="store_true", help="cria como rascunho (aguardando aprovação)")
    args = ap.parse_args()

    if args.cmd == "proximo-horario":
        dt, slot = proximo_horario()
        print(json.dumps({"data_hora": dt.isoformat(), "slot": slot}, ensure_ascii=False))
    elif args.cmd == "avancar-slot":
        avancar_slot()
    else:
        print(json.dumps(payload(Path(args.post_dir), args.sha, args.rascunho), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
