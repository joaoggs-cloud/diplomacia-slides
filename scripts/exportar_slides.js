// Exporta cada .slide do carrossel como JPEG 1080x1080 (540px CSS x escala 2).
// JPEG porque a API de publicação do Instagram só aceita esse formato para fotos.
// Uso: node scripts/exportar_slides.js posts/<slug>/carrossel.html posts/<slug>/slides
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const [html, outDir] = process.argv.slice(2);
  fs.mkdirSync(outDir, { recursive: true });
  for (const f of fs.readdirSync(outDir)) if (/\.(png|jpg)$/.test(f)) fs.unlinkSync(path.join(outDir, f));

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 700, height: 700 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.body.classList.add('export'));
  await page.evaluate(() => document.fonts.ready);

  const slides = await page.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    const file = path.join(outDir, String(i + 1).padStart(2, '0') + '.jpg');
    await slides[i].screenshot({ path: file, type: 'jpeg', quality: 92 });
    console.log(file);
  }
  await browser.close();
})();
