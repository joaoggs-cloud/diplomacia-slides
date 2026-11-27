# APROVADO (coordenador, rodada 2, 27 nov): correções 1–8 aplicadas, fotos novas, slides relidos. Reconferir Áden em 29 nov.

REPROVADO

# Revisão — 2026-11-30-houthis-60-km-de-aden (revisor, 27 nov 2026, noite)

A apuração central se sustenta. Os 60 km agora têm três agências independentes: AFP (15 nov), Reuters (Japan Times, 16 nov) e AP (24–25 nov), além do Crisis Group. O post foi reprovado por quatro motivos: duas URLs de fonte quebradas e uma atribuição que não consegui confirmar, um slide de Hodeidah que conta só um lado, a repetição e o descasamento das fotos, e um erro de cronologia na legenda. Todas as correções são pontuais.

| Item | Situação |
|---|---|
| 1. Fatos | problema (A1–A5) |
| 2. Isenção | problema (B1) |
| 3. Imagens: licenças | ok (as 3 conferidas no Commons: ISS-47 PD/NASA; Bab-el-Mandeb outer space PD/NASA JSC; Steamer Point CC BY-SA 2.0, Brian H. Spier). Créditos no slide e na legenda ok. Descartar a foto da Reuters foi correto. |
| 3. Imagens: uso e coerência | problema (C1–C3) |
| 4. Texto | ok no geral: todos os slides com até 45 palavras (máx. 44, no slide 5), as cenas com até 18 (máx. 17), só o título da capa e o do CTA, sem tag e sem factbox. Pequeno problema em D1. |
| 5. Visual | problema leve: no slide 5, "Al-" fica no fim de uma linha e "Kharaz" no começo da seguinte (D1). Nada cortado, numeração 1/10–10/10 certa, texto legível, degradê ok. |
| 6. Legenda | 1.664 caracteres, sem emoji, sem pergunta, primeiro comentário vazio, 6 hashtags do post + base: ok. Erro de cronologia (E1) e fontes a trocar (A5). |
| 7. Reel | problema (F1–F3). Payload: TRIAL_REEL, 30 nov 19:01, legenda com 887 caracteres: ok. |
| Story | ok (capa centralizada, sem texto extra) |
| Política brasileira | ok (ausente) |

## Checagem independente (refeita por mim)
- **60 km / Lahj / Al-Kharaz:** AFP via SCMP (15 nov); **Reuters** via Japan Times (16 nov: "positioned at the al-Kharaz camp in al-Madariba", 60 km); **AP** de 24–25 nov (KSL, Business Standard, France 24: "about 60 km"); Crisis Group (semana de 23 nov). Situação em 27 nov: nenhum relato de avanço além disso nem de ataque à cidade. Em 27 nov, o embaixador iemenita na Rússia disse à TASS que o governo não pretende deixar Áden. Há relatos de ataques houthis com mísseis contra Áden e de reforços na frente de Abyan, ao leste.
- **Retirada de Bab al-Mandeb/Dhubab, 15 nov:** Al Jazeera (URL do post confirmada), Times of Israel, Middle East Eye, Reuters via Yahoo. Ok.
- **Alimi, 4 out:** Al Jazeera (URL confirmada), Al Arabiya, Arab News. Ok. **Ofensiva/escalada em set:** Reuters via Yahoo ("offensive launched in September"). Ok.
- **60 alvos:** é o porta-voz da coalizão, Turki al-Maliki, na Al Jazeera (18 nov, URL confirmada) e na Arab News. Ok. A operação foi feita em 17 nov e anunciada em 18 nov.
- **"Hipotético":** France 24 (AP), atribuído a "um oficial iemenita". Ok.
- **Hodeidah, 25 nov:** The National, Gulf News, Times of Israel, Al Hurra e Marine Insight: tem 2ª fonte independente. A coalizão diz que atacou em resposta a ataques de drones houthis contra a Arábia Saudita e que avisou os civis para deixar o porto. Os houthis ameaçaram Jeddah e outros portos sauditas e depois disseram ter atacado Jeddah e Jazan, sem confirmação saudita (Times of Israel, Gulf News). Ok, mas falta contexto no slide (B1).
- **Análise "cortar o abastecimento":** existe (New Arab; analista Mohammed al-Basha: estradas pelo leste, via Abyan), mas **não achei na matéria da AP**. A atribuição "pela AP" não se confirma (A3).

## Correções exatas

### A. Fatos e fontes
- **A1 (URL quebrada).** Em `fontes`, troque a URL "The New Arab (Hodeidah)" por `https://www.newarab.com/news/saudi-led-coalition-strikes-hodeidah-houthis-threaten-ports` (sem "-as-"). Acrescente como 2ª fonte `{"nome": "The National (25 nov, Hodeidah)", "url": "https://www.thenationalnews.com/news/mena/2026/11/25/saudi-led-coalition-strikes-hodeidah-port-after-riyadh-attack/"}`.
- **A2 (URL quebrada).** Troque a URL "The New Arab (prontos para atacar Áden)" por `https://www.newarab.com/news/yemen-armed-forces-says-houthis-ready-attack-aden`.
- **A3 (atribuição).** No slide 8 (`slides[6]`), troque "Analistas ouvidos pela AP" pela redação do item D2.
- **A4 (data).** No slide 7 (`slides[5]`), a France 24 data a declaração do exército em **24 nov**, e a AP circulou entre 24 e 25 nov. Troque "Em 25 nov, o exército iemenita disse" por "Em 24 nov, o exército iemenita disse". Se a New Arab confirmar 25 nov, pode manter. No slide 6 (`slides[4]`), troque "Por volta de 18 nov" por "Em 18 nov".
- **A5 (fontes não confirmadas).** Não consegui localizar as URLs da ABC News e do Jerusalem Post. Substitua:
  - "AP via ABC News (25 nov)" → `{"nome": "AP via KSL (25 nov)", "url": "https://www.ksl.com/article/51647806/houthi-rebels-close-in-on-aden-as-yemeni-forces-dig-in-behind-a-fortified-line"}`
  - "Jerusalem Post" → `{"nome": "Arab News (coalizão, 60 alvos)", "url": "https://www.arabnews.com/middle-east/military-coalition-carries-out-wave-of-strikes-on-houthi-targets-3012714"}`
  - acrescente `{"nome": "Reuters via Japan Times (16 nov, 60 km)", "url": "https://www.japantimes.co.jp/news/2026/11/16/world/houthis-aden-govt-defences/"}` e `{"nome": "France 24 (24 nov)", "url": "https://www.france24.com/en/middle-east/20261124-yemen-army-houthi-attack-aden"}`.

### B. Isenção
- **B1. Slide 9 (`slides[7]`, Hodeidah).** Hoje o slide mostra só o bombardeio e o lado humanitário. Faltam a justificativa que a própria coalizão deu, o aviso aos civis e a alegação houthi de ter atacado portos sauditas. Texto novo (44 palavras):
  `Em 25 nov, a coalizão bombardeou o <strong>porto de Hodeidah</strong>, por onde entra boa parte dos alimentos do país. Disse responder a ataques de drones houthis e avisou civis para deixar a área. Os houthis disseram ter atacado portos em Jeddah e Jazan; Riad não confirmou.`

### C. Imagens
Três fotos, cada uma usada três vezes, **não é aceitável** como está:
- **C1.** Os slides 2, 5 e 7 usam o mesmo quadro de satélite. Como a imagem é vertical, o `foco` não muda nada e as três telas saem idênticas.
- **C2.** O slide 9 (Hodeidah) usa o satélite de Bab al-Mandeb, que não tem relação com Hodeidah.
- **C3.** `alt_text` cita "mapa das províncias", mas o post não tem mapa.

**Plano de troca** (licenças conferidas no Commons hoje; cada foto no máximo 2 vezes; todas coloridas). Mantenha `credito_custom` com "Foto de arquivo" + ano.

| Slide | Texto | Arquivo | Licença / autor |
|---|---|---|---|
| 1 capa | 60 km | manter `File:Aden. Steamer Point. Aug 2013 (9727325813).jpg` | CC BY-SA 2.0, Brian H. Spier |
| 2 | Áden sede / set | `File:Aden crater.jpg` (2304×1728, bairro de Crater) | CC BY-SA 3.0, Haimasoph |
| 3 | Alimi, 4 out | `File:Rashad al-Alimi (2023).jpg` (enquadrar em Alimi; 1411×1980) | CC BY 2.0, Governo do Reino Unido (Kirsty O'Connor/Cabinet Office) |
| 4 | retirada de Bab al-Mandeb | `File:Bab-el-Mandeb Seen From Midchannel (cropped).jpg` (2783×1818, 2023, vista do estreito ao nível do mar) | CC0, Richard Weil |
| 5 | Lahj / 60 km | `File:Governorates of Yemen named.svg` (mapa com Lahij e Aden) ou `File:Location of Lahij.svg` | CC BY-SA 3.0, Jarke |
| 6 | 150 km de costa + 60 alvos | `File:Boeing F-15SA Eagle Royal Saudi Air Force 5D4 2291 (53919688252).jpg` (5404×3608, 2024) | CC BY 2.0, Ronnie Macdonald |
| 7 | trincheiras em Áden | manter `File:ISS-47 Port of Aden, Yemen.jpg` | PD, NASA |
| 8 | rotas de abastecimento | `File:Port Of Aden Yemen.jpg` (1920×1080, 2010) | CC BY-SA 3.0, T3n60 |
| 9 | Hodeidah | `File:Al Hudaydah Market, Yemen (11042765095).jpg` (6016×4016, mercado de Hodeidah, 2013; combina com "alimentos") | CC BY-SA 2.0, Rod Waddington |

Reserva para o slide 9: `File:Bab-el-Mandeb, outer space.jpg` (PD, mostra a entrada do Mar Vermelho). **Não usar:**
- `File:Yemeni Houthi troops ride on the back...jpg`: marcado como "Public domain, autor desconhecido", origem duvidosa (possível agência) e com armas;
- `File:Yemeni Civil War 2 December 2025.svg`: mapa de controle defasado em quase um ano.

Novo `alt_text`: `Carrossel sobre o avanço dos houthis a cerca de 60 km de Áden, no Iêmen, com fotos de arquivo de Áden, de Hodeidah e do estreito de Bab al-Mandeb e mapa das províncias.` Se o mapa não entrar, tire "e mapa das províncias".

### D. Texto / visual
- **D1. Slide 5 (`slides[3]`).** Texto novo (37 palavras). Ele traz a confirmação por outras agências e impede a quebra de "Al-Kharaz" no fim da linha (hífen não separável):
  `Em 15 nov, segundo a <strong>AFP</strong>, os houthis tomaram dois distritos da província de Lahj e chegaram ao acampamento de Al&#8209;Kharaz, a cerca de 60 km de Áden. A Reuters e, em 24 nov, a AP relataram a mesma distância.`
- **D2. Slide 8 (`slides[6]`).** Texto novo (35 palavras):
  `Analistas ouvidos pela imprensa internacional avaliam que os houthis podem tentar cortar as estradas de abastecimento de Áden, pelo leste, via Abyan, em vez de invadir a cidade de imediato. É uma avaliação, não um fato.`

### E. Legenda
- **E1 (cronologia errada).** Troque "Dias antes, forças do governo haviam se retirado da região de Bab al-Mandeb para concentrar a defesa em Áden." por "No mesmo dia, forças do governo anunciaram a retirada da região de Bab al-Mandeb para concentrar a defesa em Áden." A retirada foi anunciada em 15 nov, mesmo dia do relato da AFP.
- **E2.** Troque "Em 25 nov, o exército iemenita disse" por "Em 24 nov, o exército iemenita disse" (se aplicar A4). Troque também "A posição de 60 km é a reportada pela AFP em meados de nov e pode ter mudado;" por "A distância de 60 km foi relatada pela AFP, pela Reuters e pela AP entre 15 e 24 nov e pode ter mudado;".
- **E3.** Troque "e os houthis ameaçaram portos sauditas no Mar Vermelho." por "e, depois de bombardear Hodeidah em resposta a drones houthis, viu os houthis dizerem ter atacado portos sauditas, sem confirmação de Riad." A frase fica mais longa; se preferir, use só: "e os houthis ameaçaram e disseram ter atacado portos sauditas, sem confirmação de Riad."

### F. Reel
- **F1 (repetição).** Os 60 km aparecem três vezes seguidas: título da capa, gancho da capa e cena 1. Troque `reel.cenas[0].texto_html` por (17 palavras):
  `Em 15 de novembro, os houthis tomaram dois distritos de Lahj, ao norte de Áden, segundo a <em>AFP</em>.`
- **F2 (Hodeidah sem contexto, mesma questão de B1).** Troque `reel.cenas[4].texto_html` por (18 palavras):
  `Em 25 de novembro, a coalizão saudita bombardeou o porto de <em>Hodeidah</em> e disse responder a drones houthis.`
  Imagem: a do mercado de Hodeidah (C), não o satélite de Bab al-Mandeb.
- **F3 (frase vaga: "as alegações" não diz quais).** Troque `reel.cenas[5].texto_html` por (15 palavras):
  `Os houthis dizem ter atacado portos sauditas no Mar Vermelho; a Arábia Saudita <em>não confirmou</em>.`
- Use também as fotos novas nas cenas (cena 2 → Aden crater; cena 3 → Bab-el-Mandeb Midchannel) para não repetir a Steamer Point em 4 das 6 cenas.

## Observação ao coordenador
O post sai em 30 nov, três dias depois desta checagem, numa frente que muda rápido. Antes de pedir a aprovação ao João, e de novo na noite de 29 nov, refaça uma busca com "Aden Houthis" na janela das últimas 24 h. Se houver ataque à cidade ou mudança de distância, o texto dos slides 5 e 7 precisa ser atualizado.
