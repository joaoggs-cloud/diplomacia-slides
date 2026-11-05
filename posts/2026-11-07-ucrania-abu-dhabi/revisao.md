REPROVADO

Revisão rodada 2 (última) de posts/2026-11-07-ucrania-abu-dhabi (SHA f06bbd2), 5 nov 2026.
Só um problema: a fala de Zelensky no slide 6 e na legenda. A troca abaixo resolve e não exige nova revisão de conteúdo, só conferir o slide 6 renderizado de novo.

| Item | Resultado |
|---|---|
| Correção 1 da rodada 1 (slide 5 com as três rodadas, Genebra 17-18 fev, fontes) | ok, aplicada |
| Correção 2 da rodada 1 (fala de Zelensky com data e fonte) | PROBLEMA: o texto novo não se confirma (ver abaixo) |
| Correção 3 da rodada 1 (foto do lado ucraniano no slide 6) | ok: Zelensky com von der Leyen, CC BY 4.0, crédito "Dati Bendo / União Europeia" inteiro no slide |
| Fatos: Kremlin 3 nov, Medinski, pauta de Witkoff, Ushakov 21 out | ok (verificados na rodada 1) |
| Fatos: "Em 28 out, Zelensky disse esperar a nova rodada para meados de novembro, à espera da confirmação de Washington" | PROBLEMA: não encontrei em nenhuma fonte. Pravda.com.ua e Hvylya estão bloqueados nesta sessão. Nas buscas: em 23 out ele falou em "primeira quinzena de novembro" (Ukrainska Pravda, Liga), não em "meados". Em 25 out disse que os três países tinham acertado a reunião trilateral em novembro (Euronews, AFP via NZ Herald, TRT World). "À espera da confirmação americana" foi dito pelo negociador Arakhamia, não por Zelensky (Liga) |
| Isenção visual | ok: Kremlin (3), Witkoff (4), Putin com Witkoff (5), Zelensky (6) |
| Licenças e créditos | ok em todos os slides, nenhum cortado |
| Texto: palavras por slide (32/25/25/41+factbox/37/43), 1 título + CTA, 1 factbox, sem emoji, sem perguntas | ok |
| Visual: 8 JPEGs, numeração 2/8 a 8/8, cor, rostos acima do degradê, legível | ok |
| Legenda (604 caracteres; payload --rascunho rc=0) | ok, mas precisa da mesma correção do Zelensky |

## Correções exatas

1. Slide 6 (`slides[4].texto_html`): substituir por
   `Em 21 out, Putin aceitou <em>“em princípio”</em> retomar o formato trilateral, segundo o assessor do Kremlin <strong>Iuri Ushakov</strong>. Em 25 out, <strong>Zelensky</strong> disse que os três países tinham acertado uma reunião trilateral em novembro.`
   (33 palavras)

2. Legenda: trocar "Em 28 out, Zelensky disse esperar a rodada para meados de novembro." por
   "Em 25 out, Zelensky disse que os três países tinham acertado uma reunião em novembro."

3. `fontes`: remover "Ukrainska Pravda (28 out)" e "Hvylya", porque não confirmam o texto. Acrescentar:
   - Euronews, 25 out: https://www.euronews.com/2026/10/25/ukraines-zelenskyy-confirms-trilateral-talks-with-russia-and-us-to-take-place-in-november
   - TRT World: https://www.trtworld.com/article/0951f8ea6290
   - NZ Herald (AFP): https://www.nzherald.co.nz/world/zelenskyy-says-trilateral-us-ukraine-russia-meeting-to-take-place-in-november/WOAAPNDFXNDJVNZJRKDJPNGBZY/

Depois: renderizar e conferir o slide 6 (texto dentro da área, crédito inteiro). Nenhum outro item precisa mudar.
