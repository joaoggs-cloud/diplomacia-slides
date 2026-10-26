REPROVADO

# Revisão, rodada 2: 2026-10-27-bomba-tsar-65-anos (slides SHA f2fc319)

Obs.: o proxy desta sessão bloqueia commons.wikimedia.org (403 / ENOTFOUND). Licenças conferidas pelos metadados gravados em `post.json` e `imagens/candidatos/*.json` e por buscas restritas ao domínio.

| Item | Resultado |
|---|---|
| 1. Fatos | ok. Correções da rodada 1 aplicadas (11h32 horário de Moscou, tratado com atmosfera/espaço/debaixo d'água, Sakharov) |
| 2. Isenção | ok (histórico, sem adjetivos, sem glorificar) |
| 3. Imagens | PROBLEMA: slide 2 é retrato da agência TASS; slide 7 (Belushya Guba) não combina com o texto e pode induzir a erro |
| 4. Texto | ok. 32 a 44 palavras por slide, sem título nem tag, sem factbox, sem emoji, texto corrido |
| 5. Visual | ok. Numeração 1/10 a 10/10, nada cortado, texto legível, créditos em todos os slides com foto, CTA ok |
| 6. Legenda | ok. Sem emoji, pergunta no fim; `metricool.py payload --sha f2fc319 --rascunho` passou (rc=0) |

## Rodada 1: o que foi aplicado
- 1 (capa AP): ok, a capa agora é MODIS/NASA de Novaya Zemlya (domínio público, colorida). A bola de fogo da AP saiu do post.
- 2 (invólucro repetido): ok. O invólucro aparece só no slide 4, e o texto avisa: "Na foto, peça do mesmo tipo, exposta no museu nuclear de Sarov."
- 3 (slide 8, foto de outro evento): ok com desvio aceitável. Selo soviético de 1963 sobre o tratado (CPA 2943; selo é ato oficial, domínio público), coerente com o texto, que é o exato pedido.
- 4 (horário): ok, "11h32 (horário de Moscou)". Conferido de novo: NWA dá 11h32 (Moscou); outra fonte dá 11h33. "Por volta das" cobre a diferença.
- 5 a 8 (recomendadas): todas aplicadas. A cor no slide 2 não foi aplicada, por causa do problema abaixo.

## Fatos conferidos de novo nesta rodada
- 30 out 1961, sobre o cabo Sukhoy Nos (ilha Severny, zona C), Tu-95V, paraquedas, detonação a 4.000 m, 11h32 (Moscou): NWA + Wikipedia/Durnovtsev. ok
- 50 Mt (valor russo desde 1991; estimativa dos EUA 57 Mt) e projeto de 100 Mt: NWA + National Interest. ok
- Sakharov já questionava os testes em 1961: AIP (exposição Sakharov) + Britannica ("in 1961 he opposed Khrushchev's plan to test a 100-megaton bomb"). ok
- Slide 2, "na retomada dos testes": a URSS rompeu a moratória de 1958 em set 1961 (AIP). ok
- Slide 7: 60 km / 8,85 km = 6,8, então "perto de sete Everests" está ok. A frase das três voltas está atribuída à AHF. ok

## Correções obrigatórias

1. **Slide 2 (img10): foto de agência.** O arquivo `Nikita Khrushchev TASS Portrait Trim.jpg` tem autor "G. Weil for TASS". É um retrato oficial da TASS de 1954, retocado e distribuído como foto de imprensa. O domínio público dele se apoia na mesma base que reprovamos na rodada 1 para a AP (foto de imprensa publicada nos EUA sem aviso de copyright). Na Rússia não é domínio público, porque é posterior a 1943. A regra do CLAUDE.md é nunca usar foto de agência. Os candidatos `img02_op2/op3` também são TASS.
   - Troque por `File:John Kennedy, Nikita Khrushchev 1961.jpg`: Viena, 3 jun 1961, fotógrafo do Departamento de Estado dos EUA, JFK Library PX 96-33:12, domínio público como obra do governo federal (17 U.S.C. 105). Combina com o slide, porque foi um mês antes da encomenda da bomba.
   - Alternativa: `File:1961 John F. Kennedy, Nikita Khrushchev, Jacqueline Kennedy.jpg` (USIA, 3 jun 1961, domínio público).
   - Se `Nikita Khruchchev Colour.jpg` tiver licença livre que não seja de agência, também serve. Mas o `imagens.py` caiu no fallback TASS, então confira a página antes.
   - Na `busca_imagens`, mude `img10.query` para `"File:John Kennedy, Nikita Khrushchev 1961.jpg"` e tire os dois "TASS" das `alternativas`. Texto do slide sem mudança.

2. **Slide 7 (img15): foto que não combina e pode enganar.** O arquivo `Belushya guba novaya zemlya russia nasa photo.jpg` é uma obra derivada com dois círculos marcando o aeródromo de Rogachevo e a vila de Belushya Guba. Os dois ficam na ilha **sul** (Yuzhny), a uns 400 km do ponto do teste (Sukhoy Nos, ilha norte). Ao lado de um texto sobre o clarão e a onda de choque, o leitor vai entender que os círculos marcam a explosão ou o alvo. A imagem também está pixelada.
   - Troque por `File:Comparative nuclear fireball sizes.svg` (Fastfission, domínio público). Mostra a escala da Tsar Bomba e conversa com "sete Everests". Use a miniatura PNG do Commons se o `imagens.py` não aceitar SVG.
   - Alternativa sem marcações: `File:Roze Glacier, Novaya Zemlya.jpg` (NASA EO-1, ilha Severny, domínio público, colorida).
   - Texto do slide sem mudança.

## Recomendações (não bloqueiam)
- Capa e slide 6 usam a mesma base MODIS (o mapa do slide 6 é desenhado sobre ela). Dá para aceitar porque o mapa acrescenta informação. A troca do slide 7 acima evita uma terceira imagem de satélite.
- Slide 6: o mapa tem rótulos em inglês, e um "...ERN" da ilha sul fica cortado sob o texto. O ponto que importa ("Sukhoy Nos / C") está visível acima do degradê. ok
- Slide 5: a foto é de um Tu-95 atual (RF-94130), não do Tu-95V de 1961. O texto diz só "Um Tu-95 modificado", então não engana. ok
- Slides 3 e 9 em P&B: históricos e justificados. Slide 2 fica em P&B se usar a foto de Viena; também justificado.

## Sem problemas
Estilo novo respeitado (texto corrido, nenhum título ou tag nos slides de conteúdo, capa sem etiqueta de nº de fontes), legenda e primeiro comentário sem emoji, pergunta neutra, créditos presentes (CC BY-SA com autor nos slides 4 e 5), slide 10 (CTA) ok, payload ok.
