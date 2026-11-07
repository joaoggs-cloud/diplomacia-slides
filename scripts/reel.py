#!/usr/bin/env python3
"""Gera o Reel (vídeo 9:16, 1080x1920, 30 fps) de um carrossel.

Cada cena é uma foto do post em tela cheia, com zoom lento, e uma frase curta
na tela. A sequência é: capa (o gancho) → cenas de conteúdo → cartão final
("o carrossel completo está no perfil"). O objetivo do Reel é alcançar quem
ainda não segue a página (diagnóstico de 7 nov), então o gancho aparece já no
primeiro segundo e o texto fica fora das áreas que a interface do Instagram cobre.

As frases vêm de `post.json → reel.cenas` (escritas pelo roteirista, até
18 palavras cada). Sem esse bloco, o script usa a primeira frase de cada slide
e avisa: funciona, mas fica melhor com as frases escritas para o vídeo.

Uso:
    python3 scripts/reel.py posts/<slug>                    # -> reel/reel.mp4 + reel/capa.jpg + reel/cenas/NN.jpg
    python3 scripts/reel.py posts/<slug> --audio voz.m4a    # narração do João (o vídeo acompanha a duração)
    python3 scripts/reel.py posts/<slug> --se-dia-de-reel   # só gera se o post cair num dia de Reel (workflow)
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from html import escape, unescape
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render import credito_curto, logo_uri  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
DIAS = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
W, H, FPS = 1080, 1920, 30
ZOOM = 0.08            # quanto a foto cresce ao longo de cada cena
TRANSICAO = 0.35       # segundos de fusão entre cenas
MAX_PALAVRAS = 18
MAX_CENAS = 7          # sem contar capa e cartão final
MIN_LARGURA_TELA_CHEIA = 900   # px de largura útil no recorte 9:16; abaixo disso, foto em moldura
MOLDURA_TOPO, MOLDURA_ALT_MAX = 320, 960

JS = """
const {chromium} = require('playwright');
(async () => {
  const [html, outDir] = process.argv.slice(1);
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 540, height: 960}, deviceScaleFactor: 2});
  await p.goto('file://' + html, {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  const cenas = await p.$$('.cena');
  for (let i = 0; i < cenas.length; i++) {
    await cenas[i].screenshot({path: outDir + '/' + String(i + 1).padStart(2, '0') + '.png', omitBackground: true});
  }
  await b.close();
})();
"""

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:transparent}
.cena{width:540px;height:960px;position:relative;overflow:hidden;margin-bottom:10px;background:transparent}
.grad{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.45) 0%,rgba(0,0,0,0) 16%,rgba(0,0,0,0) 38%,rgba(0,0,0,.72) 56%,rgba(0,0,0,.88) 100%)}
.logo{position:absolute;top:62px;left:50%;transform:translateX(-50%);width:120px;filter:brightness(0) invert(1) drop-shadow(0 1px 6px rgba(0,0,0,.6))}
/* Área livre: a interface do Reel cobre ~200px embaixo e ~70px à direita (em 540x960). */
.corpo{position:absolute;left:30px;right:78px;bottom:205px;text-shadow:0 2px 12px rgba(0,0,0,.6)}
.pills{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:14px}
.pill{font-family:'Inter';font-weight:600;font-size:14px;padding:6px 10px;border-radius:3px;line-height:1}
.pill.cat{background:#e0b84f;color:#1c1500}.pill.esc{background:rgba(0,0,0,.6);color:#fff}
.manchete{font-family:'Montserrat',sans-serif;font-weight:800;font-size:40px;line-height:1.1;letter-spacing:-.3px;color:#fff}
.manchete .hl,.manchete .hl2,.frase em{color:#e0b84f;font-style:normal}
.gancho{font-family:'Inter';font-weight:500;font-size:18px;line-height:1.4;color:#d6d6d6;margin-top:12px}
.frase{font-family:'Montserrat',sans-serif;font-weight:700;font-size:30px;line-height:1.22;color:#fff}
.frase strong{font-weight:800}
.credito{position:absolute;left:30px;right:78px;bottom:178px;font-family:'Inter';font-size:10.5px;color:#a8a8a8;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-shadow:0 1px 4px rgba(0,0,0,.8)}
.fim{background:radial-gradient(circle at 50% 38%,#1f1a0c 0%,#000 72%)}
.fim .centro{position:absolute;inset:0 30px 190px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.fim img{width:230px;margin-bottom:30px}
.fim .h{font-family:'Montserrat';font-weight:800;font-size:32px;line-height:1.15;color:#fff}
.fim .s{font-family:'Inter';font-size:18px;color:#c9c9c9;margin-top:12px;line-height:1.4}
.fim .btn{margin-top:28px;font-family:'Inter';font-weight:700;font-size:18px;color:#1c1500;background:#e0b84f;padding:12px 22px;border-radius:26px}
"""


def palavras(html_txt):
    return len(re.sub(r"<[^>]+>", " ", unescape(html_txt)).split())


def primeira_frase(html_txt, limite=MAX_PALAVRAS):
    """Primeira frase do slide, cortada em `limite` palavras (plano B sem reel.cenas)."""
    texto = " ".join(re.sub(r"<[^>]+>", "", unescape(html_txt)).split())
    frase = re.split(r"(?<=[.!?])\s", texto, maxsplit=1)[0]
    ps = frase.split()
    return escape(" ".join(ps[:limite]) + ("…" if len(ps) > limite else ""))


def montar_cenas(post):
    """Lista de cenas: [{'tipo', 'imagem', 'foco', 'html'}]; avisa se usou o plano B."""
    reel = post.get("reel", {})
    capa = post["capa"]
    cenas = [{"tipo": "capa", "imagem": capa["imagem"], "foco": capa.get("foco"),
              "html": capa["titulo_html"], "gancho": reel.get("gancho", capa.get("gancho", ""))}]
    if reel.get("cenas"):
        for c in reel["cenas"]:
            cenas.append({"tipo": "frase", "imagem": c["imagem"], "foco": c.get("foco"), "html": c["texto_html"]})
    else:
        print("aviso: post.json sem reel.cenas — usando a primeira frase de cada slide. "
              "Para um Reel melhor, escreva reel.cenas (até 18 palavras por cena).", file=sys.stderr)
        for s in post["slides"][:MAX_CENAS]:
            if s.get("imagem"):
                cenas.append({"tipo": "frase", "imagem": s["imagem"], "foco": s.get("foco"),
                              "html": primeira_frase(s["texto_html"])})
    cenas.append({"tipo": "fim", "imagem": None, "html": reel.get("fim_titulo", "O carrossel completo está no perfil"),
                  "sub": reel.get("fim_subtitulo", "com as fontes e todos os detalhes")})
    return cenas


def validar(cenas):
    problemas = []
    meio = [c for c in cenas if c["tipo"] == "frase"]
    if not 3 <= len(meio) <= MAX_CENAS:
        problemas.append(f"{len(meio)} cenas de conteúdo (use de 3 a {MAX_CENAS}).")
    for i, c in enumerate(meio, start=2):
        n = palavras(c["html"])
        if n > MAX_PALAVRAS:
            problemas.append(f"cena {i}: {n} palavras (máx. {MAX_PALAVRAS}).")
    return problemas


def duracao(cena):
    if cena["tipo"] == "capa":
        return 3.2
    if cena["tipo"] == "fim":
        return 2.8
    # Tempo de leitura confortável: ~0,3 s por palavra + respiro.
    return round(min(6.0, max(3.0, 1.4 + 0.3 * palavras(cena["html"]))), 2)


def overlay_html(post, cenas, imagens):
    logo = logo_uri()
    partes = [p.strip() for p in post.get("categoria", "Geopolítica").split("·") if p.strip()]
    pills = f'<span class="pill cat">{escape(partes[0])}</span>' + "".join(
        f'<span class="pill esc">{escape(p)}</span>' for p in partes[1:])
    blocos = []
    for c in cenas:
        if c["tipo"] == "fim":
            blocos.append(f'''<div class="cena fim"><div class="centro"><img src="{logo}" alt="">
<div class="h">{escape(c["html"])}</div><div class="s">{escape(c["sub"])}</div>
<div class="btn">Siga @diplomaciadaguerra</div></div></div>''')
            continue
        cred = escape(credito_curto(imagens.get(c["imagem"])))
        if c["tipo"] == "capa":
            corpo = (f'<div class="pills">{pills}</div><h1 class="manchete">{c["html"]}</h1>'
                     + (f'<p class="gancho">{c["gancho"]}</p>' if c.get("gancho") else ""))
        else:
            corpo = f'<p class="frase">{c["html"]}</p>'
        blocos.append(f'''<div class="cena"><div class="grad"></div><img class="logo" src="{logo}" alt="">
<div class="corpo">{corpo}</div><div class="credito">{cred}</div></div>''')
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{"".join(blocos)}</body></html>'''


def realcar(img):
    img = ImageEnhance.Color(img).enhance(1.15)
    img = ImageEnhance.Contrast(img).enhance(1.06)
    return img.filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2))


def preparar_foto(origem, destino, foco):
    """Monta o fundo 1080x1920 da cena com o mesmo realce do carrossel.

    Foto que aguenta o recorte 9:16 vai em tela cheia. Foto larga demais (o caso
    comum: paisagens e fotos históricas) iria ficar borrada se fosse cortada, então
    entra inteira na parte de cima, sobre um fundo desfocado da própria foto."""
    img = Image.open(origem).convert("RGB")
    alvo = H / W
    # foco "X% Y%" (como o object-position do CSS) decide onde cortar.
    fx, fy = 0.5, 0.5
    nums = re.findall(r"(\d+(?:\.\d+)?)%", foco or "")
    if len(nums) >= 1:
        fx = float(nums[0]) / 100
    if len(nums) >= 2:
        fy = float(nums[1]) / 100

    def cobrir(im):
        if im.height / im.width < alvo:      # foto larga: corta as laterais
            nova_w = round(im.height / alvo)
            x = round((im.width - nova_w) * fx)
            return im.crop((x, 0, x + nova_w, im.height))
        nova_h = round(im.width * alvo)      # foto alta: corta em cima/embaixo
        y = round((im.height - nova_h) * fy)
        return im.crop((0, y, im.width, y + nova_h))

    recorte = cobrir(img)
    if recorte.width >= MIN_LARGURA_TELA_CHEIA:
        realcar(recorte.resize((W, H), Image.LANCZOS)).save(destino, quality=92)
        return "tela_cheia"
    fundo = cobrir(img).resize((W // 4, H // 4), Image.LANCZOS).filter(ImageFilter.GaussianBlur(10))
    fundo = ImageEnhance.Brightness(fundo.resize((W, H), Image.LANCZOS)).enhance(0.45)
    alt = min(round(W * img.height / img.width), MOLDURA_ALT_MAX)
    frente = img
    if img.height / img.width > MOLDURA_ALT_MAX / W:   # mais alta que o espaço: corta um pouco
        nova_h = round(img.width * MOLDURA_ALT_MAX / W)
        y = round((img.height - nova_h) * fy)
        frente = img.crop((0, y, img.width, y + nova_h))
    frente = realcar(frente.resize((W, alt), Image.LANCZOS))
    fundo.paste(frente, (0, MOLDURA_TOPO))
    fundo.save(destino, quality=92)
    return "moldura"


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args], check=True)


def gerar_clipe(foto, overlay, dur, saida, n):
    """Foto com zoom lento (alternando zoom-in e zoom-out) + texto que surge em 0,4 s."""
    frames = int(round(dur * FPS))
    # Uma só imagem de entrada: o zoompan gera os `frames` quadros (contador `on`).
    z = f"(1+{ZOOM}*on/{frames})" if n % 2 == 0 else f"(1+{ZOOM}-{ZOOM}*on/{frames})"
    if foto:
        # Escala grande antes do zoompan evita o tremido típico do filtro.
        fundo = (f"[0:v]scale={W * 2}:{H * 2},zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                 f":d={frames}:s={W}x{H}:fps={FPS},format=yuv420p[bg]")
        entradas = ["-i", str(foto)]
    else:
        fundo = f"[0:v]format=yuv420p[bg]"
        entradas = ["-f", "lavfi", "-t", str(dur), "-i", f"color=c=black:s={W}x{H}:r={FPS}"]
    filtro = (f"{fundo};[1:v]format=rgba,fade=in:st=0:d=0.4:alpha=1[ov];"
              f"[bg][ov]overlay=0:0:shortest=1,format=yuv420p[v]")
    ffmpeg(*entradas, "-loop", "1", "-t", str(dur), "-framerate", str(FPS), "-i", str(overlay),
           "-filter_complex", filtro, "-map", "[v]", "-r", str(FPS), "-frames:v", str(frames),
           "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", str(saida))


def duracao_audio(caminho):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                          str(caminho)], capture_output=True, text=True, check=True).stdout
    return float(out.strip())


def dia_de_reel(post):
    est = json.loads((RAIZ / "config" / "estrategia.json").read_text(encoding="utf-8"))
    cfg = est.get("reels", {})
    if not cfg.get("ativo") or post.get("formato") == "noticia":
        return False
    if post.get("reel", {}).get("gerar") is not None:
        return bool(post["reel"]["gerar"])
    quando = post.get("agendamento", {}).get("data_hora")
    if not quando:
        return False
    return DIAS[datetime.fromisoformat(quando).weekday()] in cfg.get("dias", [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("post_dir")
    ap.add_argument("--audio", help="narração (m4a/mp3/wav); as cenas se ajustam à duração dela")
    ap.add_argument("--se-dia-de-reel", action="store_true",
                    help="não faz nada se o post não cair num dia de Reel (config/estrategia.json → reels)")
    args = ap.parse_args()

    post_dir = Path(args.post_dir).resolve()
    post = json.loads((post_dir / "post.json").read_text(encoding="utf-8"))
    if args.se_dia_de_reel and not dia_de_reel(post):
        print(f"{post_dir.name}: não é dia de Reel, nada a fazer.")
        return
    if post.get("formato") == "noticia":
        sys.exit("Reel só para carrossel (o formato notícia é de imagem única).")

    imagens = {i["id"]: i for i in post.get("imagens", [])}
    cenas = montar_cenas(post)
    for c in cenas:
        if c["imagem"] and (c["imagem"] not in imagens or not (post_dir / imagens[c["imagem"]]["arquivo"]).exists()):
            sys.exit(f"Imagem {c['imagem']} não encontrada — rode scripts/imagens.py antes.")
    for p in validar(cenas):
        print("aviso:", p, file=sys.stderr)

    duracoes = [duracao(c) for c in cenas]
    if args.audio:
        total_audio = duracao_audio(args.audio) + 0.3
        # Mantém as proporções entre as cenas e estica/encolhe para caber na narração.
        bruto = sum(duracoes) - TRANSICAO * (len(cenas) - 1)
        fator = total_audio / bruto
        duracoes = [round(max(2.0, d * fator), 2) for d in duracoes]

    pasta = post_dir / "reel"
    (pasta / "cenas").mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        html = tmp / "overlay.html"
        html.write_text(overlay_html(post, cenas, imagens), encoding="utf-8")
        (tmp / "ov").mkdir()
        subprocess.run(["node", "-e", JS, str(html), str(tmp / "ov")], check=True)

        clipes = []
        for i, (c, d) in enumerate(zip(cenas, duracoes), start=1):
            foto = None
            if c["imagem"]:
                foto = tmp / f"foto{i:02d}.jpg"
                preparar_foto(post_dir / imagens[c["imagem"]]["arquivo"], foto, c.get("foco"))
            ov = tmp / "ov" / f"{i:02d}.png"
            # Quadro estático de cada cena, para a revisão visual (e a capa do Reel).
            quadro = Image.open(foto).convert("RGBA") if foto else Image.new("RGBA", (W, H), "black")
            quadro.alpha_composite(Image.open(ov).convert("RGBA").resize((W, H)))
            quadro.convert("RGB").save(pasta / "cenas" / f"{i:02d}.jpg", quality=90)
            clipe = tmp / f"cena{i:02d}.mp4"
            gerar_clipe(foto, ov, d, clipe, i)
            clipes.append(clipe)
        shutil.copy(pasta / "cenas" / "01.jpg", pasta / "capa.jpg")

        # Encadeia as cenas com fusão curta.
        entradas, filtro, anterior, offset = [], [], "[0:v]", 0.0
        for c in clipes:
            entradas += ["-i", str(c)]
        for i in range(1, len(clipes)):
            offset += duracoes[i - 1] - TRANSICAO
            rotulo = f"[x{i}]"
            filtro.append(f"{anterior}[{i}:v]xfade=transition=fade:duration={TRANSICAO}:offset={offset:.3f}{rotulo}")
            anterior = rotulo
        total = sum(duracoes) - TRANSICAO * (len(clipes) - 1)
        n = len(clipes)
        if args.audio:
            entradas += ["-i", str(Path(args.audio).resolve())]
            audio = [f"[{n}:a]aresample=48000,apad,atrim=0:{total:.3f}[a]"]
        else:
            # Faixa silenciosa: alguns players e a API rejeitam vídeo sem áudio.
            entradas += ["-f", "lavfi", "-t", f"{total:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
            audio = [f"[{n}:a]anull[a]"]
        ffmpeg(*entradas, "-filter_complex", ";".join(filtro + audio), "-map", anterior, "-map", "[a]",
               "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS),
               "-profile:v", "high", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
               "-t", f"{total:.3f}", str(pasta / "reel.mp4"))

    info = {"duracao_s": round(total, 1), "cenas": len(cenas), "narracao": bool(args.audio)}
    (pasta / "reel.json").write_text(json.dumps(info, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    tamanho = (pasta / "reel.mp4").stat().st_size / 1e6
    print(f"{pasta / 'reel.mp4'}  ({total:.1f} s, {len(cenas)} cenas, {tamanho:.1f} MB)")


if __name__ == "__main__":
    main()
