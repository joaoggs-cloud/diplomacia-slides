REPROVADO

Revisão do SHA 3dda0c5 (10 nov 2026). Os fatos centrais conferem. Reprovado por limite de palavras, por uma distorção na legenda e por três problemas de imagem. As correções são curtas: dá para refazer na mesma noite.

| Item | Resultado |
|---|---|
| 1. Fatos | ok no geral. Conferi por conta própria: 1ª rodada desde fev; Umerov chefe da inteligência exterior desde 3 ago 2026 (Meduza, RBC-Ucrânia); Medinski + Kostyukov (GRU); Witkoff e Kushner; quase 4 h (AP/NPR/CBC) x 4h30 (TASS/Kyiv Post); "construtivo e bastante substancial" (Anadolu, Ukrinform); Peskov sem prognóstico e Riabkov "cedo para avaliar" (TASS); europeus em Abu Dhabi fora da mesa, Kushner no X e Rubio "ainda não estão à mesa, mas deveriam" (TRT, bne). Problema: a legenda distorce a posição de Kiev (C3). |
| 2. Isenção | ok: 2 fotos da Ucrânia, 2 da Rússia, 1 dos EUA, e as alegações estão atribuídas. Ressalva: a frase "o que é uma alegação dele" (slide 8) soa como opinião (C4). |
| 3. Imagens/licenças | Licenças ok (Zelensky: retrato de 2019, CC BY 4.0, válida para arquivos do president.gov.ua anteriores a out 2022; Kremlin CC BY 4.0; Medinski CC0). Problemas: o interior do Emirates Palace no slide 2 sugere uma sede que ninguém confirmou (C2); os créditos estão cortados nos slides 4 e 5 (C5); no slide 8 o texto fala de Trump e a foto é de Witkoff, sem que o nome dele apareça (C4). |
| 4. Texto | Problema: slide 7 com 47 palavras e slide 2 com 51 (39 do texto + 12 do factbox) (C1). 2 títulos e 1 factbox: ok. |
| 5. Visual | ok: numeração 2/10 a 10/10 certa, nada cortado, fotos coloridas, rostos acima do degradê. |
| 6. Legenda | 1.236 caracteres, sem emoji e sem pergunta: ok. Distorção: C3. |
| 7. Reel | não há (`reel.gerar: false`). |
| Story | ok (repete a capa sem texto extra). |

## Correções obrigatórias

**C1. Palavras (máx. 45).**
- Slide 7 (`slides[5].texto_html`): `Delegações de Reino Unido, França, Alemanha, Itália, OTAN e UE estavam em Abu Dhabi, <strong>fora da sala principal</strong>. Peskov diz que a mesa é trilateral. Kushner defendeu no X “engajamento direto” entre Rússia e europeus; Rubio disse que eles deveriam estar à mesa.` (43 palavras)
- Slide 2 (`slides[0]`): apague a frase "O primeiro dia durou cerca de quatro horas." e troque `factbox.label` por `Primeiro dia`. O slide fica com 44 palavras.

**C2. Slide 2, sede não confirmada.** Nenhuma fonte cita o Emirates Palace nesta rodada (as de jan e fev foram no Al Shati Palace). Troque `img02` (saguão do Emirates Palace) por `imagens/candidatos/img09_op2` ("Skyline Abu Dhabi I (260477643).jpeg", Madlen Steiner, CC BY 3.0), com `"foco": "50% 30%"` para a marca 500px do canto inferior esquerdo ficar sob o degradê. Recomendado: no slide 7 a vista aérea do hotel junto com "estavam em Abu Dhabi" sugere que os europeus se hospedaram ali. Se der tempo, troque por outra foto da cidade.

**C3. Legenda, posição de Kiev.** Hoje está "Kiev rejeita ceder território sem garantias de segurança". Isso dá a entender que Kiev cederia território em troca de garantias, e Zelensky disse que não pode trocar Donbas por garantias (Ukrinform). Troque por: `e Kiev rejeita ceder território e cobra garantias de segurança`.

**C4. Slide 8, foto e texto.** Novo `texto_html`: `Trump disse esperar que a guerra termine <em>“em breve”</em>. Segundo Washington, representado em Abu Dhabi por <strong>Steve Witkoff</strong> (foto) e Jared Kushner, o objetivo não é um acordo final agora, e sim um quadro para negociações mais frequentes.` (39 palavras). Isso também tira "se apresentou como responsável por isso, o que é uma alegação dele", trecho que não consegui confirmar em segunda fonte e que soa como opinião.

**C5. Créditos inteiros.** Encurte `autor` em `imagens`: img04 → `Presidência da Ucrânia`; img05 → `Kremlin.ru`. Depois renderize de novo os slides e o story.

## Recomendações (não bloqueiam)
- Slide 4: a pergunta sobre "trocar Donbas por segurança" veio de uma entrevista de Zelensky à emissora dinamarquesa DR, não do balanço do dia. Sugestão (43 palavras): `Zelensky chamou o dia de “construtivo e bastante substancial”, com temas humanitários e garantias de segurança. Em entrevista, disse que os EUA perguntaram se Kiev trocaria Donbas por segurança, e que não pode. Kiev diz esperar uma troca de prisioneiros; Moscou não confirmou.`
- Slide 6: o retrato de Medinski (olhos semicerrados, meio sorriso) ao lado de "O que ninguém cedeu" pode passar por deboche, ainda mais perto do retrato oficial de Zelensky. Se houver outro retrato livre dele, use.
- Ainda não saiu nada do 2º dia. A delegação russa marcou entrevista coletiva para 11 nov (TASS), e 06:01 em Brasília são 13:01 em Abu Dhabi. Antes do APROVAR, confira o noticiário: se houver acordo, troca de prisioneiros confirmada ou o fim da rodada, ajuste a capa, o slide 9 e a legenda. "Nesta quarta" aparece 4 vezes; no dia da publicação, "hoje" fica mais claro.
- O slug diz 14 nov e a publicação é em 11 nov. Não afeta nada técnico, só a organização.
