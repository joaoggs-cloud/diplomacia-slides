#!/usr/bin/env python3
"""Baixa as URLs listadas em consultas/baixar/<nome>.txt (uma por linha) para
consultas/baixar/<nome>/, para a sessão do Claude ler dados oficiais que ela não
alcança (Tesouro Transparente, Banco Central, Câmara/Senado). Roda no GitHub.

Linhas "ckan:<url do package_show>" também baixam todos os recursos listados.
"""
import json
import re
import sys
from pathlib import Path

import requests

UA = "DiplomaciaDaGuerraBot/1.0 (https://github.com/joaoggs-cloud/diplomacia-slides)"
LIMITE_MB = 40


def nome_arquivo(n, url):
    base = re.sub(r"[^A-Za-z0-9._-]+", "_", url.split("?")[0].rstrip("/").split("/")[-1])[:80] or "arquivo"
    return f"{n:02d}-{base}"


def baixar(url, destino):
    r = requests.get(url, headers={"User-Agent": UA}, timeout=120, stream=True)
    r.raise_for_status()
    tamanho = 0
    with open(destino, "wb") as f:
        for bloco in r.iter_content(1 << 16):
            tamanho += len(bloco)
            if tamanho > LIMITE_MB * 2**20:
                raise RuntimeError(f"maior que {LIMITE_MB} MB")
            f.write(bloco)


def main():
    pedido = Path(sys.argv[1])
    pasta = pedido.with_suffix("")
    pasta.mkdir(parents=True, exist_ok=True)
    urls = []
    for linha in pedido.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        if linha.startswith("ckan:"):
            api = linha[5:]
            urls.append(api)
            try:
                dados = requests.get(api, headers={"User-Agent": UA}, timeout=60).json()
                urls += [r["url"] for r in dados["result"]["resources"]]
            except Exception as e:
                print(f"ckan falhou: {api}: {e}")
        else:
            urls.append(linha)
    log = []
    for n, url in enumerate(urls, start=1):
        arq = pasta / nome_arquivo(n, url)
        try:
            baixar(url, arq)
            log.append({"url": url, "arquivo": arq.name, "ok": True})
        except Exception as e:
            log.append({"url": url, "erro": str(e), "ok": False})
    (pasta / "log.json").write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{sum(l['ok'] for l in log)}/{len(log)} baixados em {pasta}")


if __name__ == "__main__":
    main()
