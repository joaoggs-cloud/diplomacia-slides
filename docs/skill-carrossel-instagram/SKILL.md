---
name: carrossel-instagram
description: >
  Cria carrosseis de Instagram para a pagina Diplomacia da Guerra (geopolitica, conflitos, historia).
  ATIVAR IMEDIATAMENTE quando o usuario mencionar carrossel, fazer carrossel, criar post, post do insta,
  slides, conteudo para o instagram, ou enviar um tema/fatos pedindo para transformar em post.
  Tambem ativar quando o usuario descrever um tema de geopolitica, guerra, conflito ou historia e pedir
  para criar conteudo visual. Gera um arquivo HTML unico no layout "moderno" aprovado pelo Joao
  (formato vertical 4:5, foto colorida em tela cheia, etiquetas acima da manchete, fonte sem serifa),
  com fotos reais embutidas em base64, navegacao por setas e exportacao JPEG 1080x1350 por slide e em lote.
---

# Skill: Carrossel Instagram — Diplomacia da Guerra (layout moderno, out/2026)

Mesmo visual dos posts automáticos do sistema `diplomacia-slides`. Inspirado em perfis de notícia
(Ground News, Horizonte, Jovem Pan, O Antagonista).

## Regras de visual
- **Formato 4:5** — 1080×1350 px (HTML em 540×675 com escala 2 na exportação).
- **Foto em tela cheia em todos os slides**, colorida, clara e nítida. A metade de cima fica limpa;
  o degradê preto só cobre a faixa de baixo, onde vai o texto.
- **Preto e branco só estratégico**: fato histórico sem registro em cor, ou quando o efeito servir à história.
- Antes de embutir, dê um leve realce na foto (cor ×1.15, contraste ×1.06, nitidez/unsharp leve).
- Escolha fotos com o assunto **no centro ou no topo** (o texto cobre a parte de baixo).
- Fontes: **Montserrat 800** (manchete/títulos) e **Inter** (texto). Destaque em **dourado #e0b84f**.
- Logo da página em **branco** no canto superior direito (todos os slides).
- Rodapé: "| DIPLOMACIA DA GUERRA" à esquerda e "Foto: autor · licença" à direita.

## Estrutura
1. **Capa** — etiquetas (pills) acima da manchete: 1ª dourada com o tema, depois região/época em
   fundo escuro. Nunca usar etiqueta "N fontes" (decisão do João). Manchete grande (maiúsculas e minúsculas normais,
   palavras-chave em dourado), linha fina com o gancho, marca no rodapé e setas "›››" em dourado.
2. **Slides de conteúdo (6 a 8)** — contador "2/9" no canto superior esquerdo e um parágrafo
   corrido de até **45 palavras** (fonte maior, trechos-chave em dourado), que continua a história
   do slide anterior. **Sem título nem etiqueta** — no máximo 2 slides com título e 1 caixa de
   destaque por post; título em todo slide dá cara de conteúdo de IA. Legenda sem emojis.
3. **Slide final** — fundo escuro, logo grande, "Salve este post", subtítulo e botão dourado
   "Siga @diplomaciadaguerra".

Total: 8 a 10 slides. Tom sério, isento, sem sensacionalismo; todo fato com fonte; imagens só
com licença livre (domínio público, CC0, CC BY, CC BY-SA) e crédito no slide.

## Logo
`assets/logo.png` tem fundo creme. Remova o fundo (Pillow/numpy: pixels claros → transparentes,
escuros → creme) e embuta em base64; no CSS a classe `.logo` aplica
`filter: brightness(0) invert(1)` para deixá-la branca.

## CSS do layout
```html
<style>
:root{
  --w:540px;--h:675px;
  --gold:#e0b84f;--gold-d:#1c1500;--text:#ffffff;--muted:#c9c9c9;
}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#111;display:flex;flex-direction:column;align-items:center;min-height:100vh;font-family:'Inter',sans-serif;padding:20px 0 32px;}
.slide{width:var(--w);height:var(--h);background:#000;color:var(--text);position:relative;overflow:hidden;display:none;}
.slide.active{display:block;}
body.export .slide{display:block;margin-bottom:20px;}
body.export .controls{display:none;}

.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.fallback{position:absolute;inset:0;background:radial-gradient(circle at 60% 30%,#2a2a2a,#000 70%);}
.grad{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0.28) 0%,rgba(0,0,0,0) 13%,rgba(0,0,0,0) 54%,rgba(0,0,0,0.55) 68%,rgba(0,0,0,0.9) 84%,#000 100%);}
.grad.forte{background:linear-gradient(180deg,rgba(0,0,0,0.28) 0%,rgba(0,0,0,0) 13%,rgba(0,0,0,0) 46%,rgba(0,0,0,0.6) 60%,rgba(0,0,0,0.92) 76%,#000 100%);}

.logo{position:absolute;top:20px;right:22px;width:96px;z-index:5;filter:brightness(0) invert(1) drop-shadow(0 1px 6px rgba(0,0,0,.6));}
.contador{position:absolute;top:22px;left:22px;z-index:5;font-family:'Inter';font-weight:600;font-size:12px;color:#fff;background:rgba(0,0,0,.55);padding:4px 10px;border-radius:12px;}

.corpo{position:absolute;left:0;right:0;bottom:0;z-index:4;padding:0 26px 18px;text-shadow:0 1px 10px rgba(0,0,0,.55);}
.pills{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:12px;}
.pill{font-family:'Inter';font-weight:600;font-size:12.5px;padding:5px 9px;border-radius:3px;line-height:1;}
.pill.cat{background:var(--gold);color:var(--gold-d);}
.pill.esc{background:rgba(0,0,0,.6);color:#fff;}
.pill.cla{background:#fff;color:#111;}

.manchete{font-family:'Montserrat',sans-serif;font-weight:800;font-size:40px;line-height:1.12;letter-spacing:-0.3px;color:#fff;}
.manchete .hl,.manchete .hl2{color:var(--gold);}
.linha-fina{font-family:'Inter';font-weight:500;font-size:15px;line-height:1.45;color:var(--muted);margin-top:10px;}

.titulo{font-family:'Montserrat',sans-serif;font-weight:800;font-size:25px;line-height:1.15;color:#fff;margin-bottom:8px;}
.texto{font-family:'Inter';font-size:14.5px;line-height:1.5;color:#e6e6e6;}
.texto strong{color:#fff;font-weight:700;}
.texto em{color:var(--gold);font-style:normal;font-weight:700;}

.destaque{margin-top:10px;border-left:3px solid var(--gold);padding:7px 11px;background:rgba(0,0,0,.45);}
.destaque .rot{font-family:'Inter';font-weight:700;font-size:10.5px;letter-spacing:1.5px;text-transform:uppercase;color:var(--gold);margin-bottom:3px;}
.destaque p{font-family:'Inter';font-size:13.5px;line-height:1.45;color:#ddd;}
.destaque cite{display:block;margin-top:4px;font-style:normal;font-size:12px;color:var(--gold);}
.numero{font-family:'Montserrat';font-weight:800;font-size:46px;line-height:1;color:var(--gold);margin-top:10px;}
.numero-rot{font-family:'Inter';font-size:12px;color:var(--muted);margin-top:2px;}

.rodape{display:flex;justify-content:space-between;align-items:center;margin-top:12px;}
.marca{display:flex;align-items:center;gap:8px;font-family:'Montserrat';font-weight:700;font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:#fff;}
.marca::before{content:'';width:2px;height:16px;background:#fff;}
.credito{font-family:'Inter';font-size:9.5px;color:#9a9a9a;text-align:right;max-width:58%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.credito b{color:var(--gold);font-weight:600;}
.setas{font-family:'Montserrat';font-weight:800;font-size:28px;letter-spacing:-3px;color:var(--gold);}

/* CTA */
.cta{background:radial-gradient(circle at 50% 35%,#1f1a0c 0%,#000 70%);}
.cta .centro{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:40px;}
.cta-logo{width:210px;margin-bottom:26px;}
.cta-h{font-family:'Montserrat';font-weight:800;font-size:30px;line-height:1.15;color:#fff;}
.cta-sub{font-family:'Inter';font-size:15px;color:var(--muted);margin-top:10px;}
.cta-btn{margin-top:26px;font-family:'Inter';font-weight:700;font-size:15px;color:var(--gold-d);background:var(--gold);padding:10px 18px;border-radius:22px;}

</style>
```

## Marcação dos slides
```html
<!-- CAPA -->
<div class="slide">
  <img class="bg" src="[BASE64_FOTO]" alt=""><div class="grad"></div>
  <img class="logo" src="[BASE64_LOGO]" alt="">
  <div class="corpo">
    <div class="pills"><span class="pill cat">[Tema]</span><span class="pill esc">[Região]</span></div>
    <h1 class="manchete">[Manchete com <span class="hl2">destaque</span>]</h1>
    <p class="linha-fina">[Gancho em uma frase]</p>
    <div class="rodape"><span class="marca">Diplomacia da Guerra</span><span class="setas">›››</span></div>
    <div class="credito" style="max-width:100%;margin-top:6px"><b>Foto:</b> [autor · licença]</div>
  </div>
</div>

<!-- CONTEÚDO -->
<div class="slide">
  <img class="bg" src="[BASE64_FOTO]" style="object-position:center 30%" alt=""><div class="grad forte"></div>
  <img class="logo" src="[BASE64_LOGO]" alt="">
  <div class="contador">2/9</div>
  <div class="corpo">
    <div class="pills"><span class="pill cat">[Data ou tema]</span></div>
    <div class="titulo">[Título]</div>
    <div class="texto">[Texto com <strong>negrito</strong> e <em>destaque dourado</em>]</div>
    <div class="destaque"><div class="rot">[Rótulo]</div><p>[Fato complementar]</p></div>
    <div class="rodape"><span class="marca">Diplomacia da Guerra</span><span class="credito"><b>Foto:</b> [autor · licença]</span></div>
  </div>
</div>

<!-- FINAL -->
<div class="slide cta">
  <div class="contador">9/9</div>
  <div class="centro">
    <img class="cta-logo" src="[BASE64_LOGO]" alt="Diplomacia da Guerra">
    <div class="cta-h">Salve este post</div>
    <div class="cta-sub">e compartilhe com quem precisa saber</div>
    <div class="cta-btn">Siga @diplomaciadaguerra</div>
  </div>
</div>
```
Use `.slide{display:none}` + `.slide.active{display:block}` com botões Anterior/Próximo e teclas ←/→.

## Exportação
Inclua `https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js` e exporte cada
slide com `html2canvas(slide,{scale:2,useCORS:true,backgroundColor:'#000'})` → JPEG 1080×1350
(`canvas.toDataURL('image/jpeg',0.92)`), com botão "Exportar este slide" e "Exportar todos".

## Checklist
- [ ] 4:5, foto colorida em tela cheia em todos os slides (P&B só se justificado)
- [ ] Assunto da foto visível acima do texto; nada importante sob o degradê
- [ ] Capa com etiquetas, manchete, linha fina e setas
- [ ] Máx. 45 palavras por slide de conteúdo; contador em todos
- [ ] Logo branca, marca e crédito da foto em todos os slides
- [ ] Fatos com fonte; isenção; licenças livres
