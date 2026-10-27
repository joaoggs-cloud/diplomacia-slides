#!/usr/bin/env python3
"""Lista os arquivos de categorias do Wikimedia Commons com data, autor e licença,
e baixa miniaturas para escolher fotos sem acesso direto ao Commons.

Roda no GitHub (workflow "Consultar Commons") a partir de consultas/<nome>.txt,
um pedido por linha:  Category:Nome da categoria   ou   busca livre
Grava consultas/<nome>/resultado.json e consultas/<nome>/NN.jpg (miniaturas),
ordenados do mais recente para o mais antigo, só com licenças livres.

Uso:
    python3 scripts/consulta_commons.py consultas/moraes-flavio.txt
"""
import io
import json
import sys
from pathlib import Path

import requests
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from imagens import API, UA, limpa, prioridade_licenca  # noqa: E402

LIMITE = 40


def membros(pedido):
    params = {"action": "query", "format": "json", "prop": "imageinfo",
              "iiprop": "url|size|mime|extmetadata|timestamp", "iiurlwidth": 400}
    if pedido.startswith("Category:"):
        params.update({"generator": "categorymembers", "gcmtitle": pedido,
                       "gcmtype": "file", "gcmlimit": LIMITE, "gcmsort": "timestamp", "gcmdir": "desc"})
    else:
        params.update({"generator": "search", "gsrsearch": f"{pedido} filetype:bitmap",
                       "gsrnamespace": 6, "gsrlimit": LIMITE})
    r = requests.get(API, params=params, headers={"User-Agent": UA}, timeout=60)
    r.raise_for_status()
    for p in r.json().get("query", {}).get("pages", {}).values():
        info = (p.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata", {})
        licenca = limpa(meta.get("LicenseShortName", {}).get("value"))
        if info.get("mime") not in ("image/jpeg", "image/png", "image/webp"):
            continue
        if prioridade_licenca(licenca) is None:
            continue
        yield {
            "titulo": p["title"],
            "data": limpa(meta.get("DateTimeOriginal", {}).get("value"))[:19],
            "envio": info.get("timestamp", ""),
            "autor": limpa(meta.get("Artist", {}).get("value")),
            "credito": limpa(meta.get("Credit", {}).get("value")),
            "licenca": licenca,
            "largura": info.get("width"),
            "altura": info.get("height"),
            "url_origem": info.get("descriptionurl"),
            "thumb": info.get("thumburl"),
        }


def main():
    pedido_txt = Path(sys.argv[1])
    pasta = pedido_txt.with_suffix("")
    pasta.mkdir(parents=True, exist_ok=True)
    vistos, itens = set(), []
    for linha in pedido_txt.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        for item in membros(linha):
            if item["titulo"] not in vistos:
                vistos.add(item["titulo"])
                item["pedido"] = linha
                itens.append(item)
    # Mais recentes primeiro (data da foto; sem ela, data de envio).
    itens.sort(key=lambda i: i["data"] or i["envio"], reverse=True)
    for n, item in enumerate(itens, start=1):
        if not item["thumb"]:
            continue
        try:
            r = requests.get(item["thumb"], headers={"User-Agent": UA}, timeout=60)
            r.raise_for_status()
            arquivo = f"{n:02d}.jpg"
            Image.open(io.BytesIO(r.content)).convert("RGB").save(pasta / arquivo, "JPEG", quality=85)
            item["miniatura"] = arquivo
        except Exception as e:  # miniatura é só conveniência
            item["erro_miniatura"] = str(e)
    (pasta / "resultado.json").write_text(json.dumps(itens, ensure_ascii=False, indent=2) + "\n",
                                          encoding="utf-8")
    print(f"{len(itens)} arquivos livres em {pasta}/resultado.json")


if __name__ == "__main__":
    main()
