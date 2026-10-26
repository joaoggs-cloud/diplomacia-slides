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
TEMPLATE_MODERNO = (RAIZ / "scripts" / "template_moderno.html").read_text(encoding="utf-8")


def data_uri(caminho, largura_max=1400, realce=False):
    """Embute a foto em base64, reduzida para o HTML não ficar gigante.
    `realce` dá um leve reforço de cor, contraste e nitidez (layout moderno)."""
    img = Image.open(caminho).convert("RGB")
    if img.width > largura_max:
        img = img.resize((largura_max, round(img.height * largura_max / img.width)), Image.LANCZOS)
    if realce:
        from PIL import ImageEnhance, ImageFilter
        img = ImageEnhance.Color(img).enhance(1.15)
        img = ImageEnhance.Contrast(img).enhance(1.06)
        img = img.filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2))
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


def montar_moderno(post, post_dir):
    """Layout "moderno" (4:5, 1080x1350): foto em tela cheia, etiquetas acima da
    manchete e texto sobre o degradê — no estilo dos perfis de notícia do Instagram."""
    imagens = {i["id"]: i for i in post.get("imagens", [])}
    logo = logo_uri()
    total = len(post["slides"]) + 2

    def fundo(img_id, foco=None):
        img = imagens.get(img_id)
        if not img:
            return '<div class="fallback"></div>', None
        pos = f' style="object-position:{escape(foco)}"' if foco else ""
        return f'<img class="bg" src="{data_uri(post_dir / img["arquivo"], 1600, realce=True)}"{pos} alt="">', img

    def rodape(img, direita=""):
        cred = escape(credito_curto(img)).replace("Foto:", "<b>Foto:</b>", 1)
        return (f'<div class="rodape"><span class="marca">Diplomacia da Guerra</span>'
                f'{direita or f"<span class=credito>{cred}</span>"}</div>')

    capa = post["capa"]
    bg, img = fundo(capa["imagem"], capa.get("foco"))
    partes = [p.strip() for p in post.get("categoria", "Geopolítica").split("·") if p.strip()]
    pills = [f'<span class="pill cat">{escape(partes[0])}</span>']
    pills += [f'<span class="pill esc">{escape(p)}</span>' for p in partes[1:]]
    if post.get("fontes"):
        n = len(post["fontes"])
        pills.append(f'<span class="pill cla">{n} fonte{"s" if n > 1 else ""}</span>')
    cred_capa = escape(capa.get("credito") or credito_curto(img)).replace("Foto:", "<b>Foto:</b>", 1)
    # Notícia de imagem única: só a capa, com quadros de indicadores opcionais.
    so_capa = post.get("formato") == "noticia"
    indicadores = ""
    if capa.get("indicadores"):
        indicadores = '<div class="inds">' + "".join(
            f'<div class="ind"><div class="ind-v {escape(i.get("cor", ""))}">{escape(i["valor"])}</div>'
            f'<div class="ind-r">{escape(i["rotulo"])}</div></div>' for i in capa["indicadores"]) + "</div>"
    html = [f'''
  <div class="slide">
    {bg}<div class="grad{' noticia' if so_capa else ''}"></div>
    <img class="logo" src="{logo}" alt="">
    <div class="corpo">
      <div class="pills">{"".join(pills)}</div>
      <h1 class="manchete">{capa["titulo_html"]}</h1>
      <p class="linha-fina">{capa["gancho"]}</p>
      {indicadores}
      <div class="rodape"><span class="marca">Diplomacia da Guerra</span>{"" if so_capa else '<span class="setas">›››</span>'}</div>
      <div class="credito" style="max-width:100%;margin-top:6px">{cred_capa}</div>
    </div>
  </div>''']
    if so_capa:
        return (TEMPLATE_MODERNO
                .replace("{{TITULO}}", escape(post.get("titulo_interno", post["slug"])))
                .replace("{{SLIDES}}", "\n".join(html)))

    for n, s in enumerate(post["slides"], start=2):
        bg, img = fundo(s.get("imagem"), s.get("foco"))
        extras = ""
        if s.get("numero"):
            extras += (f'<div class="numero">{escape(s["numero"]["valor"])}</div>'
                       f'<div class="numero-rot">{escape(s["numero"].get("label", ""))}</div>')
        if s.get("factbox"):
            f = s["factbox"]
            extras += f'<div class="destaque"><div class="rot">{escape(f.get("label", "Fato"))}</div><p>{f["texto"]}</p></div>'
        if s.get("citacao"):
            c = s["citacao"]
            extras += f'<div class="destaque"><p>{c["texto"]}</p><cite>— {escape(c.get("autor", ""))}</cite></div>'
        html.append(f'''
  <div class="slide">
    {bg}<div class="grad forte"></div>
    <img class="logo" src="{logo}" alt="">
    <div class="contador">{n}/{total}</div>
    <div class="corpo">
      <div class="pills"><span class="pill cat">{escape(s.get("tag", ""))}</span></div>
      <div class="titulo">{escape(s["titulo"])}</div>
      <div class="texto">{s["texto_html"]}</div>
      {extras}
      {rodape(img)}
    </div>
  </div>''')

    cta = post.get("cta", {})
    html.append(f'''
  <div class="slide cta">
    <div class="contador">{total}/{total}</div>
    <div class="centro">
      <img class="cta-logo" src="{logo}" alt="Diplomacia da Guerra">
      <div class="cta-h">{escape(cta.get("titulo", "Salve este post"))}</div>
      <div class="cta-sub">{escape(cta.get("subtitulo", "e compartilhe com quem precisa saber"))}</div>
      <div class="cta-btn">Siga @diplomaciadaguerra</div>
    </div>
  </div>''')
    return (TEMPLATE_MODERNO
            .replace("{{TITULO}}", escape(post.get("titulo_interno", post["slug"])))
            .replace("{{SLIDES}}", "\n".join(html)))


def layout_do_post(post):
    if post.get("layout"):
        return post["layout"]
    try:
        est = json.loads((RAIZ / "config" / "estrategia.json").read_text(encoding="utf-8"))
        return est.get("layout", "classico")
    except (OSError, ValueError):
        return "classico"


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
    # Foto do vencedor ocupando o card inteiro; textos sobre um degradê na base.
    slide = f'''
  <div class="slide venc">
    <img class="v-bg" src="{foto(v, 1400)}" alt="">
    <div class="v-grad"></div>
    <div class="v-faixa"></div>
    <div class="v-tag">{escape(n["tag"])}</div>
    <img class="v-logo" src="{logo_original_uri()}" alt="">
    <div class="v-body">
      <div class="v-eleito">{n["titulo_html"]}</div>
      <div class="v-nome">{escape(v["nome"])} <span class="v-partido">{escape(v.get("partido", ""))}</span></div>
      <div class="v-linha">
        <div><div class="v-pct">{escape(v["valor"])}</div><div class="v-votos">{escape(v.get("votos", ""))}</div></div>
        <div class="v-segundo">
          <img class="v-foto2" src="{foto(s2, 300)}" alt="">
          <div><div class="v-s-nome">{escape(s2["nome"])} <span>{escape(s2.get("partido", ""))}</span></div>
          <div class="v-s-pct">{escape(s2["valor"])}</div></div>
        </div>
      </div>
      <div class="v-foot"><span>{escape(n.get("rodape", ""))}</span><span class="v-handle">@diplomaciadaguerra</span></div>
      <div class="v-credit">{escape(n.get("credito", ""))}</div>
    </div>
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
        limite = 45 if layout_do_post(post) == "moderno" else 60
        if palavras > limite:
            erros.append(f"slide {i} tem {palavras} palavras (máx. {limite})")
    ids = {i["id"] for i in post.get("imagens", [])}
    for ref in [post["capa"]["imagem"], *[s.get("imagem") for s in post["slides"]]]:
        if ref and ref not in ids:
            erros.append(f"imagem {ref} ainda não foi baixada (rode scripts/imagens.py)")
    return erros


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("post_dir")
    ap.add_argument("--so-html", action="store_true")
    ap.add_argument("--layout", choices=["classico", "moderno"], help="força um layout (padrão: post.json ou estrategia.json)")
    ap.add_argument("--saida", help="pasta de saída dos JPEGs (padrão: <post>/slides) — use para prévias")
    args = ap.parse_args()
    post_dir = Path(args.post_dir).resolve()
    post = json.loads((post_dir / "post.json").read_text(encoding="utf-8"))

    for e in validar(post):
        print("AVISO:", e, file=sys.stderr)

    destino = Path(args.saida).resolve() if args.saida else post_dir / "slides"
    saida = (destino.parent / "carrossel.html") if args.saida else post_dir / "carrossel.html"
    if post.get("formato") == "noticia" and post.get("capa"):
        montar = montar_moderno
    elif post.get("formato") == "noticia":
        montar = montar_noticia
    else:
        montar = montar_moderno if (args.layout or layout_do_post(post)) == "moderno" else montar_html
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(montar(post, post_dir), encoding="utf-8")
    print(f"HTML: {saida}")
    if args.so_html:
        return
    subprocess.run(["node", str(RAIZ / "scripts" / "exportar_slides.js"), str(saida), str(destino)],
                   check=True)


if __name__ == "__main__":
    main()
