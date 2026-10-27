#!/usr/bin/env python3
"""Gera o Story (1080x1920) que repete o post do feed: a capa centralizada sobre
o fundo desfocado da própria capa, sem nenhum texto extra (pedido do João).

Uso:
    python3 scripts/story.py posts/<slug>        # -> posts/<slug>/story/story.jpg
"""
import base64
import subprocess
import sys
from pathlib import Path

JS = """
const {chromium} = require('playwright');
(async () => {
  const [html, out] = process.argv.slice(1);
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 540, height: 960}, deviceScaleFactor: 2});
  await p.goto('file://' + html, {waitUntil: 'networkidle'});
  await (await p.$('.st')).screenshot({path: out, type: 'jpeg', quality: 92});
  await b.close();
})();
"""


def main():
    post_dir = Path(sys.argv[1]).resolve()
    capa = post_dir / "slides" / "01.jpg"
    if not capa.exists():
        sys.exit(f"{capa} não existe — renderize os slides antes.")
    img = base64.b64encode(capa.read_bytes()).decode()
    # Capa 4:5 do carrossel, ou quadrada no formato notícia antigo: mantém a proporção.
    from PIL import Image
    w, h = Image.open(capa).size
    largura = 460
    altura = round(largura * h / w)
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#000}}
.st{{width:540px;height:960px;position:relative;overflow:hidden;background:#000}}
.bg{{position:absolute;inset:-40px;background:url(data:image/jpeg;base64,{img}) center/cover;filter:blur(28px) brightness(.35)}}
.card{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:{largura}px;height:{altura}px;
border-radius:14px;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.7)}}
.card img{{width:100%;height:100%;object-fit:cover;display:block}}
</style></head><body><div class="st"><div class="bg"></div>
<div class="card"><img src="data:image/jpeg;base64,{img}" alt=""></div></div></body></html>"""
    pasta = post_dir / "story"
    pasta.mkdir(exist_ok=True)
    (pasta / "story.html").write_text(html, encoding="utf-8")
    subprocess.run(["node", "-e", JS, str(pasta / "story.html"), str(pasta / "story.jpg")], check=True)
    print(pasta / "story.jpg")


if __name__ == "__main__":
    main()
