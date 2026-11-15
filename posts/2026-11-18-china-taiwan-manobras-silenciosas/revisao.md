REPROVADO

# Revisão: 2026-11-18-china-taiwan-manobras-silenciosas (commit 7a13d64)
Revisado em 15 nov 2026. Rodada 1.

| Item | Resultado |
|---|---|
| 1. Fatos (2 fontes, atribuição) | **problema**: slides 7 e 8, legenda e reel desatualizados (cúpula a três com Putin confirmada; Busan 2025 virou contexto velho); capa diz "100" em vez de "mais de 100" |
| 2. Isenção | ok (números atribuídos a Taipé, versão de Pequim nos slides 5 e 6, "Pequim não confirmou essa leitura") |
| 3. Imagens: licenças e créditos | ok nas licenças (todas conferidas na API do Commons). **problema**: o crédito do slide 8 aparece cortado, sem a licença legível |
| 3b. Imagens: qualidade e coerência | **problema**: capa e slide 2 com foto em baixa resolução, borradas; mapa do slide 6 esconde o assunto |
| 4. Texto | ok: até 45 palavras por slide, sem títulos nem factbox, sem emoji, sem pergunta ao leitor, primeiro_comentario vazio |
| 5. Visual (slides 01-09) | **problema**: capa e slide 2 borrados; slide 6 com Taiwan e a primeira cadeia de ilhas sob o degradê; no slide 8 a assinatura "Diplomacia da Guerra" quebra em 2 linhas (efeito do crédito longo) |
| 6. Legenda | 1.216 caracteres, dentro do limite. **problema** de conteúdo (ver C5) |
| 7. Reel (cenas 01-08, payload-reel) | **problema**: cenas 06 e 07 desatualizadas ou ambíguas; capa e cena 01 com "100" sem "mais de". Cenas 02, 03, 05 e 08 ok, todas com crédito |
| Story | ok no formato, mas precisa ser **regerado** depois da troca da capa |
| Data | ok: APEC em Shenzhen nos dias 18 e 19 nov, com Trump confirmado pela Casa Branca |

## Fatos conferidos de novo (WebSearch extended, 15 nov)
- Mais de 100 navios, informados por Joseph Wu (secretário-geral do NSC) em 3 nov: confirmado (Reuters via Star-Advertiser, Taipei Times 14 nov, Maritime Executive).
- Cerca de 70 navios dentro da primeira cadeia de ilhas: confirmado (Reuters 13 nov / Taipei Times 13 nov, citando dois funcionários de segurança).
- Comandos Leste, Norte e Sul, e mobilização maior que a da Justice Mission 2025: confirmado (Reuters/Kyiv Post, Taipei Times 14 nov; Justice Mission em 29 e 30 dez 2025 segundo USNI e Wikipedia).
- Koo, em 10 nov, sobre "negação de área" com o Liaoning, e a versão de Pequim ("rotina anual", "não dirigido a nenhum país"): confirmado (Japan Times/Reuters 10 nov, Taipei Times 10/11 nov).
- APEC em Shenzhen, 18 e 19 nov, com Trump; terceiro encontro Trump-Xi do ano: confirmado (VOA 13 nov, ABC News).
- **FATO NOVO, ausente do post:** a Casa Branca (CNN, 13 nov) e o Kremlin (TASS e Anadolu, 14 nov) anunciaram para **quinta, 19 nov**, em Shenzhen, uma reunião bilateral Trump-Xi seguida do **primeiro encontro a três Trump-Xi-Putin**, focado em não proliferação nuclear (o Irã também deve entrar). A pauta, que mandava não usar a trilateral, ficou desatualizada. A frase do slide 7 "O formato exato ainda não tinha comunicado oficial" agora está **errada**.
- **Contexto que mudou:** Busan (out 2025) já não é o dado mais recente sobre Taiwan. Na cúpula de setembro de 2026, em Washington, o fact sheet da Casa Branca não citou Taiwan, mas o comunicado chinês diz que Xi pediu aos EUA que se oponham à "independência de Taiwan" (Focus Taiwan/CNA, 26 set 2026; CommonWealth, 29 set 2026). Usar só Busan passa uma ideia enganosa de que o tema não aparece nas conversas.

## Correções (texto pronto)

**C1. Capa** (fato e visual)
- `capa.titulo_html`: `<span class="hl">Mais de 100 navios</span> chineses em torno de Taiwan. Pequim não anunciou nada`
- Trocar a imagem da capa de `img01` (Fujian, original de 1852x515, ampliado cerca de 2,6x e borrado) para `img02` (Liaoning, Baycrest, 2400x1600, CC BY-SA 2.5, nítida). É o porta-aviões citado no post. Ajuste o `foco` para o navio aparecer acima do texto.
- Depois disso, regere o story (`scripts/story.py`) e o reel (capa e cena 01).

**C2. Slide 2** (foto borrada: Nanchang, 1489x454, ampliada). Troque por uma foto nítida, colorida e com pelo menos 1080 px na menor dimensão útil. Sugestão: `File:PLANS Liaoning (CV-16) 20221216 - 1.jpg` (Ministério da Defesa do Japão, CC BY 4.0, 900x1167, vertical), usada no slide 2 ou no 5 (o 5 fica sem foto se o Liaoning for para a capa). Para não repetir o Liaoning, outra saída é buscar um Type 055 ou um navio da Guarda Costeira com `incategory:"Type 055 destroyers"`. O texto do slide 2 continua o mesmo.

**C3. Slide 6** (mapa da Eurásia; Taiwan e a primeira cadeia de ilhas ficam sob o degradê e o texto cai sobre os rótulos do mapa). Mude o `foco` para `"95% 72%"` e renderize de novo. Se Taiwan e a linha "First Island Chain" ainda não aparecerem acima do texto, troque por um mapa recortado no Pacífico ocidental (por exemplo, a versão recortada desse mapa do DoD ou um mapa da primeira cadeia de ilhas em domínio público).

**C4. Slide 7** (fato desatualizado). `texto_html`, com 44 palavras:
`Nesta quarta, 18 nov, começa em <strong>Shenzhen</strong> a cúpula da APEC. Na quinta, segundo a Casa Branca e o Kremlin, Trump terá reunião com Xi Jinping, a terceira do ano, e depois um encontro inédito a três com Putin, focado em não proliferação nuclear.`

**C5. Slide 8** (contexto velho). `texto_html`, com 39 palavras:
`A pauta com Xi deve ter comércio e riscos da inteligência artificial; <strong>Taiwan não aparece</strong> entre os temas anunciados. Na cúpula de setembro, a Casa Branca não citou a ilha; Pequim disse que Xi pediu aos EUA que se oponham à independência taiwanesa.`
- Crédito cortado: em `imagens` → img08, troque `autor` por `中岑 范姜` (sem "from Taipei, Taiwan, Republic of China"). Assim aparecem "CC BY-SA 2.0" e a assinatura em uma linha só. Faça o mesmo na legenda, que é gerada a partir daí.

**C6. Legenda.** Troque a frase final do segundo parágrafo por:
`Nesta quarta, 18 nov, começa a cúpula da APEC em Shenzhen. Na quinta, Trump terá reunião com Xi e um encontro inédito a três com Putin, segundo a Casa Branca e o Kremlin; Taiwan não está entre os temas anunciados.` (substitui desde "Nesta quarta" até "pauta formal.")

**C7. Fontes** (`post.json → fontes`)
- Acrescentar: CNN, 13 nov (https://www.cnn.com/2026/11/13/politics/trump-putin-xi-meeting); TASS, 14 nov (https://tass.com/politics/2218203); Focus Taiwan, 26 set 2026 (https://focustaiwan.tw/politics/202609260010); CommonWealth, 29 set 2026 (https://english.cw.com.tw/article/article.action?id=5027); Japan Times, 10 nov (https://www.japantimes.co.jp/news/2026/11/10/asia-pacific/taiwan-china-area-denial-pacific/).
- Retirar: NPR, 29 out 2025 (Busan saiu do texto).

**C8. Reel**
- Capa e cena 01 seguem a nova capa (C1).
- Cena 06 (`imagem: img07`), com 17 palavras: `Na quinta, em Shenzhen, Trump se reúne com Xi e com <em>Putin</em>, dizem Casa Branca e Kremlin.`
- Cena 07 (`imagem: img08`): o "O mar ao redor da ilha, sim" é ambíguo e opinativo (dá a entender que o mar está na pauta). Substituir, com 14 palavras: `Taiwan não está entre os temas anunciados pela Casa Branca para o <em>encontro de quinta</em>.`
- Cena 04 (mapa): a primeira linha do texto cai sobre o mapa. Ainda dá para ler, mas, se trocar o mapa em C3, use o novo aqui também.

## Opcionais (não bloqueiam)
- Slide 3: "No pico, em 3 nov" junta duas informações. Wu informou a contagem em 3 nov, e a Reuters diz "em algum momento no início do mês". Texto mais seguro: `Em 3 nov, mais de <strong>100 navios</strong> da Marinha e da Guarda Costeira chinesas estavam na região, segundo o chefe do Conselho de Segurança Nacional de Taiwan, Joseph Wu, e um alto funcionário. É uma contagem de Taipé, sem verificação independente.`
- Crédito do Ministério da Defesa do Japão: a licença no Commons é a Government of Japan Standard Terms of Use 2.0 (`Gjstu-2.0`, compatível com CC BY 4.0, com revisão de licença feita). O "CC BY 4.0" está correto. Para o leitor, o autor poderia aparecer como "Ministério da Defesa do Japão".
- Slide 7: o recorte da foto de Shenzhen ficou suave, porque veio da miniatura de 1920 px de um panorama de 25408 px. Se der, baixe uma miniatura maior (por exemplo, 6000 px) para o recorte ficar nítido.
