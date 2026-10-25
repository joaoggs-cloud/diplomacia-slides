#!/usr/bin/env python3
"""Gera o carrossel (HTML navegável + JPEGs 1080x1080) a partir do post.json.

Segue a identidade visual da skill carrossel-instagram: capa com foto e
gradiente, slides de conteúdo com foto no topo, fact box / citação / número
grande opcionais, marca d'água com a logo e CTA final.

Uso:
    python3 scripts/render.py posts/2026-10-26-slug          # HTML + JPEGs
    python3 scripts/render.py posts/2026-10-26-slug --so-html
"""
import argparse
import base64
import io
import json
import re
import subprocess
import sys
from html import escape
from pathlib import Path

import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
TEMPLATE = (RAIZ / "scripts" / "template.html").read_text(encoding="utf-8")


def data_uri(caminho, largura_max=1400):
    """Embute a foto em base64, reduzida para o HTML não ficar gigante."""
    img = Image.open(caminho).convert("RGB")
    if img.width > largura_max:
        img = img.resize((largura_max, round(img.height * largura_max / img.width)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=88)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def logo_uri():
    """Logo sem o fundo creme e com tanque/texto em creme claro (receita da skill)."""
    img = Image.open(RAIZ / "assets" / "logo.png").convert("RGBA")
    arr = np.array(img, dtype=np.float32)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    bg = (r > 180) & (g > 170) & (b > 150) & (r < 245) & (g < 240) & (b < 230)
    escuro = (r < 60) & (g < 60) & (b < 60)
    medio = (r > 80) & (r < 180) & ~bg & ~escuro
    out = arr.copy()
    out[bg, 3] = 0
    out[escuro, 0:3] = [240, 234, 214]
    out[escuro, 3] = 255
    out[medio, 0:3] = np.clip(out[medio, 0:3] * 1.6, 0, 255)
    out[medio, 3] = 200
    buf = io.BytesIO()
    Image.fromarray(out.astype(np.uint8), "RGBA").save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def credito_curto(img):
    if not img:
        return ""
    if not img.get("exige_credito"):
        return "Foto: domínio público · Wikimedia Commons"
    autor = img["autor"]
    if len(autor) > 40:
        autor = autor[:38] + "…"
    return f"Foto: {autor} · {img['licenca']}"


def bloco_extra(slide):
    partes = []
    if slide.get("numero"):
        n = slide["numero"]
        partes.append(f'<div class="hn">{escape(n["valor"])}</div>'
                      f'<div class="hlabel">{escape(n.get("label", ""))}</div>')
    if slide.get("factbox"):
        f = slide["factbox"]
        partes.append(f'<div class="fb"><div class="ft">{escape(f.get("label", "Fato"))}</div>'
                      f'<p>{f["texto"]}</p></div>')
    if slide.get("citacao"):
        c = slide["citacao"]
        partes.append(f'<blockquote>{c["texto"]}<cite>— {escape(c.get("autor", ""))}</cite></blockquote>')
    return "\n".join(partes)


def montar_html(post, post_dir):
    imagens = {i["id"]: i for i in post.get("imagens", [])}
    logo = logo_uri()
    total = len(post["slides"]) + 2

    def foto(img_id):
        img = imagens.get(img_id)
        if not img:
            return "", None
        return data_uri(post_dir / img["arquivo"]), img

    capa = post["capa"]
    src, img = foto(capa["imagem"])
    html_slides = [f'''
  <div class="slide capa">
    {f'<img class="capa-photo" src="{src}" alt="">' if src else '<div class="capa-photo fallback"></div>'}
    <div class="capa-grad"></div>
    <div class="capa-body">
      <div class="capa-tag">{escape(post.get("categoria", "GEOPOLÍTICA"))}</div>
      <h1 class="capa-title">{capa["titulo_html"]}</h1>
      <p class="capa-hook">{capa["gancho"]}</p>
    </div>
    <div class="credit capa-credit">{escape(credito_curto(img))}</div>
    <div class="capa-line"></div>
  </div>''']

    for n, s in enumerate(post["slides"], start=2):
        src, img = foto(s.get("imagem"))
        # "foco" escolhe o enquadramento da foto na faixa de 210px (ex.: "center 85%").
        foco = f' style="object-position:{escape(s["foco"])}"' if s.get("foco") else ""
        html_slides.append(f'''
  <div class="slide">
    <div class="s-photo">
      {f'<img src="{src}"{foco} alt="">' if src else '<div class="fallback"></div>'}
      <div class="s-photo-grad"></div>
      <div class="s-photo-num">{n:02d} / {total:02d}</div>
      <div class="s-photo-tag">{escape(s.get("tag", ""))}</div>
      <div class="credit">{escape(credito_curto(img))}</div>
    </div>
    <div class="s-content">
      <div>
        <div class="s-title">{escape(s["titulo"])}</div>
        <div class="s-div"></div>
        <div class="s-body">{s["texto_html"]}</div>
      </div>
      {bloco_extra(s)}
      <div class="s-footer"><span class="s-pn">Diplomacia da Guerra</span><span class="s-handle">@diplomaciadaguerra</span></div>
    </div>
    <img class="wm" src="{logo}" alt="">
  </div>''')

    cta = post.get("cta", {})
    html_slides.append(f'''
  <div class="slide cta">
    <div class="cta-b1"></div><div class="cta-b2"></div>
    <img class="cta-logo" src="{logo}" alt="Diplomacia da Guerra">
    <div class="cta-div"></div>
    <div class="cta-h">{escape(cta.get("titulo", "Salve este post"))}</div>
    <div class="cta-sub">{escape(cta.get("subtitulo", "e compartilhe com quem precisa saber"))}</div>
    <div class="cta-handle">@diplomaciadaguerra</div>
  </div>''')

    return (TEMPLATE
            .replace("{{TITULO}}", escape(post.get("titulo_interno", post["slug"])))
            .replace("{{SLIDES}}", "\n".join(html_slides)))


def logo_original_uri():
    """Logo como é (fundo creme), para os cards de fundo claro."""
    return data_uri(RAIZ / "assets" / "logo.png", 300)


def montar_vencedor(post, post_dir):
    """Card claro e colorido de resultado oficial: vencedor em destaque, segundo colocado abaixo.
    Paleta âmbar/turquesa, propositalmente sem as cores associadas a partidos."""
    n = post["noticia"]
    imagens = {i["id"]: i for i in post.get("imagens", [])}

    def foto(c, largura):
        f = imagens.get(c.get("foto"))
        return data_uri(post_dir / f["arquivo"], largura) if f else ""

    v, s2 = n["vencedor"], n["segundo"]
    slide = f'''
  <div class="slide venc">
    <div class="v-faixa"></div>
    <img class="v-logo" src="{logo_original_uri()}" alt="">
    <div class="v-tag">{escape(n["tag"])}</div>
    <div class="v-main">
      <div class="v-foto-wrap"><img class="v-foto" src="{foto(v, 600)}" alt=""></div>
      <div class="v-info">
        <div class="v-eleito">{n["titulo_html"]}</div>
        <div class="v-nome">{escape(v["nome"])}</div>
        <div class="v-partido">{escape(v.get("partido", ""))}</div>
        <div class="v-pct">{escape(v["valor"])}</div>
        <div class="v-votos">{escape(v.get("votos", ""))}</div>
      </div>
    </div>
    <div class="v-segundo">
      <img class="v-foto2" src="{foto(s2, 300)}" alt="">
      <div class="v-s-nome">{escape(s2["nome"])} <span>{escape(s2.get("partido", ""))}</span></div>
      <div class="v-s-pct">{escape(s2["valor"])}</div>
    </div>
    <p class="v-sub">{n.get("subtitulo_html", "")}</p>
    <div class="v-foot"><span>{escape(n.get("rodape", ""))}</span><span class="v-handle">@diplomaciadaguerra</span></div>
    <div class="v-credit">{escape(n.get("credito", ""))}</div>
  </div>'''
    return (TEMPLATE
            .replace("{{TITULO}}", escape(post.get("titulo_interno", post["slug"])))
            .replace("{{SLIDES}}", slide))


def montar_noticia(post, post_dir):
    """Formato "noticia": uma imagem só, para fatos do momento (placar, anúncio, alerta)."""
    n = post["noticia"]
    if n.get("tema") == "vencedor":
        return montar_vencedor(post, post_dir)
    img = next((i for i in post.get("imagens", []) if i["id"] == n.get("imagem")), None)
    fundo = (f'<img class="n-photo" src="{data_uri(post_dir / img["arquivo"])}" alt="">'
             if img else '<div class="fallback"></div>')
    imagens = {i["id"]: i for i in post.get("imagens", [])}

    def retrato(c):
        # Mesmo tamanho e mesmo tratamento para todos os retratos (isenção).
        foto = imagens.get(c.get("foto"))
        return f'<img class="n-foto" src="{data_uri(post_dir / foto["arquivo"], 400)}" alt="">' if foto else ""

    placar = "".join(
        f'<div class="n-cand">{retrato(c)}<div><div class="n-pct">{escape(c["valor"])}</div>'
        f'<div class="n-nome">{escape(c["nome"])}</div><div class="n-partido">{escape(c.get("partido", ""))}</div></div></div>'
        for c in n.get("placar", []))
    slide = f'''
  <div class="slide noticia">
    {fundo}
    <div class="n-grad"></div>
    <div class="n-body">
      <div class="n-tag">{escape(n["tag"])}</div>
      <h1 class="n-title">{n["titulo_html"]}</h1>
      {f'<div class="n-placar">{placar}</div>' if placar else ''}
      <p class="n-sub">{n.get("subtitulo_html", "")}</p>
      <div class="n-foot"><span>{escape(n.get("rodape", ""))}</span><span class="n-handle">@diplomaciadaguerra</span></div>
    </div>
    <div class="credit capa-credit">{escape(n.get("credito") or credito_curto(img))}</div>
    <img class="n-logo" src="{logo_uri()}" alt="">
    <div class="capa-line"></div>
  </div>'''
    return (TEMPLATE
            .replace("{{TITULO}}", escape(post.get("titulo_interno", post["slug"])))
            .replace("{{SLIDES}}", slide))


def validar(post):
    erros = []
    if post.get("formato") == "noticia":
        return erros
    n = len(post["slides"]) + 2
    if not 8 <= n <= 10:
        erros.append(f"o carrossel tem {n} slides (capa + conteúdo + CTA); o padrão é 8 a 10")
    for i, s in enumerate(post["slides"], start=2):
        palavras = len(re.sub(r"<[^>]+>", " ", s["texto_html"]).split())
        if palavras > 60:
            erros.append(f"slide {i} tem {palavras} palavras (máx. 60)")
    ids = {i["id"] for i in post.get("imagens", [])}
    for ref in [post["capa"]["imagem"], *[s.get("imagem") for s in post["slides"]]]:
        if ref and ref not in ids:
            erros.append(f"imagem {ref} ainda não foi baixada (rode scripts/imagens.py)")
    return erros


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("post_dir")
    ap.add_argument("--so-html", action="store_true")
    args = ap.parse_args()
    post_dir = Path(args.post_dir).resolve()
    post = json.loads((post_dir / "post.json").read_text(encoding="utf-8"))

    for e in validar(post):
        print("AVISO:", e, file=sys.stderr)

    saida = post_dir / "carrossel.html"
    montar = montar_noticia if post.get("formato") == "noticia" else montar_html
    saida.write_text(montar(post, post_dir), encoding="utf-8")
    print(f"HTML: {saida}")
    if args.so_html:
        return
    subprocess.run(["node", str(RAIZ / "scripts" / "exportar_slides.js"), str(saida), str(post_dir / "slides")],
                   check=True)


if __name__ == "__main__":
    main()
