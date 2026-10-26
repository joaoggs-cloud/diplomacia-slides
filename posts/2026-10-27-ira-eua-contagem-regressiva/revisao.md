REPROVADO

# Revisão — 2026-10-27-ira-eua-contagem-regressiva
Revisor, 26 out 2026. WebFetch e acesso direto (curl) seguem bloqueados nesta sessão; a checagem foi feita com WebSearch (modo extended) cruzando veículos diferentes.

| Item | Resultado |
|---|---|
| 1. Fatos | PROBLEMA: slide 7 e legenda (3 nov tratado como "bastidores"); slide 6 (data do comício) |
| 2. Isenção | PROBLEMA: falta a posição declarada do Irã |
| 3. Imagens: licenças e créditos | ok: todas PD, CC BY 2.0 ou CC BY-SA 4.0; créditos no slide e na legenda |
| 3. Imagens: adequação | PROBLEMA: slides 2, 6 e 8 cinzentos ou desfocados; 3 porta-aviões quase iguais (capa, 2 e 8) |
| 3. Foto NASA, slide 4 | ok: é o Estreito de Ormuz (catálogo NASA/JSC STS004-37-716, STS-4, jun-jul 1982, centro 26°N 56°E; aparecem Musandam e Qeshm) |
| 4. Texto | ok: ortografia e concordância; todos os slides com menos de 60 palavras. Ajustes abaixo |
| 5. Visual | ok: nada cortado, numeração 1/9 a 9/9 certa, texto legível, logo sem sobreposição |
| 6. Legenda | ok: 1.064 caracteres no total. Ajustes de conteúdo abaixo |

## Checagens refeitas
- Memorando Clayton→Rubio de 23 out com planos em "advanced stages": confirmado (Axios, NBC, AP/PBS, Al Jazeera). OK.
- Redução de pessoal em Jordânia, Líbano, Catar e Emirados, com as sedes abertas, o argumento dos houthis e a negativa de ligação com ataques: confirmado (AP/PBS, U.S. News, CNN, Naharnet). OK.
- Cessar-fogo de 7 abr e MoU de jun que expirou em ago: confirmado pelo CRS (IN12678 e R48887). OK.
- Fox News em 25 out ("deal or finish them off", sem ataque "hoje"): confirmado (CBS, L'Orient Today). OK.
- Frase "another little Epic Fury": confirmada, mas dita em **23 out**, num comício em Fort Myers, Flórida (France 24, URL 20261023; Times of Israel; Epoch Times). Não foi no fim de semana de 25 out.
- 3 nov: **não é leitura de bastidores.** Em 8 out, Trump declarou publicamente (Truth Social) que os EUA não retomariam ataques ao Irã antes das eleições de 3 nov (Washington Post/AP de 8 out; Al Jazeera de 9 out). A atribuição "reportagens citadas pela Al Jazeera" e a frase "não declaração oficial" estão erradas.
- Irã: segundo a Al Jazeera (24 out), Teerã não respondeu ao memorando. Em 25 out, o porta-voz da chancelaria, Esmaeil Baghaei, disse que Teerã não fechou a janela da diplomacia e que mensagens chegam aos EUA por intermediários. Também rejeitou a "rendição completa" exigida por Washington. Fontes: AP (via ABC News, CP24 e Business Standard) e CBS News.

## Correções exatas

### C1. Slide 7 (fato errado, obrigatória)
`texto_html` →
`Em 8 out, Trump afirmou que os EUA não retomariam ataques ao Irã antes das <strong>eleições legislativas de 3 de novembro</strong>. Segundo a Al Jazeera, o Pentágono mantém planos prontos, o que <em>não equivale a ordem de ataque</em>.`
Mantenha o factbox ("Nenhuma fonte confirma que haverá ou não ação militar depois dessa data.").
Inclua em `fontes`:
- `{"nome": "Washington Post (8 out)", "url": "https://www.washingtonpost.com/politics/2026/10/08/trump-iran-war-midterms-attack/cb8aa31a-c335-11f1-8170-681419af1cc9_story.html"}`
- `{"nome": "Al Jazeera (midterms)", "url": "https://www.aljazeera.com/news/2026/10/9/is-trump-signalling-a-return-to-war-with-iran-after-the-midterms"}`

### C2. Slide 6 (data errada, obrigatória)
- `tag` → `23 e 25 out 2026`
- `texto_html` →
`Em comício na Flórida, em 23 out, Trump disse: <em>“We may do another little Epic Fury, or they'll agree”</em> (podemos fazer outra “pequena” Epic Fury, ou eles aceitam). À Fox News, no dia 25, disse escolher entre um acordo e “acabar com eles”, e que não haveria ataque naquele dia.`
- Inclua em `fontes`: `{"nome": "France 24", "url": "https://www.france24.com/en/americas/20261023-trump-says-us-may-launch-another-little-epic-fury-attack-iran"}` e `{"nome": "CBS News", "url": "https://www.cbsnews.com/live-updates/iran-war-trump-us-oil-gas-prices-strait-of-hormuz-midterms/"}`

### C3. Isenção: posição do Irã (obrigatória)
Crie um slide novo **entre o atual 6 (Trump) e o atual 7 (calendário)**. O carrossel passa a ter 10 slides, ainda dentro do limite.
```json
{
  "imagem": "img09",
  "tag": "25 out 2026",
  "titulo": "O que diz Teerã",
  "texto_html": "O porta-voz da chancelaria iraniana, <strong>Esmaeil Baghaei</strong>, disse em 25 out que Teerã não fechou a porta à diplomacia e que mensagens chegam aos EUA por intermediários.",
  "factbox": {"label": "Memorando", "texto": "Segundo a Al Jazeera, até 24 out o Irã não havia comentado o documento."}
}
```
O texto principal tem 28 palavras. Imagem `img09`: `"query": "File:Tehran Milad Tower.jpg"` (Morteza Jrk, CC BY-SA 4.0, 5184×3456, colorida). Alternativa: `File:Tehran skyline- Alborz Mountains on background-20150401.jpg` (confira a licença).
Inclua em `fontes`: `{"nome": "AP via ABC News", "url": "https://abcnews.com/Politics/wireStory/iran-messages-passed-us-amid-war-concerns-mideast-137558362"}` e `{"nome": "Business Standard", "url": "https://www.business-standard.com/world-news/messages-are-still-being-passed-to-us-amid-war-concerns-says-iran-126102600052_1.html"}`

### C4. Slide 8, resumo (consequência de C1 e C3)
`texto_html` →
`<strong>Fato:</strong> memorando existe, segundo a imprensa; embaixadas reduziram equipe; Trump prometeu não atacar antes de 3 nov e fala em acordo ou nova ação; Irã diz manter canal indireto.<br><br><em>Não confirmado:</em> planos iranianos e o que acontece depois de 3 nov.`
(44 palavras)

### C5. Legenda (obrigatória)
Troque o trecho `Os EUA reduziram equipes em embaixadas da região e Trump falou em "acordo ou nova ação". Reportagens apontam as eleições de 3 nov como possível marco, mas isso é leitura de bastidores.` por:
`Os EUA reduziram equipes em embaixadas da região. Trump, que prometeu não atacar antes das eleições de 3 nov, diz escolher entre acordo e nova ação. O Irã diz que a diplomacia segue aberta, por intermediários.`
Troque também `Atualizado em 27 out 2026.` por `Atualizado em 26 out 2026.`, a data real da apuração.

### C6. Fotos fracas (recomendada; confira cor e enquadramento ao baixar)
Todas são do governo dos EUA (domínio público) e foram achadas no Commons:
- Slide 2 (Epic Fury, contexto) → `File:U S Forces Launch Operation Epic Fury (9542614).jpg` (decolagem de F/A-18E do USS Abraham Lincoln, 28 fev 2026). Combina com o texto e não mostra vítimas. Reserva: `File:U S Forces Launch Operation Epic Fury (9542618).jpg`
- Slide 6 (acordo ou nova ação) → `File:Boeing FA-18F Super Hornet of VFA-103 lands aboard USS Abraham Lincoln (CVN-72) on 24 October 2019 (191024-N-MM912-1015).JPG` (Mar Arábico). Reserva: `File:North Façade White House.JPG` (PD, decisão da Casa Branca, sem rosto de político)
- Slide 8 (resumo) → `File:US Navy 101205-N-2937R-205 The aircraft carrier USS Abraham Lincoln (CVN 72) transits the Arabian Sea while conducting flight operations.jpg`. Se ela também vier cinza, use `File:171022-N-VR594-0093 (38245775971).jpg` (USS Princeton em Ormuz, 2017).
Motivo: hoje a capa, o slide 2 e o slide 8 mostram porta-aviões no mesmo céu cinza. O slide 6 é um cockpit desfocado sem assunto definido. Isso contraria a regra de "fotos coloridas, claras e nítidas".

### Observações (não bloqueiam)
- Slide 4: a foto é de 1982 e não deve ser legendada como atual. Hoje não está, então ok.
- Pauta, fato 4 (Arábia Saudita em ordered departure, 21 out): confirmado por Times of Israel e Reuters/ThePrint, mas não entrou no post. Ok omitir.
- Depois das correções, renderize de novo e confira se o slide 6, com o título em duas linhas, não passa de 60 palavras (o novo texto tem cerca de 50).
