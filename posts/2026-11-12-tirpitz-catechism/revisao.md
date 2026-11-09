APROVADO (coordenador, 9 nov 2026, rodada 2): as 4 correções obrigatórias foram aplicadas no SHA 00a544c806f6397ac3dce5e70306321dd6211b38, junto com as recomendações dos slides 2 e 7.
- Slide 8 com o texto novo.
- Legenda cita a Tallboy e os Lancasters modificados.
- Slide 6 com os tanques extras.
- Capa usa a img07 com o título em 3 linhas, e a img01 foi para o slide 7.
Conferi a capa e os slides 7 e 8 em JPEG, e o story foi regerado.

--- Rodada 1 ---

REPROVADO

Revisão do SHA 7bbfeadcd9e66fe8ada01eca8c2ef0c20b96fec3 (09 nov 2026). Fatos reconferidos por WebSearch fora da Wikipedia: RAF Museum (Target the Tirpitz), Memorial Flight Club, Inside Story, Maritime Quest, aviamuseum, nordnorge.com.

| Item | Resultado |
|---|---|
| Fatos: 12 nov 1944, esq. 9 e 617, Lossiemouth/Milltown (Escócia), "cerca de 30" (29–32), Tallboy 12.000 lb | ok |
| Fatos: Paravane 15 set, 1 Tallboy, dano na proa, sem condições de combate | ok |
| Fatos: Tromsø/Håkøya como bateria flutuante, Obviate 29 out falhou (nuvens) | ok |
| Fatos: 2–3 acertos, emborcou em minutos (~09:41–09:52) | ok |
| Fatos: 950–1.204 mortos; ~1.000 de ~1.700 | ok (atribuídos) |
| Fatos: "cerca de 200 sobreviveram" (slide 8) | PROBLEMA 1 |
| Legenda: "Só a bomba Tallboy mudou esse cálculo" | PROBLEMA 2 |
| Coerência slide 2 ("longe demais do Reino Unido") x slide 6 ("saiu da Escócia") | PROBLEMA 3 |
| Desmonte do casco e brasão em Lofoten | ok (lokalhistoriewiki + ficha do Commons; desmonte 1948–1957) |
| Isenção / tom (sem glorificar mortes) | ok |
| Licenças e créditos (IWM/AWM/RAF domínio público; CC BY 2.0 e CC BY-SA 4.0 creditados no slide e na legenda; nada de agência) | ok |
| Texto (≤ 45 palavras, 0 títulos, 1 factbox, sem emoji/pergunta) | ok, com ajuste de redação no slide 8 |
| Capa: assunto da foto (casco emborcado) fica atrás das etiquetas e do título; topo mostra só neve | PROBLEMA 4 |
| Slide 8: vista atual e ensolarada de Tromsø sob o número de mortos, sem ligação no texto | PROBLEMA 5 |
| Slides 2–7 e 9–10: refletem as fotos trocadas, legíveis, créditos inteiros, numeração 2/10…10/10 certa | ok |
| Story: reproduz a capa (herda o problema 4) | PROBLEMA 4 |
| Legenda: 1.094 caracteres | ok |
| Reel | não há (quinta) |

## Correções obrigatórias

1. **Slide 8, sobreviventes.** "Cerca de 200 sobreviveram" contradiz o próprio slide (≈1.700 a bordo e ≈1.000 mortos dão ≈700 sobreviventes; a Wikipedia fala em centenas resgatados da água). Cortar a frase. Novo `texto_html` do slide 8 (que já resolve o problema 5):
   `Hoje, Tromsø vive em frente ao lugar onde o navio virou, perto da ilha de Håkøya. O saldo humano segue incerto: as estimativas vão de <em>950 a 1.204 mortos</em>, e outra fonte fala em cerca de mil dos cerca de 1.700 homens a bordo.`

2. **Legenda.** Trocar "Só a bomba Tallboy, de cerca de 5,4 toneladas, mudou esse cálculo." por:
   "A bomba Tallboy, de cerca de 5,4 toneladas, e Lancasters modificados para voar mais longe mudaram esse cálculo."
   (A Tallboy resolveu a blindagem, não o alcance.)

3. **Slide 6.** Trocar "saiu da Escócia: cerca de 30 Lancasters dos esquadrões nº 9 e nº 617 da RAF, armados com Tallboys." por:
   "saiu da Escócia: cerca de 30 Lancasters dos esquadrões nº 9 e nº 617 da RAF, com tanques extras de combustível e armados com Tallboys."

4. **Capa e story.** Na `img01` o casco é uma faixa fina em y≈660–780, coberta pelas etiquetas e pelo título; o render não tem zoom, então `foco` não resolve. Fazer:
   - `capa.imagem` = `"img07"` (casco emborcado em close, CL2830) e `slides[5].imagem` (slide 7) = `"img01"`;
   - encurtar o título para caber em 3 linhas: `Afundado <span class="hl">parado</span>, por bombas de <span class="hl2">5,4 toneladas</span>`;
   - renderizar, conferir que o topo do casco e o hélice ficam visíveis acima das etiquetas e que no slide 7 o casco da img01 aparece acima do texto; rodar `scripts/story.py` de novo e conferir `story/story.jpg`.

5. **Slide 8, foto.** A foto fica (CC BY 2.0, crédito certo), desde que entre o texto da correção 1, que diz o que a imagem mostra.

## Recomendado (não bloqueia)
- Slide 2: a foto é de Fættenfjord, perto de Trondheim, em 1942, e o navio quase não aparece. Trocar "Atracado em fiordes do norte da Noruega" por "Escondido em fiordes da Noruega".
- Slide 7: "Conforme a fonte, foram dois a três acertos diretos." → "As fontes contam dois ou três acertos diretos."
- Slide 5: a img05 tem 638×478 px e sai granulada, mas legível.
- Slide 6: a tripulação da CH17863 não está identificada; o texto não atribui nada a ela, então ok.
