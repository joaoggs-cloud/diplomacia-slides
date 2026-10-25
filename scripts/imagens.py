#!/usr/bin/env python3
"""Busca imagens livres de direitos no Wikimedia Commons para um post.

Lê `busca_imagens` do post.json, procura cada consulta no Commons, mantém só
licenças que permitem uso comercial em rede social (domínio público, CC0,
CC BY, CC BY-SA), baixa a melhor candidata em ~1600px e grava autor, licença
e link de origem em `imagens` do post.json — esses dados viram os créditos
no slide e na legenda.

Uso:
    python3 scripts/imagens.py posts/2026-10-26-slug
    python3 scripts/imagens.py posts/2026-10-26-slug --candidatos 4   # baixa alternativas para escolher
    python3 scripts/imagens.py posts/2026-10-26-slug --so img03       # troca só a img03 por outra
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

import requests

API = "https://commons.wikimedia.org/w/api.php"
UA = "DiplomaciaDaGuerraBot/1.0 (https://github.com/joaoggs-cloud/diplomacia-slides)"

# Ordem de preferência: domínio público primeiro (sem obrigação de crédito),
# depois CC0, depois licenças que exigem atribuição.
LICENCAS_OK = [
    (re.compile(r"public domain|^pd\b|pd-", re.I), 0),
    (re.compile(r"cc0", re.I), 1),
    (re.compile(r"cc[ -]by[ -]\d", re.I), 2),
    (re.compile(r"cc[ -]by[ -]sa", re.I), 3),
]
# Licenças "NC"/"ND" ou fair use nunca entram.
LICENCAS_BLOQUEADAS = re.compile(r"\bnc\b|\bnd\b|non-?commercial|no ?deriv|fair use", re.I)


def limpa(texto):
    texto = re.sub(r"<[^>]+>", "", texto or "")
    return html.unescape(texto).strip()


def prioridade_licenca(nome):
    if not nome or LICENCAS_BLOQUEADAS.search(nome):
        return None
    for padrao, prio in LICENCAS_OK:
        if padrao.search(nome):
            return prio
    return None


def buscar(consulta, limite=20):
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": f"{consulta} filetype:bitmap",
        "gsrnamespace": 6,
        "gsrlimit": limite,
        "prop": "imageinfo",
        "iiprop": "url|size|mime|extmetadata",
        "iiurlwidth": 1600,
    }
    r = requests.get(API, params=params, headers={"User-Agent": UA}, timeout=30)
    r.raise_for_status()
    paginas = r.json().get("query", {}).get("pages", {})
    candidatos = []
    for p in sorted(paginas.values(), key=lambda p: p.get("index", 999)):
        info = (p.get("imageinfo") or [{}])[0]
        if info.get("mime") not in ("image/jpeg", "image/png"):
            continue
        if min(info.get("width", 0), info.get("height", 0)) < 700:
            continue
        meta = info.get("extmetadata", {})
        licenca = limpa(meta.get("LicenseShortName", {}).get("value"))
        prio = prioridade_licenca(licenca)
        if prio is None:
            continue
        candidatos.append({
            "titulo": p["title"].removeprefix("File:"),
            "autor": limpa(meta.get("Artist", {}).get("value")) or "Autor desconhecido",
            "licenca": licenca,
            "exige_credito": prio >= 2,
            "url_origem": info.get("descriptionurl"),
            "url_download": info.get("thumburl") or info.get("url"),
            "largura": info.get("width"),
            "altura": info.get("height"),
            "_prio": prio,
        })
    # Mantém a relevância da busca, mas sobe licenças mais livres.
    candidatos.sort(key=lambda c: c["_prio"])
    return candidatos


def baixar(url, destino):
    r = requests.get(url, headers={"User-Agent": UA}, timeout=60)
    r.raise_for_status()
    destino.write_bytes(r.content)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("post_dir")
    ap.add_argument("--candidatos", type=int, default=1,
                    help="quantas opções baixar por imagem (as extras vão para imagens/candidatos/)")
    ap.add_argument("--so", help="processa só este id de imagem (ex.: img03)")
    ap.add_argument("--refazer", action="store_true", help="busca de novo mesmo as imagens já baixadas")
    args = ap.parse_args()

    post_dir = Path(args.post_dir)
    post_path = post_dir / "post.json"
    post = json.loads(post_path.read_text(encoding="utf-8"))
    pasta = post_dir / "imagens"
    pasta.mkdir(exist_ok=True)

    registradas = {i["id"]: i for i in post.get("imagens", [])}
    usadas = {i["url_origem"] for i in registradas.values()}
    falhas = []

    for pedido in post.get("busca_imagens", []):
        img_id = pedido["id"]
        if args.so and img_id != args.so:
            continue
        ja_tem = registradas.get(img_id)
        if ja_tem and (post_dir / ja_tem["arquivo"]).exists() and not (args.refazer or args.so):
            continue
        if ja_tem and args.refazer:
            usadas.discard(ja_tem["url_origem"])
        candidatos = []
        for consulta in [pedido["query"], *pedido.get("alternativas", [])]:
            candidatos = [c for c in buscar(consulta) if c["url_origem"] not in usadas]
            if candidatos:
                break
        if not candidatos:
            falhas.append(img_id)
            print(f"[{img_id}] nenhuma imagem livre para: {pedido['query']}", file=sys.stderr)
            continue

        escolhida = candidatos[0]
        arquivo = f"{img_id}.jpg"
        baixar(escolhida["url_download"], pasta / arquivo)
        usadas.add(escolhida["url_origem"])
        registro = {k: v for k, v in escolhida.items() if not k.startswith("_")}
        registro.update({"id": img_id, "arquivo": f"imagens/{arquivo}", "query": pedido["query"]})
        registradas[img_id] = registro
        print(f"[{img_id}] {escolhida['titulo']} — {escolhida['licenca']}")

        if args.candidatos > 1:
            extra = pasta / "candidatos"
            extra.mkdir(exist_ok=True)
            for n, c in enumerate(candidatos[1:args.candidatos], start=2):
                baixar(c["url_download"], extra / f"{img_id}_op{n}.jpg")
                (extra / f"{img_id}_op{n}.json").write_text(
                    json.dumps({k: v for k, v in c.items() if not k.startswith("_")},
                               ensure_ascii=False, indent=2), encoding="utf-8")

    post["imagens"] = sorted(registradas.values(), key=lambda i: i["id"])
    post_path.write_text(json.dumps(post, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if falhas:
        print("Sem imagem para: " + ", ".join(falhas) + " — ajuste as queries em busca_imagens.",
              file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
