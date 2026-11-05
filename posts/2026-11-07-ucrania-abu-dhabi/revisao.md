REPROVADO

Revisão de posts/2026-11-07-ucrania-abu-dhabi (SHA 9b86a9e), 5 nov 2026.

| Item | Resultado |
|---|---|
| Fatos: Kremlin confirma Abu Dhabi 10-11 nov (3 nov) | ok (Reuters/ThePrint, Ukrainska Pravda, Xinhua 4 nov). Nenhum adiamento encontrado até 5 nov |
| Fatos: Medinski chefe da delegação, segundo Peskov | ok (Reuters, NV.ua, Kyiv Post) |
| Fatos: agenda citada por Witkoff | ok (Fox, Axios, Moscow Times) |
| Fatos: histórico das rodadas (slide 5) | PROBLEMA: omite a 3ª rodada, em Genebra, 17-18 fev 2026 |
| Fatos: fala de Zelensky (slide 6 e legenda) | PROBLEMA: sem data e sem fonte de novembro; "diz" no presente sugere reação à rodada de 10-11 nov |
| Isenção visual | PROBLEMA: 2 fotos de Putin com Witkoff (slides 5 e 6), nenhuma do lado ucraniano |
| Licenças e créditos | ok (CC BY-SA 3.0/4.0, CC BY 4.0, domínio público). Crédito do slide 6 sai cortado ("President of R..."), o que se resolve com a troca abaixo |
| Texto (45 palavras, sem emoji, sem perguntas, 1 título + CTA, 1 factbox) | ok |
| Visual (8 JPEGs, numeração 2/8 a 8/8, legibilidade, cor) | ok |
| Legenda (1.192 caracteres; payload --rascunho rc=0) | ok, mas precisa da correção do Zelensky |

## Correções exatas

1. Slide 5 (`slides[3].texto_html`): substituir por
   `Houve três rodadas trilaterais antes: em Abu Dhabi, em <strong>23 e 24 jan</strong> e em <strong>4 e 5 fev</strong>, e em Genebra, em <strong>17 e 18 fev</strong>. Depois, EUA e Israel iniciaram a guerra contra o Irã e as conversas sobre a Ucrânia pararam.`
   Remover o `factbox` (repete a capa e estoura o limite de palavras). Se quiser mantê-lo, use:
   `Última rodada mediada pelos EUA: Genebra, 17 e 18 fev 2026.`
   Acrescentar em `fontes`:
   - Euromaidan Press, 17 fev: https://euromaidanpress.com/2026/02/17/third-round-of-ukraine-russia-us-talks-opens-in-geneva/
   - Arab News (Kremlin anuncia Genebra 17-18 fev): https://www.arabnews.pk/node/2632885

2. Slide 6 (`slides[4].texto_html`): substituir por
   `Em 21 out, após reunião com Witkoff, Putin aceitou <em>“em princípio”</em> retomar o formato trilateral, segundo o assessor do Kremlin <strong>Iuri Ushakov</strong>. Em 28 out, <strong>Zelensky</strong> disse que Kiev está pronta para negociar e que parceiros veem sinais de que Moscou leva a reunião a sério.`
   Fontes: Ukrainska Pravda, 28 out (https://www.pravda.com.ua/eng/news/2026/10/28/8060037/) e Hvylya (https://en.hvylya.net/news/369-zelensky-confirms-trilateral-talks-in-abu-dhabi-as-kremlin-issues-donbas-ultimatum). Confira a frase nas duas páginas antes de publicar. Se não confirmar, mantenha o texto atual com data e fonte: "Em 21 out, Zelensky disse que…" (News24).
   Legenda: trocar "Zelensky afirma que Kiev precisa participar de qualquer decisão sobre o futuro da Ucrânia." por "Zelensky disse em 28 out que Kiev está pronta para negociar."

3. Isenção visual: trocar a imagem do slide 6 (img06, Putin e Witkoff numa biblioteca em maio de 2025, que além disso pode ser lida como foto de 21 out) por uma foto do lado ucraniano. Depois disso, Witkoff (slide 4), Putin com Witkoff (slide 5) e Zelensky (slide 6) ficam com um slide cada. Em `busca_imagens` img06:
   - query: `File:President introduces new Minister of Defense of Ukraine Rustem Umerov (7 September 2023) 02.jpg` (CC BY 4.0, Ministério da Defesa da Ucrânia, segundo o Commons)
   - alternativas: `File:Volodymyr Zelensky, President of Ukraine, and Ursula von der Leyen, President of the European Commission - 2025.jpg`, `File:Volodymyr Zelensky Official portrait.jpg`, `File:Flag of Ukraine.svg`
   Rode `scripts/imagens.py posts/2026-11-07-ucrania-abu-dhabi --so img06`, que filtra a licença. Não legende como delegação de novembro: a composição ucraniana não está confirmada. Se só vier foto com Umerov sem Zelensky, prefira a alternativa com Zelensky. Observação: não consegui abrir as páginas do Commons nesta sessão (o host está bloqueado), então as licenças vêm dos snippets de busca e o imagens.py deve confirmar.

Depois: renderizar de novo e revisar os slides 5 e 6 (crédito inteiro, rosto acima do degradê).

Observações menores, que não reprovam: a foto do Witkoff no slide 4 é de 2018 (domínio público), embora a busca pedisse a de 2025. Ela é aceitável. Nas rodadas de jan e fev em Abu Dhabi, a delegação russa foi chefiada por Igor Kostiukov, e o texto atual não diz o contrário.
