REPROVADO

# Revisão: 2026-11-19-trilateral-nuclear-shenzhen (commit 058de5d)

Revisado em 16 nov 2026. Fatos-chave refeitos com WebSearch extended. O sipri.org e o commons.wikimedia.org não abrem nesta sessão (precisam ser liberados nas configurações de rede); os números do SIPRI foram confirmados pelo resumo do Yearbook 2026 citado nos resultados de busca.

| Item | Situação |
|---|---|
| 1. Fatos: encontro confirmado (Casa Branca, Kremlin, MRE chinês, 19 nov, APEC) | ok (Al Jazeera 14 nov, CNBC 16 nov, Anadolu) |
| 1. Fatos: agenda de Trump (nuclear, proliferação, Irã) | ok (porta-voz da Casa Branca; CNBC, Al Jazeera) |
| 1. Fatos: Reuters "não esperamos acordo" | ok ("We do not expect to get to any kind of agreement") |
| 1. Fatos: New START, 5 fev 2026, 1.550/700 | ok |
| 1. Fatos: SIPRI jan 2026 (5.420 / 5.042 / ~620 / quase 86%) | ok (resumo do SIPRI Yearbook 2026; total mundial ~12.187) |
| 1. Fatos: Mao Ning, fev 2026, "não está na mesma liga" | ok (Global Times, Anadolu) |
| 1. Fatos: capa "na mesma sala pela primeira vez" | **problema**: os três estiveram juntos nas cúpulas do G20 (Hamburgo 2017, Osaka 2019) e na APEC de Da Nang (2017). O que é inédito é a reunião só entre os três |
| 1. Fatos: capa "sem tratado nuclear entre EUA e Rússia" | **problema**: impreciso. Os dois continuam no TNP e no Tratado de Limitação de Testes (TTBT, 1974), que é bilateral. O que acabou foi o limite dos arsenais |
| 1. Fatos: slide 2 "um porta-voz chinês o descreveu como primeira reunião presencial" | **problema**: não achei essa fala atribuída a um porta-voz. Mao Ning falou em "estabilidade estratégica"; "o primeiro encontro a três" é como a imprensa descreveu |
| 1. Fatos: slide 6 "Trump não aceitou formalmente" | **problema**: desatualizado. Em 5 fev 2026, Trump **rejeitou** a oferta publicamente (Truth Social) e pediu um tratado novo (Reuters via Dawn/Cyprus Mail, 6 fev 2026; Arms Control Association, mar 2026) |
| 1. Fatos: slide 9, data e testes | **problema** leve: o post de Trump é de 29 out (EUA) / 30 out (Ásia), e as fontes divergem. Wright (DOE) falou em "explosões não críticas", sem explosão nuclear; Peskov disse que a Rússia responderia na mesma moeda. Ok com a data "out 2025" |
| 1. Fontes da legenda | **problema**: há fontes fracas ou de segunda mão (Reuters via Ukranews, IBTimes, Defence-Blog, China Strategy Group, Defencetalk). Os nomes com vírgula ("CNN, 13 nov, Anadolu, 14 nov…") ficam confusos na lista |
| 2. Isenção | **problema**: o slide 2 cita os três líderes, mas mostra só um close de Xi (a foto original é dele com Putin, e Putin saiu no corte). Nenhum adjetivo nem tom de torcida no texto. As hashtags dão o mesmo tratamento aos três |
| 3. Licenças | ok: CC0, domínio público e CC BY 4.0 (President of Russia, MoD russo, China News Service), todas creditadas no slide e na legenda |
| 3. Imagens: adequação | **problema**: o slide 4 usa o Shenzhen Bay Sports Center, que não tem relação com a cúpula, a foto está lavada e sem nitidez e tem um objeto escuro cortado no canto inferior direito. O slide 9 mostra uma explosão nuclear real (Sedan, 1962) sobre um texto que diz "sem detonação", e a foto sem contexto sugere que os EUA vão voltar a explodir bombas. O slide 8 (DF-61) **não engana**: é um míssil intercontinental chinês real, mostrado no desfile de 3 set 2025, mas a imagem é baixa (1290 px, tirada de vídeo) e fica aceitável |
| 4. Texto: palavras | **problema**: o slide 7 tem 40 palavras + 16 do factbox = 56, acima de 45. O factbox repete o "segundo estimativas" do texto. "cerca de… cerca de" se repete na mesma frase |
| 4. Cara de IA | ok: 0 títulos, 1 factbox, nenhum emoji, nenhuma pergunta, primeiro_comentario vazio |
| 5. Visual | **problema**: na capa, as duas primeiras linhas do título (fonte fina) ficam sobre prédios cheios de detalhe e perdem leitura. A numeração de 2/10 a 10/10 está certa, nada aparece cortado e o slide 10 está ok |
| 6. Legenda | ok no tamanho (1.247 caracteres), sem emoji e sem pergunta. A primeira frase tem o mesmo erro da capa ("à mesma mesa pela primeira vez") |
| 7. Reel | não se aplica (reel.gerar = false) |
| Story | ok no formato. Precisa ser renderizado de novo depois de trocar a capa |
| Layout: cor | ok: todas as fotos são coloridas (o slide 9 está marcado pb:true, mas a foto é colorida, o que não atrapalha) |

## Correções exatas (post.json)

### 1. Capa
- `capa.titulo_html`:
  `Trump, Xi e Putin em reunião a três pela primeira vez, <span class="hl">sem limite para os arsenais</span> de EUA e Rússia`
- `capa.gancho`:
  `Pelas estimativas do SIPRI, os três países somam cerca de 11 mil ogivas. O encontro é nesta quinta, em Shenzhen.`
- Visual: troque img01 por uma foto de Shenzhen com o terço inferior mais limpo (céu, água ou céu noturno). Sugestão de busca: `Shenzhen Bay skyline night` ou `Shenzhen Futian CBD Ping An Finance Centre` com `incategory:"Skylines of Shenzhen"`, colorida, com 1920 px ou mais. Os candidatos img01_op2 e op3 não servem: são conjuntos residenciais, como a atual. Se não achar outra, escureça o degradê da capa para o título ficar legível.

### 2. Slide 2 (texto, 43 palavras)
`Nesta quinta, 19 nov, <strong>Trump, Xi Jinping e Putin</strong> têm encontro marcado em Shenzhen, à margem da cúpula da APEC. Casa Branca, Kremlin e governo chinês confirmaram. Os três já estiveram juntos em cúpulas do G20, mas nunca numa reunião só entre eles.`
- Imagem (isenção): troque o close de Xi por uma foto em que os três tenham o mesmo destaque, de preferência a foto de família do G20 de Osaka 2019 (kremlin.ru, CC BY 4.0; busca `incategory:"2019 G20 Osaka summit" family photo`), conferindo se os três aparecem. Se não houver, use uma foto neutra de Shenzhen ou da APEC, sem nenhum líder.

### 3. Slide 4: só a imagem
Troque img04 (estádio). Use uma foto neutra e nítida de Shenzhen, diferente da capa (ex.: `Shenzhen Bay Bridge`, `Shenzhen Civic Center`, `Shenzhen Futian skyline night`), colorida e com 1920 px ou mais. O texto continua igual.

### 4. Slide 6 (texto, 42 palavras)
`Em 22 set 2025, Putin ofereceu respeitar os limites centrais por mais um ano, se os EUA fizessem o mesmo, sem prever verificação. Em 5 fev 2026, Trump recusou a oferta e defendeu um tratado novo. Washington quer que a <strong>China</strong> participe.`
- Nas `fontes`, troque "NPR, 4 fev 2026" (ou acrescente) por: `Reuters via Dawn (6 fev 2026)`, https://www.dawn.com/news/1971417/trump-rejects-putin-offer-of-one-year-extension-of-new-start-deployment-limits, e `Arms Control Association (mar 2026)`, https://www.armscontrol.org/act/2026-03/news/new-start-expires-us-urges-modernized-treaty

### 5. Slide 7 (texto, 39 palavras; sem factbox)
`Segundo estimativas do SIPRI para jan 2026, a Rússia tem <strong>5.420 ogivas</strong>, os EUA 5.042 e a China cerca de 620, 20 a mais que um ano antes. Somados, EUA e Rússia detêm quase 86% do inventário mundial.`
- Remova o `factbox`: estoura o limite de 45 palavras e repete "estimativas". Assim o post fica com 0 factbox.

### 6. Slide 9 (texto, 45 palavras)
`Em out 2025, Trump mandou o Pentágono retomar testes de armas nucleares. O Departamento de Energia disse que seriam testes <strong>não críticos</strong>, sem explosão nuclear. Moscou disse que agirá de acordo se alguém romper a moratória. Na foto, o teste Sedan, em Nevada, em 1962.`
- Mantenha a foto Sedan só com essa legenda no texto. Se preferir não mostrar explosão, troque pela alternativa `File:Aerial View of Sedan Crater.jpg` e mude a última frase para `Na foto, a cratera do teste Sedan, em Nevada, de 1962.`

### 7. Legenda
- Primeira frase:
  `Pela primeira vez, os líderes dos Estados Unidos, da China e da Rússia vão se reunir a três.`
- Troque "O New START, último tratado a limitar os arsenais de EUA e Rússia, expirou em 5 fev 2026" por: `O New START, último tratado a limitar os arsenais de EUA e Rússia, expirou em 5 fev 2026, e Trump recusou a oferta russa de manter os limites por mais um ano.` (o resto continua igual)

### 8. Fontes (`fontes`): nomes sem vírgula e fontes primárias
Use o formato `Nome (data)`. Substitua as fontes fracas:
- `Al Jazeera (14 nov)`: https://www.aljazeera.com/news/2026/11/14/trump-xi-and-putin-to-hold-first-three-way-summit-in-china
- `CNBC (16 nov)`: https://www.cnbc.com/2026/11/16/trump-xi-putin-ukraine-nuclear-tariffs-russia-iran-.html
- `Anadolu (14 nov)`: o link atual do Kremlin
- `CNN (13 nov)`: o link atual
- `Reuters via Ukranews`: mantenha só se não houver reprodução melhor da mesma nota da Reuters
- `SIPRI Yearbook 2026`: https://www.sipri.org/yearbook/2026/08 (no lugar de Defence-Blog e China Strategy Group)
- `Global Times (fev 2026)`: https://www.globaltimes.cn/page/202602/1355844.shtml e `Anadolu (fev 2026)`: https://www.aa.com.tr/en/asia-pacific/china-rejects-us-demand-to-attend-trilateral-nuclear-disarmament-talks/3841850 (no lugar de Defencetalk)
- `Al Jazeera (3 nov 2025)`: https://www.aljazeera.com/news/2025/11/3/how-will-limited-us-nuclear-tests-avoid-any-explosions (testes; junto com PBS)
- Remova IBTimes e IranWire (a agenda do Irã já está na CNBC e na Al Jazeera).

### 9. Depois das correções
Renderize de novo os slides e o story (`scripts/story.py`), confira a capa (título legível) e os slides 2, 4 e 9.

## Aviso ao coordenador (timing)
O post sai às 06:01 BRT de 19 nov, que são 17:01 em Shenzhen. A hora do encontro não foi divulgada, e a reunião pode já ter acontecido. Na noite de 18 nov, confira as manchetes. Se houver resultado ou adiamento, o texto "têm encontro marcado" e "nesta quinta" precisa ser adaptado antes do APROVAR.
