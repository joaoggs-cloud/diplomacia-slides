REPROVADO

# Revisão: 2026-11-22-shenzhen-resultado-declaracao (19 nov 2026, noite)

O post está bem montado: tudo vem atribuído, não há emoji nem pergunta ao leitor e a legenda tem 1.307 caracteres. Mas há **4 erros de fato** (duração da reunião, Peskov fora de contexto, "inovador" atribuído a Xi, nome e publicação da declaração), redação imprecisa no ponto do TPI e na fala de Putin, e 2 fotos a trocar.

## Tabela

| Item | Situação |
|---|---|
| 1. Citação "não pode ser vencida e nunca deve ser travada" + diálogo sobre riscos nucleares e não proliferação | ok (Xinhua, Casa Branca, The National, Bernama) |
| 1b. Quem publicou a declaração e com que nome (slide 2) | **problema** |
| 2. Reuters: nenhuma negociação de controle de armas anunciada | ok |
| 2b. New START (5 fev 2026) / China recusa negociar a três | **problema** (o tempo verbal: a recusa é anterior à cúpula, e a declaração agora prevê "diálogo" a três) |
| 3. ONU / derivados de petróleo / TPI | **problema** (TPI: o texto fala em "jurisdição" e em imunidade de autoridades de Estado, não em "poderes"; o factbox fica desnecessário) |
| 4. Ucrânia: 40 min e Peskov | **problema** (os ~40 min foram a conversa a dois Putin-Trump, em que, segundo Ushakov, a Ucrânia foi o tema principal; o "não foi o tema central" de Peskov se refere à reunião a três; o slide mistura as duas) |
| 5. Putin, Ponte da Crimeia | **problema** (ele recusou negociar um *cessar-fogo limitado* e conversas diretas; "não fará acordos" entre aspas não é a fala dele) |
| 6. Trump sobre Xi e Irã/Ormuz | ok, com ajuste recomendado (Xi não comentou em público a versão de Trump) |
| 7. Reações | **problema**: "inovador" (groundbreaking) foi como a chancelaria chinesa chamou a cúpula *antes* de ela acontecer (16 nov); depois, a Xinhua relata que Xi chamou as conversas de "positivas, construtivas e frutíferas". Hurst (ok: Guardian/Yahoo), Macron (ok: Korea Times/France 24), CBS (ok) |
| 8. Duração "pouco mais de uma hora" | **problema**: NPR e Globe and Mail dão cerca de 90 min. Data 19 nov (ok). "Primeira reunião trilateral" (ok: WaPo, CNN, Al Jazeera) |
| 9a. Licenças e créditos | ok (CC BY-SA, CC BY, PD, CC0; créditos no slide e na legenda) |
| 9b. Slide 4 Obama/Medvedev | ok **se** o texto disser quem assinou e quando (senão o leitor não entende a foto) |
| 9c. Slide 5 (skyline de Shenzhen) | **problema**: imagem pixelada (recorte de um panorama baixado a 1920 px), quase só céu, e é a 4ª foto genérica de Shenzhen |
| 9d. Slide 6 (Kostiantynivka à noite) | **problema**: escura, de 2024, não tem a ver com o texto (fala do Kremlin) e, num slide sobre a versão russa, dá uma leitura editorial de um lado só. Trocar |
| 9e. Isenção entre os três líderes | ok, depois das correções (Trump e Putin têm uma alegação cada, ambas ressalvadas; Xi aparece pela avaliação oficial) |
| 10. Texto: palavras por slide | ok (35–45), mas a capa tem 23 palavras em fonte grande e cobre a torre: encurtar. "divulgaram que" soa mal |
| 10b. Sem emoji / sem pergunta / 1 factbox / hashtags 7+4 base | ok |
| 10c. Legenda | **problema**: duração errada; a frase "Quem comentou os resultados, de Xi a analistas, é atribuído em cada slide" é metalinguagem com cara de IA; a lista de fontes precisa incluir os textos oficiais |
| 11. Visual (números de slide, cortes, legibilidade, cores) | ok, menos os slides 5 e 6 (fotos) |
| Story | ok (vai regenerar com a capa nova) |

## Correções exatas

**Capa (`capa.titulo_html`)**
`<span class="hl">Trump, Xi e Putin</span> declararam que uma guerra nuclear "nunca deve ser travada". O texto não fixa limites, prazos nem verificação`
(gancho continua igual)

**Slide 2**
`Em 19 nov, à margem da APEC em Shenzhen, Trump, Xi e Putin fizeram sua primeira reunião a três, de cerca de 1h30. Xinhua, Kremlin e Casa Branca publicaram a mesma <strong>declaração conjunta</strong>, de quatro pontos, chamada "Declaração rumo à Paz".`
(40 palavras. Nome oficial: "U.S.-Russia-China Heads of State Declaration toward Peace" na Casa Branca e "China-Russia-U.S. Heads of State Declaration toward Peace" na Xinhua; não é um nome só da Casa Branca)

**Slide 3**: manter.

**Slide 4** (mantém a foto img04)
`Mas, segundo a Reuters, a declaração não anunciou as negociações de controle de armas que Trump vinha buscando. O New START, assinado em 2010 por Obama e Medvedev, expirou em 5 fev 2026, e até a véspera da cúpula a China recusava negociar a três.`
(44 palavras)

**Slide 5**: tirar o `factbox` e usar
`O texto também promete reformar a ONU e ampliar a produção e a oferta de derivados de petróleo. E defende a imunidade de autoridades de Estado: o Tribunal Penal Internacional e "órgãos similares" não devem abusar de sua jurisdição.`
(39 palavras). Foto: trocar img05 pelo prédio do TPI, ex.: `"query": "File:International Criminal Court Headquarters, Netherlands.jpg"`, com as alternativas `File:Building of the International Criminal Court in The Hague.jpg` e `File:Netherlands, The Hague, International Criminal Court.JPG` (confirmar a licença pelo imagens.py; evitar o arquivo do Tony Webster, que tem licença inconsistente).

**Slide 6**
`A declaração não cita a Ucrânia. Putin e Trump trataram da guerra numa conversa a dois de cerca de 40 minutos, sem resultado anunciado, segundo o Kremlin. Na reunião a três, disse o porta-voz Dmitri Peskov, a Ucrânia não foi o "tema central".`
(43 palavras). Foto: trocar img06 (Kostiantynivka) por uma neutra do Kremlin, ex.: `"query": "File:Moscow - August 2025 - Kremlin Wall, Senate Palace, Senate Tower1.jpg"`, alternativa `File:7322. Moscow Kremlin. Senate Building.jpg` (categoria `incategory:"Kremlin Senate"`), colorida e de dia.

**Slide 7**
`Em entrevista coletiva em Shenzhen, após a cúpula, Putin disse que, depois dos ataques à Ponte da Crimeia, a Rússia não vai negociar um cessar-fogo limitado, e descartou conversas diretas com a Ucrânia. É a posição do presidente russo, não um ponto da declaração.`
(43 palavras; sem aspas, porque não é citação literal. Fontes: Meduza, CBS, Anews)

**Slide 8**
`Trump disse que ele e Xi concordam que o Irã deve reabrir totalmente o <strong>Estreito de Ormuz</strong> e não pode ter arma nuclear. Xi não comentou essa versão em público, e a declaração conjunta não menciona o Irã.`
(37 palavras)

**Slide 9**
`Segundo a Xinhua, Xi classificou as conversas como positivas, construtivas e frutíferas. CBS e CNN relatam que nenhum avanço diplomático foi anunciado, e William Hurst, professor de Cambridge, disse que "muito pouco de substância" foi alcançado. Para Macron, o texto "não leva a uma reorganização do mundo".`
(44 palavras; sai o "inovador")

**Legenda**: trocar o 2º parágrafo por
`A reunião trilateral de Shenzhen, em 19 nov, durou cerca de uma hora e meia. O texto, publicado pela Xinhua, pelo Kremlin e pela Casa Branca, promete diálogo sobre redução de riscos nucleares, mas não fixa limites, prazos nem verificação, e a Reuters diz que ele não anunciou as negociações de controle de armas que Trump buscava. A Ucrânia ficou de fora do documento. Segundo o Kremlin, Putin e Trump trataram da guerra numa conversa a dois de cerca de 40 minutos, sem resultado anunciado.`
(sai a frase "Quem comentou os resultados...")

**Fontes (`fontes`)**: acrescentar
- Xinhua (texto integral): https://english.news.cn/20261119/c15631ea3f054a278e3a3f592021f0da/c.html
- Casa Branca (texto integral): https://www.whitehouse.gov/briefings-statements/2026/11/u-s-russia-china-heads-of-state-declaration-toward-peace/
- The National (texto integral): https://www.thenationalnews.com/news/mena/2026/11/19/nuclear-war-cannot-be-won-full-text-of-china-russia-and-us-peace-declaration/
- NPR (duração): https://www.npr.org/2026/11/18/nx-s1-6040432/trump-xi-and-putin-shenzhen-china-russia-usa
- Meduza (Putin e a ponte): https://meduza.io/en/news/2026/11/19/putin-russia-refuses-to-negotiate-ceasefire-with-ukraine-after-strikes-on-crimean-bridge
- APA (Peskov, reunião a três): https://en.apa.az/cis-countries/kremlin-reveals-details-of-putin-xi-trump-meeting-ukraine-was-not-main-topic-of-trilateral-summit-537207
- Korea Times (Macron): https://www.koreatimes.co.kr/world/20261120/macron-says-trump-xi-putin-declaration-not-reorganization-of-the-world
- Yahoo (Hurst): https://www.yahoo.com/news/politics/articles/xi-putin-trump-summit-heavy-193205437.html
- Al Jazeera (recusa chinesa antes da cúpula): https://www.aljazeera.com/news/2026/11/16/why-is-china-not-keen-on-a-nuclear-treaty-with-us-and-russia

e tirar "Yahoo/NewsNation", que tem o resumo divergente do TPI.

**Depois**: renderizar de novo (slides e story) e reenviar para revisão. Leve: o crédito do slide 9 diz "domínio público" para uma foto CC0; é aceitável, mas o certo seria "CC0".

## Fatos refeitos pelo revisor (busca própria)
- Texto da declaração: Xinhua, Casa Branca, People's Daily, CGTN, The National, Bernama.
- Duração de ~90 min e "primeira" reunião: NPR, Globe and Mail, Washington Post.
- Peskov × Ushakov: APA, Saudi Gazette, bne IntelliNews/Yahoo.
- Putin/ponte: Meduza, Anews, Yeni Safak.
- Xi "frutífero" (Xinhua, via NBC/US News); "groundbreaking" = chancelaria chinesa em 16 nov (political.org e prévias).
- Hurst: Yahoo/Guardian. Macron: Korea Times, France 24.
- Observação: WebFetch não resolve lufkindailynews.com nem rt-english.com nesta sessão; a conferência foi feita por WebSearch.
