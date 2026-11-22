REPROVADO

# Revisão: 2026-11-25-sparta-ii-golfo-da-finlandia
Revisor, 22 nov 2026 (noite). Post: qua 25 nov 06:01 · Reel 19:01.
Obs.: o WebFetch está bloqueado para france24, yle.fi e opensanctions, então a checagem foi feita pelo WebSearch (modo extended), com os resumos de várias fontes. A API do Commons bateu no limite de requisições, então a licença do arquivo sugerido para a capa precisa ser conferida pelo `imagens.py`.

| Item | Situação |
|---|---|
| 1. Fatos | problema: o estado do navio está desatualizado (rebocado em 22 nov); o 11 nov das restrições não foi confirmado; a fala do "diretor de comunicação" não foi confirmada; a reivindicação da "SBU" tem uma fonte só; o slide 8 tem frase sem fonte; 4h15/4h20 sem fuso |
| 2. Isenção | ok, com o ajuste de atribuição do slide 6 |
| 3. Imagens | problema: radar da ESA em P&B (2x); porto de Baltiysk sob o texto da autoria finlandesa; F-22 americano no slide de Orpo; fotos de Gogland baixadas e não usadas; 3 fotos repetidas; capa do Reel sem o aviso "não é o Sparta II" |
| 4. Texto | problema: "Sem governo" (ambíguo: lê-se como governo político); "resgate russo Murman" sem "navio"; "7.260 GT" é jargão. Contagem de palavras ok (≤45) |
| 5. Visual | ok: nada cortado, numeração 2/9 a 9/9 certa, créditos presentes, texto legível |
| 6. Legenda | ok no tamanho (1.367 caracteres). Problema de conteúdo: atualizar (veja abaixo) |
| 7. Reel | problema: cena 5 desatualizada ("domingo de manhã"); falta a cena do reboque; capa sem aviso de foto de arquivo; mesmas repetições de foto |
| 8. Regras CLAUDE.md | ok: sem emoji, sem pergunta, 7 hashtags + base, CTA sem pergunta, primeiro comentário vazio, 9 slides |

## Checagem dos pontos pedidos

1. **Estado do Sparta II: CONFIRMADO.** No domingo, 22 nov, o navio de resgate russo Murman rebocou o Sparta II para fora de águas finlandesas, rumo a águas russas. O navio saiu da zona econômica finlandesa, as restrições de tráfego foram suspensas e a missão da Guarda de Fronteiras terminou. Segundo Mikko Hirvi, da Guarda de Fronteiras, o reboque russo era "a solução mais segura". Um tripulante ficou levemente ferido. O navio não afundou e não foi visto vazamento. Fontes: France 24/AFP (https://www.france24.com/en/live-news/20261122-russian-cargo-ship-hit-by-ukrainian-drone-towed-to-home-waters), Yle (https://yle.fi/a/74-20258284), The Moscow Times (https://www.themoscowtimes.com/2026/11/22/russian-cargo-ship-still-on-fire-off-finland-after-attack-a94343), Al Jazeera 22 nov (https://www.aljazeera.com/news/2026/11/22/russian-cargo-ship-still-on-fire-off-finland-after-drone-attack), Irish Times (https://www.irishtimes.com/world/europe/2026/11/22/ukrainian-drones-attack-russian-cargo-ship-in-baltic-sea/).
2. **Orpo:** a frase foi publicada no X, em inglês: "War is spilling over into our immediate vicinity" (CNN, título "Finland warns Ukraine war 'spilling over'"; ERR/Euronews). As aspas são possíveis se for informado que é tradução e que veio do X, mas o discurso indireto atual é mais seguro e pode ficar. No mesmo post ele escreveu que "a Ucrânia tem o direito de revidar ao agressor". Não é obrigatório usar; se entrar, use as duas frases juntas para não editar o sentido.
3. **Horários:** 4h15 (aéreo) e "cerca de 5 min depois" (marítimo, perto de Kotka) estão confirmados, mas são **horário da Finlândia** (Brasília -5 h). As medidas foram suspensas às 7h43 e retomadas às 9h33 (as fontes divergem). **16-17 out:** só uma fonte clara (Daily Finland fala em 3 dias seguidos, ou seja, 16 a 18). **11 nov:** nenhuma fonte encontrada. Corte as datas.
4. **7.260 GT, Oboronlogistika e OFAC desde maio 2022:** confirmados (OFAC id 36696 / OpenSanctions; MagicPort; ficha do Commons IMO 9160994; Militarnyi/Aerotime para o vínculo com o Ministério da Defesa).
5. **Autoria:** as Forças de Defesa finlandesas chamaram de "provável" a autoria ucraniana (Al Jazeera, Euronews), e o comandante Ilja Iljin, da Guarda de Fronteiras, falou em drones ucranianos (Ukrainska Pravda, Yle). Não achei fala do "diretor de comunicação" sobre autoria: o coronel Huhtinen só aparece em legenda de foto da CNN. Kiev não assumiu o ataque até 22 nov (Irish Times, Moscow Times). **"Perto de Gogland": ok** (o local exato está em disputa). **Dois drones:** foi o governador da região de Leningrado, Aleksandr Drozdenko, quem disse (Al Jazeera, Yahoo/Missile War Monitor). Atribua a ele.
6. **11 nov:** a Finlândia anunciou em 12 nov ter detectado na véspera um ataque a um navio de guerra russo (Defense News/AP, Moscow Times, Al Jazeera). A reivindicação ucraniana está confirmada (Al Jazeera: "Ukraine took credit"), mas a "SBU" só aparece numa fonte (United24). Escreva "a Ucrânia".
7. **Slide 8, "rota de navios…":** sem fonte. Corte.
8. Fotos: correções abaixo.

## Correções exatas (post.json)

**Slide 2 (slides[0])**: texto ok. Trocar a imagem `img08` por `img02` (Gogland, colorida, já baixada; CC BY 2.0, Bernt Rostad) com `"foco": "50% 72%"`. A ilha tem de ficar acima do degradê.

**Slide 3 (slides[1])**: novo texto (43 palavras), mantendo `img04`:
`Segundo o governador russo da região de Leningrado, foram dois drones. A tripulação foi retirada, com um ferido leve. Barcos finlandeses e estonianos combateram o fogo e, em 22 nov, o <strong>navio de resgate russo Murman</strong> rebocou o Sparta II para águas russas.`

**Slide 4 (slides[2])**: texto:
`O Sparta II é um ro-ro de 7.260 toneladas de arqueação bruta operado pela <strong>Oboronlogistika</strong>, empresa de transporte ligada ao Ministério da Defesa russo. Os EUA impõem sanções ao navio desde maio de 2022.`
Imagem: trocar a ESA (P&B). Primeira opção, a foto do próprio navio com o nome antigo: `"query": "File:Cuxhaven Kugelbake Elbe 2004-Sloman Provider (ship, 2000) by-RaBoe.jpg"` (Category:IMO 9160994 → Sloman Provider; conferir a licença no `imagens.py`, provavelmente CC BY-SA). Crédito: "Sparta II, então Sloman Provider, em 2004". Se não servir (licença ou nitidez), use `img08` (Baltiysk, porto de destino).

**Slide 5 (slides[3])**: novo texto (40 palavras). Imagem: trocar `img04` pelo candidato `imagens/candidatos/img07_op2` (dois F/A-18 finlandeses, domínio público, USAF), que combina com a interceptação:
`Na madrugada de sábado, a Finlândia restringiu voos e navegação no leste do golfo, inclusive perto de Kotka, para proteger civis caso fosse preciso interceptar drones. A área já tinha sido fechada outras vezes neste ano pelo mesmo risco.`
(Fontes: NBC, Militarnyi; antecedentes: Yle 74-20256236 e Verkkouutiset.)

**Slide 6 (slides[4])**: novo texto (37 palavras). Trocar `img08` por `img06` (Gogland aerial photo2, CC BY 2.0). O porto militar russo sob o texto da autoria finlandesa confunde o leitor.
`As Forças de Defesa da Finlândia consideram <strong>provável que a Ucrânia seja a autora</strong>, e um comandante da Guarda de Fronteiras, Ilja Iljin, falou em drones ucranianos. Kiev não havia assumido o ataque até 22 nov.`
(Antes do APROVAR, o coordenador deve checar se Kiev se manifestou até 24 nov. Se sim, atualizar.)

**Slide 7 (slides[5])**: novo texto (36 palavras). Trocar `img05` (ESA P&B) por `img08` (Baltiysk, navios da Frota do Báltico, colorida), que combina com "navio de guerra russo":
`Não foi o primeiro episódio. Em 11 nov, a Ucrânia disse ter atingido um navio de guerra russo no golfo, e as Forças de Defesa finlandesas confirmaram ter detectado o ataque. É o <strong>segundo incidente em cerca de 10 dias</strong>.`

**Slide 8 (slides[6])**: novo texto (27 palavras), sem a frase da rota:
`O primeiro-ministro finlandês, Petteri Orpo, escreveu no X que a guerra está transbordando para a vizinhança imediata do país, que entrou na OTAN em abril de 2023.`
Imagem: trocar o F-22 americano (fora de contexto). Opções: retrato de Orpo, `"query": "incategory:\"Petteri Orpo\""`, escolhendo foto oficial colorida CC BY (Valtioneuvoston kanslia / UE). Se não houver, `img04` (Turva).

**Capa**: a foto "Karin Lehmann" com aviso no crédito é aceitável. Se a foto real (Sloman Provider) for nítida e livre, ela vira a capa, com crédito "Foto de arquivo: Sparta II (então Sloman Provider), 2004 · <autor> · <licença>", e o slide 4 fica com `img08`. Nesse caso, o slide 7 fica com `img04`.

**Repetições:** com o mapeamento acima, cada foto aparece no máximo uma vez nos slides 2 a 8 (img02, img04, navio real ou img08, F-18, img06, img08 ou img04, Orpo). Nada de P&B.

**Legenda** (substituir o 2º parágrafo; o resto fica igual):
`Em 21 nov, o cargueiro Sparta II, que seguia para Kaliningrado, foi atingido por drones perto da ilha russa de Gogland. O governador russo da região de Leningrado fala em dois drones; as Forças de Defesa finlandesas consideram provável que a Ucrânia seja a autora, e Kiev não havia assumido o ataque até 22 nov. A tripulação foi retirada, com um ferido leve, e a Finlândia restringiu o tráfego aéreo e marítimo no leste do golfo. No domingo, 22 nov, o navio de resgate russo Murman rebocou o Sparta II para águas russas. O premiê Petteri Orpo disse que a guerra está transbordando para a vizinhança imediata do país, membro da OTAN. Em 11 nov, a Ucrânia já havia dito ter atingido um navio de guerra russo no mesmo golfo.`
**Fontes**: acrescentar France 24 (22 nov, reboque) e Yle (https://yle.fi/a/74-20258284). Pode remover Militarnyi e CP24 se quiser encurtar.

## Reel
- `reel.cenas[4]` → `Para os militares finlandeses, a Ucrânia é a <em>provável autora</em>. Kiev não assumiu o ataque até 22 nov.` (17 palavras)
- Inserir após `cenas[1]`: `{"imagem": "img04", "texto_html": "No domingo, 22 nov, um navio de resgate russo <em>rebocou o Sparta II</em> para águas russas."}` (15 palavras) e trocar a imagem da cena "A Finlândia restringiu voos…" para o F-18 (img07_op2).
- Cena 1 e 5: trocar img08 por img02/img06, igual aos slides. Cena 3 (Oboronlogistika): foto real do navio ou img08, em vez da ESA P&B. Cena 6 (Orpo): a mesma imagem nova do slide 8.
- Capa do Reel (`reel/capa.jpg` / cena 01): o crédito mostra só "Jari Sjölund…". Precisa trazer o aviso "Foto de arquivo: Karin Lehmann (não é o Sparta II)", como a capa do carrossel, ou usar a foto real.
- Renderizar de novo o carrossel, o story e o Reel, e conferir que a ilha (slides 2 e 6) fica acima do degradê.
