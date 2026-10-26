REPROVADO

# Revisão — 2026-10-27-bomba-tsar-65-anos (slides SHA 5c6b394)

Obs.: nesta sessão o proxy bloqueia ctbto.org, ahf.nuclearmuseum.org, nuclearweaponarchive.org, wikipedia e commons (403). Fatos conferidos por buscas restritas a cada domínio (trechos das próprias páginas), não por leitura integral.

| Item | Resultado |
|---|---|
| 1. Fatos | quase todos ok; 2 problemas (horário, foto/tratado) |
| 2. Isenção | ok (histórico, sem adjetivos, sem glorificar) |
| 3. Imagens | PROBLEMA: img01 vem da AP; img08 é de outro evento; img04 repetida; img01 repetida |
| 4. Texto | ok no estilo (0 títulos, 1 factbox, sem tag, sem emoji, ≤ 44 palavras); ajustes pontuais |
| 5. Visual | ok em geral; slide 5 quebra "10.500 / m."; slide 7 rótulos do mapa sob o texto |
| 6. Legenda | ok — 1.158 caracteres, sem emoji, pergunta no fim; payload passou |

## Fatos conferidos
- Encomenda em jul 1961 (encontro Khrushchev–Sakharov em 10 jul 1961) e ~100 Mt: AHF + Nuclear Weapon Archive (NWA). ok
- Teste ligado ao 22º Congresso do PCUS: fontes secundárias e NWA. ok
- "Mãe de Kuzka" (Kuz'kina mat'), AN602, "Tsar Bomba": AHF. ok
- Urânio-238 do estágio final trocado por chumbo; rendimento caiu à metade; 50 Mt valor russo (AEC estimou 55–60 Mt): NWA + AHF. ok
- ~27 t; Tu-95 modificado (Tu-95V) pintado de branco refletivo; soltura a 10.500 m; paraquedas; explosão a ~4.000 m: CTBTO (FAQ) + NWA. ok
- 30 out 1961, Novaya Zemlya: CTBTO + AHF. ok. **11h32 é horário de Moscou**, não "horário local" nas fontes.
- Clarão visto a ~1.000 km: CTBTO. ok
- Nuvem: AHF ~40 milhas / "sete vezes o Everest"; NWA 64 km; CTBTO 60 km. "passou de 60 km" ok.
- Janelas quebradas a centenas de km (NWA: ~900 km em Dikson; AHF: ~560 milhas). ok
- Onda registrada após a 3ª volta à Terra: AHF, atribuída. ok
- "Mais de 3.000 vezes Hiroshima": CTBTO (15 kt → >3.000; outra página dá ~3.800). ok
- Tratado de 5 ago 1963 (EUA, URSS, Reino Unido, Moscou): State Dept + JFK Library + Britannica. ok, mas proíbe testes na atmosfera, no espaço e debaixo d'água.
- Sakharov "um dos projetistas" (montou a equipe com Adamsky, Babayev, Trutnev, Smirnov): AHF + RFE/RL. Nobel da Paz 1975. ok

## Correções obrigatórias

1. **img01 (capa e slide 6) — foto de agência.** O Commons dá como fonte "AP Newsroom" e autor "Cover Images/…/Associated Press"; a base de domínio público é "publicado nos EUA sem aviso de copyright" (só vale nos EUA) e o arquivo foi enviado em 1 mar 2026 (risco de remoção). Regra do CLAUDE.md: nunca usar fotos de agências (AP). Além disso, a mesma foto aparece duas vezes (capa e 6).
   - Capa → `File:Tsar Bomba Revised.jpg` (o invólucro em Sarov, colorido, CC BY-SA 3.0, Croquant/Hex). Mantém o título.
   - Slide 6 → `File:Novaya Zemlya testing map.png` (hoje no slide 7; mostra a zona C/Sukhoy Nos, área do teste), com `"foco"` que deixe "Sukhoy Nos / C" acima do degradê.
   - Slide 7 → `File:NovayaZemlya.A2001222.0835.250m.jpg` (NASA, domínio público, colorida) ou `File:Belushya guba novaya zemlya russia nasa photo.jpg`.
   - Se o coordenador preferir manter a bola de fogo, só com decisão explícita do João (é a única imagem real do teste), e com crédito correto.

2. **img04 repetida (slides 3 e 4) e risco de induzir erro.** Com a capa usando o invólucro, tire-o dos slides 3 e 4:
   - Slide 3 (mãe de Kuzka) → `File:Nikita Khrushchev 1960.jpg` (Khrushchev na Assembleia Geral da ONU, 22 set 1960, Warren K. Leffler/U.S. News & World Report, Library of Congress, domínio público — confirmar o fotógrafo na página).
   - Slide 4 (projeto encolheu) → `File:Comparative nuclear fireball sizes.svg` (domínio público, Fastfission; mostra Tsar Bomba 50 Mt). Alternativa: deixar o invólucro aqui e trocar a capa.
   - Onde o invólucro aparecer, inclua no texto: "Na foto, um invólucro do mesmo tipo, exposto no museu nuclear de Sarov." (no slide 4 ficaria com 43 palavras). Na capa não é necessário.

3. **Slide 8 — foto de outro evento.** O NARA/Knudsen ("Photographing signed Treaty") é da Sala dos Tratados da Casa Branca em **7 out 1963** (ratificação americana), não da assinatura de 5 ago 1963 em Moscou.
   - Trocar por `File:Test Ban Treaty (1963) - last page.jpg` (página das assinaturas, 5 ago 1963, domínio público, ourdocuments.gov). 
   - Texto exato: "A Tsar Bomba nunca foi usada como arma: grande e pesada demais para ser prática, serviu de demonstração política. Em <strong>5 ago 1963</strong>, EUA, URSS e Reino Unido assinaram em Moscou o tratado que proíbe testes nucleares na atmosfera, no espaço e debaixo d'água." (43 palavras)

4. **Slide 6 — horário.** Trocar "por volta das 11h32 (horário local)" por "por volta das 11h32 (horário de Moscou)".

## Correções recomendadas (não bloqueiam sozinhas)
5. Slide 5: a quebra "10.500 / m." fica feia. Texto exato: "Com cerca de 27 toneladas, a bomba não cabia em um avião comum. Um Tu-95 modificado, pintado de branco para refletir o calor, a soltou a 10,5 km de altitude. Um paraquedas a freou até cerca de 4 km, para dar tempo de fuga."
6. Slide 2 em P&B: existe colorida livre, `File:Nikita Khruchchev Colour.jpg` (conferir licença). Pedido do João é foto colorida; use-a se a licença for livre. Sakharov 1989 (P&B, Anefo CC0) pode ficar.
7. Slide 9: o factbox (50 Mt / 15 kt) está solto no slide do Sakharov. Mova para o slide 6 ou apague. Sugestão de texto mais preciso (RFE/RL: ele já questionava os testes antes da explosão): "Um dos projetistas, o físico <strong>Andrei Sakharov</strong>, já questionava os testes na época. Virou o dissidente mais conhecido da URSS, defensor do desarmamento e dos direitos humanos, e ganhou o <em>Nobel da Paz</em> em 1975."
8. Capa: "fez o clarão aparecer a 1.000 km" soa truncado. Sugestão: "A bomba cujo <span class=\"hl\">clarão</span> foi visto a <span class=\"hl2\">1.000 km</span>".

## Sem problemas
Estilo novo respeitado (texto corrido, sem títulos/tags nos slides, 1 factbox, capa sem etiqueta de nº de fontes), legenda e primeiro comentário sem emoji, pergunta de engajamento neutra, créditos presentes em todos os slides, numeração 1–10 correta, slide 10 (CTA) ok, Tu-95 (slide 5) nítido e coerente.
