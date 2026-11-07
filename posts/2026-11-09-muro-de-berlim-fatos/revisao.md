REPROVADO

Revisão — 2026-11-09-muro-de-berlim-fatos (SHA 70d7b88). Rodada 1.

| Item | Resultado |
|---|---|
| Fatos | problema (slide 7: horário) |
| Isenção | ok (tema histórico, sem lado privilegiado) |
| Imagens / licenças | problema (capa) |
| Texto | ok (sem títulos, 1 factbox, ≤ 45 palavras, sem emoji/pergunta) |
| Visual 01–10 | problema (capa pixelada e crédito truncado); demais ok, numeração 2/10…10/10 certa |
| Legenda | ok — 1.128 caracteres |
| Story | problema (herda a capa e o crédito truncado); fora isso ok, sem texto extra |
| Reel | não se aplica (não há reel.mp4; `reel/cenas/01.jpg` é sobra do workflow) |

## Fatos conferidos por busca própria
- 13 ago 1961; 155 km / 43 km / 302 torres; 2 mai 1989 (Hungria); 19 ago 1989 (Piquenique, 600–900 pessoas, "centenas" ok); tratado 31 ago 1990 (Berlim Oriental, Schäuble/Krause) e 3 out 1990 — ok.
- Checkpoint Charlie, 22–28 out 1961: tanques a ~80–100 jardas (75–90 m), fim negociado sem tiros — ok.
- Pelo menos 140 mortos (ZZF/Fundação, versão 4.0 de ago 2017; 101 eram fugitivos) — ok; factbox 136/138 → 140 em 2017 ok.
- Bornholmer: Jäger, 23h20–23h30 (pauta já registra a variação), ~20 mil atravessaram em cerca de uma hora segundo a Fundação — ok.
- Schabowski: a coletiva começou às 18h, mas a leitura da regra e o "ab sofort, unverzüglich" foram por volta das **18h53** (Hertle/bpb; ADN distribuiu às 19h04). O slide diz que ele "leu por volta das 18h" — impreciso.

## Correções obrigatórias
1. **Slide 7 (horário).** Trocar "Em <strong>9 nov 1989</strong>, por volta das 18h, o porta-voz do partido, <strong>Günter Schabowski</strong>, leu numa coletiva a nova regra de viagens." por
   "Em <strong>9 nov 1989</strong>, perto das 19h, o porta-voz do partido, <strong>Günter Schabowski</strong>, leu numa coletiva a nova regra de viagens."
2. **Capa (img01): trocar a foto.** `West and East Germans at the Brandenburg Gate in 1989.jpg` tem autor desconhecido e a licença CC BY-SA vem de quem "reproduziu" a foto (Lear 21), não de quem a tirou. Uma licença dada por quem só reproduziu não cobre os direitos do fotógrafo, e há foto muito parecida à venda em agência (Getty/photo12). Além disso o arquivo tem só 661 px e a capa sai pixelada, e o crédito aparece truncado ("Unknown photographer, Reproduction by ..."). Substituir por uma foto colorida de autor identificado da série `File:Berlin 1989, Fall der Mauer, Chute du mur 01.jpg` (ou 08/18/25, já em `busca_imagens.alternativas`), conferindo no `.json` do candidato o autor (esperado: Raphaël Thiémard, CC BY-SA 2.0) e a resolução (≥ 1080 px de largura). Rodar `scripts/imagens.py posts/2026-11-09-muro-de-berlim-fatos --so img01`, renderizar de novo e regerar o story (`scripts/story.py`). O crédito precisa sair inteiro no slide ("Foto: Raphaël Thiémard · CC BY-SA 2.0") e na legenda.
3. **Story:** regerar depois da troca da capa (o atual repete a foto e o crédito truncado).

## Recomendações (não bloqueiam)
- Slide 5: "Muitas morreram tentando atravessar." → "A maioria, 101, morreu tentando fugir." (mais preciso e evita repetir "morreram").
- Slide 6: "em Sopron" → "perto de Sopron" (o piquenique foi na fronteira, fora da cidade).
- Slide 8: a foto é da abertura na Potsdamer Platz (dia, a partir de 12 nov), não da Bornholmer Straße à noite. Se houver na série Thiémard uma foto noturna de passagem, use; senão, tudo bem manter.
- Legenda: "o porta-voz da Alemanha Oriental" → "o porta-voz do partido que governava a Alemanha Oriental" (igual ao slide 7).
- Capa (gancho): "a fronteira mais vigiada da Guerra Fria" → "uma das fronteiras mais vigiadas da Guerra Fria" (é um superlativo sem fonte).
- Apagar `reel/cenas/01.jpg` (sobra; não há reel neste post).

Fontes da checagem: bpb.de (Hertle, "Sofort, unverzüglich"), cvce.eu, zzf-potsdam.de, chronik-der-mauer.de (lista 140), stiftung-berliner-mauer.de (Bornholmer, node/1859), army.mil e armyheritage.org (Checkpoint Charlie), bundesregierung.de (Piquenique), germanhistorydocs.org e deutschland.de (tratado). O commons.wikimedia.org não abriu nesta sessão (DNS bloqueado), por isso a página do arquivo da capa não foi lida diretamente.
