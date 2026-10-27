APROVADO

# Revisão, rodada 2: Crise de Suez, 70 anos (SHA ed0b8ec)

Revisor, 26 out 2026, 21h35 (Brasília). Li os 10 JPEGs e o `post.json`. O payload `--rascunho` rodou sem erro e a legenda
tem 1.141 caracteres, com fontes, créditos e hashtags.

| Item | Resultado |
|---|---|
| 1. Fatos | ok. Os cortes nos slides 5 a 9 não introduziram erro (ver abaixo) |
| 2. Isenção | ok. O pretexto está atribuído no slide 3 e agora também na legenda (C9). A leitura do slide 9 está atribuída a historiadores |
| 3. Imagens: licença | ok. img06 IWM MH 23500 (Royal Navy, oficial, PD-UKGov). img09 GPO Israel (PD-Israel) |
| 3. Imagens: adequação | ok. Slide 6 mostra o HMS Buttress (L4099) desembarcando em Port Said, com fumaça ao fundo e sem vítimas. Slide 8 agora enquadra Burns com o boné da ONU. Slide 9 mostra capacetes azuis iugoslavos da UNEF no Sinai |
| 4. Texto / cara de IA | ok. Slides de conteúdo entre 36 e 44 palavras, sem título, tag ou factbox, sem emoji |
| 5. Visual | ok. Numeração de 2/10 a 10/10, nada cortado, texto legível. O P&B se justifica (1956) |
| 6. Legenda | ok: 1.141 caracteres |

## Correções da rodada 1
- C1 (img09): aplicada, com a foto da UNEF (GPO).
- C2 (img06): aplicada, com MH 23500. A descrição do arquivo confirma o HMS Buttress desembarcando tropas e veículos no porto de pesca de Port Said.
- C3 (foco do slide 8): aplicada. Burns aparece à esquerda.
- C4 (ordem do slide 8): aplicada. "aprovou a UNEF" (sem "a criação da") está correto, porque a Res. 1000 de 5 nov criou o Comando.
- C5 (slide 9): aplicada em versão curta. "Para historiadores" mantém a atribuição.
- C6 (slide 7): aplicada. Cortar "do seu jeito" não muda o sentido.
- C7 (slide 6): aplicada. "bloqueando-o" e "as atenções se dividiram" seguem corretos (os navios foram afundados a partir de 31 out; a URSS entrou em Budapeste em 4 nov, véspera de 5 nov).
- C8 (slide 5): aplicada. "O caso foi levado à Assembleia Geral" está correto (Res. 119, 31 out, sessão de emergência). Só perdeu o detalhe "de emergência".
- C9 (legenda): aplicada.
- Recomendações: capa ajustada ("O plano secreto que durou 9 dias") e `pb: true` marcado.

## Recomendações não bloqueantes
- Slide 4: o `"foco": "40% 60%"` não mudou o enquadramento visível. O logo ainda cobre parte do rótulo de Gaza e Khan Yunis no mapa, mas o assunto do slide (Sinai, setas, canal) está todo à mostra. Não reprovo.
- Slide 9: "Suez marcou quando Londres e Paris" soa um pouco truncado. Se couber: "Suez marcou o fim da era em que Londres e Paris agiam sozinhas" (o slide ficaria com cerca de 46 palavras, então só use se cortar outra palavra, por exemplo "Em 9 jan 1957" → "Em jan 1957").
- Legenda: o crédito genérico "domínio público via Wikimedia Commons" vale. O GPO de Israel pede crédito, então seria melhor "Fotos: IWM, Casa Branca, NASA, GPO Israel, via Wikimedia Commons".
- Agendamento 27 out 06:01: agora são 21h35 de 26 out, então ainda há mais de 4 h até o slot. O coordenador deve confirmar que este post, e não a Bomba Tsar, ocupa o slot.

---

# Rodada 1 (histórico)

Veredito da rodada 1: REPROVADO (SHA a8679ea)

Revisor, 26 out 2026, 21h30 (Brasília). Rede da sessão: só o WebSearch funcionou. Commons, history.state.gov e
upload.wikimedia.org voltaram 403/ENOTFOUND no curl e no WebFetch. As licenças foram conferidas pelo
conteúdo das páginas do Commons que aparece no WebSearch (`allowed_domains: commons.wikimedia.org`).

| Item | Resultado |
|---|---|
| 1. Fatos (datas, números, nomes) | ok no geral. Ajustes nos slides 5, 6, 7, 8 e 9 (ordem, atribuição e precisão) |
| 2. Isenção | ok. Verbos neutros; o conluio está atribuído no slide 3. A legenda precisa atribuir o mesmo |
| 3. Imagens: licença | **problema**: slide 9 (Capital Press) reprovado; slide 6 (IWM HU 4163) com origem duvidosa |
| 3. Imagens: adequação | **problema**: no slide 8, o recorte tira Burns (comandante da UNEF) do quadro |
| 4. Texto / cara de IA | ok. Nenhum título ou tag nos slides de conteúdo, sem factbox, máx. 45 palavras (slide 8). Sem emoji |
| 5. Visual (10 JPEGs) | ok. Numeração 2/10 a 10/10 certa, nada cortado, texto legível. P&B se justifica (1956) |
| 6. Legenda | ok: 1.103 caracteres com créditos e hashtags; payload `--rascunho` rodou sem erro |

## Fatos conferidos por conta própria (WebSearch)
- Veto em 30 out 1956: o projeto dos EUA (recuo de Israel) teve 7 votos a 2 (Reino Unido e França contra). A Res. 119 (31 out) convocou a sessão de emergência por causa dos vetos. **Confere.**
- UNEF: Res. 998 (4 nov, proposta canadense, 57 a 0, 19 abstenções) e Res. 1000 (5 nov, cria o Comando e nomeia Burns). "A ONU aprovou em 5 nov" **confere** (ONU/UNISPAL).
- Bulganin, 5 nov: cartas a Reino Unido, França e Israel com ameaça de foguetes; carta a Eisenhower propondo ação naval e aérea conjunta. A CIA julgou improvável um ataque. **Confere**, mas o texto precisa de ajuste (ver slide 7).
- Cerca de 40 navios afundados pelo Egito (ONU/CVCE) e canal reaberto em abr 1957 (24 abr, segundo History.com). **Confere.**
- Sèvres (22 a 24 out), ultimato de 30 out (12 h, 16 km), bombardeio em 31 out, saltos em 5 nov e desembarque em 6 nov, Eden em 9 jan 1957, Pearson com o Nobel de 1957, saída anglo-francesa em 22 dez 1956 e saída de Israel em mar 1957: batem com a pauta (2 fontes cada) e com fatos consolidados.

## Correções obrigatórias

### C1. Slide 9, imagem img09 (licença): TROCAR
`Lester B. Pearson 1957 (4951614).jpg`, autor "Capital Press". A Capital Press Ltd. era a empresa de **Duncan Cameron**,
fotógrafo de imprensa de Ottawa com contrato no Parlamento (morto em 1985). É foto de agência/imprensa comercial,
e a regra é não usar. A situação também é frágil: no Canadá, ou vale vida + 50 (até 2035) ou 50 anos da
criação; nos EUA, o copyright foi restaurado pela URAA. Notei ainda que a `busca_imagens` pedia
`File:Lester B. Pearson.jpg` e o script trouxe outro arquivo. O candidato `imagens/candidatos/img09_op2` é a mesma foto
recortada e também está reprovado.
**Correção:** em `busca_imagens` → img09, use
`"query": "File:UNEF Yugoslav soldiers 15-01-1957.jpg"` (Coleção Nacional de Fotos de Israel/GPO, PD-Israel, soldados
iugoslavos da UNEF no Sinai em 15 jan 1957: mostra a força de paz de verdade), com
`"alternativas": ["File:Prime Minister Lester B Pearson with President Lyndon B Johnson.jpg"]`. A alternativa só vale se a
página do Commons mostrar obra do governo dos EUA (Casa Branca/LBJ Library, PD-USGov). Se mostrar agência, descarte.
Não use `File:Lange martino pearson.jpg` (foto da OTAN, que o Commons trata como obra do governo dos EUA: justificativa fraca).
Depois rode `python3 scripts/imagens.py posts/2026-10-27-crise-de-suez-70-anos --so img09`.

### C2. Slide 6, imagem img06 (licença/origem): TROCAR
`British tanks in Port Said.jpg` é IWM **HU 4163**, autor desconhecido. A série HU do IWM reúne doações
privadas, não fotos oficiais (as oficiais da Suez são MH). O PD-UKGov depende de ser obra da Coroa, e isso não está
provado. A segunda justificativa da página (lei egípcia) não se aplica a uma foto de soldado britânico.
**Correção:** `"query": "File:The Suez Crisis (operation Musketeer) 1956 MH23500.jpg"` (IWM MH 23500, foto oficial:
navio de desembarque HMS Buttress descarregando no porto de Port Said; combina com "desembarcaram em Port Said"),
com `"alternativas": ["incategory:\"Suez Crisis\" Port Said MH"]`. Confira se a página tem PD-UKGov (foto oficial
anterior a 1 jun 1957). Evite `Troops of 3rd Battalion Parachute Regiment escort a captured Egyptian soldier...` (prisioneiro identificável).

### C3. Slide 8, enquadramento da img08
Na foto original (GPO, D330-011, 16 dez 1956, PD-Israel: licença ok, é órgão de governo e não agência) o general
**E. L. M. Burns**, comandante da UNEF, aparece à esquerda. O recorte atual mostra só a mão dele e deixa Dayan e um
oficial dos EUA. Do jeito que está, o slide da UNEF não mostra a UNEF.
**Correção:** no slide 8, acrescente `"foco": "0% 30%"` para enquadrar Burns e o aperto de mão. Recomendado: na
legenda, deixe o crédito como "Foto: Coleção Nacional de Fotos de Israel/GPO" (o GPO pede crédito).

### C4. Slide 8, ordem cronológica (texto exato)
Hoje o cessar-fogo de 6 nov vem antes da UNEF de 5 nov. Substituir por:
> Em 5 nov, a ONU aprovou a criação da <strong>UNEF</strong>, a primeira força de paz armada. No dia 6, britânicos e franceses aceitaram o cessar-fogo. Suas tropas saíram em dez 1956, Israel deixou o Sinai e Gaza em março de 1957 e o canal reabriu em abril.

(44 palavras)

### C5. Slide 9, frase interpretativa (texto exato)
"A crise mostrou que Londres e Paris já não decidiam sozinhas: o peso passara a Washington e Moscou" está escrita como fato,
mas é análise. Substituir o slide por:
> A ideia da UNEF veio do canadense <strong>Lester Pearson</strong>, Nobel da Paz de 1957. Em 9 jan 1957, o premiê britânico Anthony Eden renunciou, alegando problemas de saúde. Para muitos historiadores, Suez marcou o momento em que Londres e Paris deixaram de agir sozinhas: o peso passara a Washington e Moscou.

(49 palavras: passa do limite de 45 do roteiro. Para ficar em 45, troque "alegando problemas de saúde" por "alegando saúde"
e "Para muitos historiadores," por "Para historiadores,". Se o slide de Pearson ficar com a foto da UNEF, o texto continua coerente.)

### C6. Slide 7, carta de Bulganin (texto exato)
"uma carta ameaçadora a Londres, Paris e Tel Aviv" mistura três cartas. E "Washington recusou uma ação conjunta" fica sem
contexto, porque a proposta foi feita a Eisenhower. Substituir por:
> No mesmo 5 nov, o premiê soviético Bulganin mandou cartas a Londres, Paris e Tel Aviv ameaçando usar foguetes e propôs a Eisenhower uma ação conjunta. Washington recusou, mas pressionou do seu jeito: a libra sofria ataques e o apoio financeiro dos EUA dependia do cessar-fogo.

(45 palavras)

### C7. Slide 6, verbo e ordem (texto exato)
Paraquedista salta, não desembarca. Substituir por:
> Em 5 nov, paraquedistas britânicos e franceses saltaram sobre <strong>Port Said</strong>; no dia 6, fuzileiros desembarcaram. O Egito já tinha afundado cerca de 40 navios no canal, que ficou bloqueado. Na véspera, a União Soviética invadira a Hungria, e as atenções do mundo se dividiram.

(43 palavras)

### C8. Slide 5, cronologia do veto (texto exato)
O veto foi em 30 out, antes dos bombardeios. Substituir por:
> Em 31 out, aviões britânicos e franceses começaram a bombardear alvos no Egito. Na véspera, no Conselho de Segurança, Reino Unido e França tinham vetado um projeto dos EUA que pedia o recuo de Israel. O impasse levou o caso à Assembleia Geral, em sessão de emergência.

(45 palavras)

### C9. Legenda, atribuição do pretexto (texto exato)
O slide 3 atribui o plano a "documentos e historiadores"; a legenda afirma sem atribuir. Trocar
"lançaram um ultimato que servia de pretexto para ocupar o canal." por
"lançaram um ultimato que, segundo documentos revelados depois, servia de pretexto para ocupar o canal."

## Recomendações (não bloqueiam)
- Capa: um acordo assinado em 24 out não "durou 9 dias"; o que durou foi a guerra (29 out a 6/7 nov). Opção mais precisa:
  `O plano <span class="hl">secreto</span> que durou <span class="hl2">9 dias</span>`.
- Slide 4 (mapa de West Point, PD-USGov: ok): o logo cobre a região de Gaza e Khan Yunis no mapa. Se o render permitir, use `"foco": "40% 60%"`.
- `busca_imagens`: marque `"pb": true` nas buscas históricas (img01, img03 a img06, img08), conforme a regra editorial.
- Agendamento 27 out 06:01: a pauta diz que este post é alternativa à Bomba Tsar no mesmo slot. O coordenador deve
  confirmar qual vai e, se for este, refazer o render, o commit e o SHA antes de criar o rascunho. Hoje, 21h30, ainda há mais de 4 h até o slot.

## Licenças das demais imagens (ok)
img01 Port Said do ar (IWM MH 23509, Fleet Air Arm, oficial, PD-UKGov) · img02 ISS (NASA, PD-USGov) · img03 porta-aviões
(Royal Navy, oficial) · img04 mapa (Dep. de História da Academia Militar dos EUA, PD-USGov) · img05 810 Sqn (Fleet Air Arm,
oficial) · img07 Eisenhower (Casa Branca, PD-USGov) · img08 Dayan e Burns (GPO Israel, PD-Israel; ok com o novo enquadramento).
