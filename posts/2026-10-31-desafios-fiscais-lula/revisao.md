REPROVADO

Revisão de `posts/2026-10-31-desafios-fiscais-lula` (SHA e00b9f7) · revisor · 27 out 2026

| Item | Resultado |
|---|---|
| 1. Fatos | problema (Oreiro fora de contexto; FMI sem edição; fonte secundária do Copom; Lei 15.270 sem "por mês/por ano") |
| 2. Isenção | problema (contraponto é editorial de opinião; a posição do próprio Lula/governo sobre a dívida não aparece; crédito "Michel Temer") |
| 3. Imagens | problema (licenças ok; slide 3 quase só céu e foto de 800 px; slide 8 repete a foto do slide 4) |
| 4. Texto | problema (slide 6 com 55 palavras, limite 45) |
| 5. Visual | problema (slide 4: barra observada sobe por causa do rótulo de 2 linhas) |
| 6. Legenda | ok no tamanho (1.611 caracteres com fontes e créditos; o payload roda sem erro). Problema: remete ao post de 29 out, que ainda não existe |

## O que conferi e está ok
- DBGG em 82,9% do PIB (R$ 11,055 tri) em ago/2026: BC, 30 set (Poder360, Jornal do Comércio, Gazeta do Povo). **Setembro ainda não saiu.** Deve sair entre 29 e 30 out: conferir na véspera e trocar o número se sair antes de 31 out 06:01. Pelo critério do FMI, a mesma DBGG foi de 94,5% em agosto.
- Selic: corte de 14,00% para 13,75% em 16 set, decisão unânime, quinto corte seguido (CNN Brasil, InfoMoney, DGABC). Uma manchete fala em "4º corte", mas a sequência dos comunicados confirma o 5º.
- Metas de primário: 0,5 (2027), 1,0 (2028), 1,25 (2029) e 1,5 (2030) no PLDO 2027 (IstoÉ Dinheiro, Poder360, nota técnica conjunta do Congresso). O Congresso em Foco dá 1,3 para 2029, mas é a fonte isolada. **A LDO 2027 ainda não foi votada.**
- IFI: dívida de 82,5% em 2026 e 86,4% em 2027, e déficit primário de R$ 86,1 bi em 2027 contra superávit de R$ 18,6 bi no PLOA (Poder360, Terra, página da IFI). A cobertura é de set/out e trata da análise do PLOA 2027, posterior ao RAF 113, de junho.
- FMI: 100% do PIB em 2027 vem do Monitor Fiscal de **abril de 2026** (Exame, Forbes). A edição de outubro manteve 96,5% para 2026, e não achei o número de 2027 dela. A diferença de metodologia (títulos do Tesouro na carteira do BC) está confirmada.
- Durigan, 26 out: quer ampliar o superávit de 2027 e mudar a lei, ou a Constituição, para mirar o centro da meta (Poder360 em duas matérias, SpaceMoney). Ok.
- Discurso da vitória sem tema fiscal: PlatôBR/EM e BM&C. Não achei a íntegra, mas as duas fontes são independentes. Ok.
- PL com 121 de 513 deputados: Exame, Correio da Manhã, Jornal do Comércio. Ok.
- Salto e Pellegrini, plano de 3 a 4 anos: segunda fonte é o Times Brasil. Ok.
- Sbardelotto (XP): PlatôBR e Jornal de Brasília. Mas veja o problema F2.
- Lei 15.270/2025: isenção até R$ 5 mil por mês e imposto mínimo para rendas acima de R$ 600 mil por ano, que chega a 10% acima de R$ 1,2 mi (Senado, DIEESE). Veja F4.
- Estilo: sem título nem tag nos slides de conteúdo, 1 factbox, sem emoji, sem pergunta ao leitor, `primeiro_comentario` vazio. Ok.
- Licenças: todas CC BY 2.0 ou CC BY-SA 4.0, com crédito no slide e na legenda. Fotos coloridas, sem violência e sem pessoas identificáveis.
- Gráficos: as barras partem do zero (`render.py`: altura = valor/máximo), e a barra observada tem cor diferente das projeções.

## Problemas e correções exatas

**F1. Slide 8: Oreiro fora de contexto (grave).** A crítica de José Luis Oreiro ("o ajuste recairia sobre os mais pobres") foi feita ao plano da campanha de Flávio Bolsonaro, o "tesouraço" (Brasil de Fato, 8 out; Brasil 247; o Substack do próprio Oreiro). Ela não fala das opções do governo eleito. Do jeito que está, o slide atribui a ele uma crítica que não fez. Além disso, a fonte nem está em `fontes`.
→ Tire a frase sobre Oreiro. Texto sugerido para o slide 8, com 45 palavras:
"Economistas debatem outras frentes. Tiago Sbardelotto, da XP, calcula que, com teto de 1,5%, a regra exigiria rever os pisos de saúde e educação em 2028. Salto e Pellegrini, no Estadão, propõem ajuste gradual em 3 a 4 anos, sem corte brusco, que seria recessivo."
Acrescente em `fontes` o PlatôBR (https://platobr.com.br/como-uma-reducao-das-despesas-impactara-as-contas-publicas-a-xp-fez-esse-calculo) e o Times Brasil (https://timesbrasil.com.br/brasil/ajuste-fiscal-deveria-ser-anunciado-apos-eleicao-e-diluido-em-ate-4-anos-diz-felipe-salto/).

**F2. Sbardelotto "defende rever os pisos".** As fontes dizem que ele projeta que, com teto de 1,5%, a regra entra em colapso em 2028 e exige reformas maiores, entre elas desvincular os pisos. Isso é cálculo, não bandeira. A redação de F1 ("calcula que… exigiria") já resolve.

**I1. Isenção: o contraponto é só de um lado, e é editorial.** O factbox usa um editorial da Gazeta do Povo, que é opinião. Não consegui confirmar o texto pela busca. Como o post já tira Oreiro, sobram só críticas pelo lado fiscalista, e a tese do próprio governo sobre a dívida não aparece.
→ (a) Troque o factbox do slide 7 por uma avaliação técnica e atribuída:
`"factbox": {"label": "IFI", "texto": "A IFI, do Senado, considera otimistas as premissas do governo: projeta déficit primário de R$ 86,1 bi em 2027, contra superávit de R$ 18,6 bi previsto no Orçamento."}`
Em `fontes`, troque a Gazeta do Povo (editorial) por "Poder360: IFI projeta déficit de R$ 86,1 bi em 2027" (https://www.poder360.com.br/poder-economia/instituicao-fiscal-independente-projeta-deficit-de-r-861-bi-em-2027/).
→ (b) Ponha no slide 6 a posição de Lula, que foi dita na Band em 27 set e confirmada por Band, Poder360 e Diário de Pernambuco. Texto sugerido para o slide 6, com 44 palavras, o que resolve também T1:
"Lula não tratou de ajuste fiscal no discurso da vitória, em 25 out. Em setembro, disse que o melhor caminho para reduzir a dívida é fazer a economia crescer. Em 26 out, o ministro da Fazenda, <strong>Dario Durigan</strong>, prometeu ampliar o superávit de 2027."
Em `fontes`, acrescente a Band (https://www.band.com.br/politica/divida-publica-nao-me-causa-panico-e-irreal-diz-lula). Se quiser manter "mudar a lei ou a Constituição para mirar o centro da meta", ponha a frase no começo do slide 7 e corte em outro ponto para ficar em até 45 palavras.
→ (c) Na legenda, troque "cada uma atribuída a quem a defende e com o contraponto" por "cada uma atribuída a quem a defende, com a avaliação da IFI".

**F3. FMI sem edição, e fonte do Copom secundária.**
→ Slide 4, `grafico.nota`: "Projeções, exceto ago/2026. *FMI, Monitor Fiscal de abr/2026: inclui títulos na carteira do BC".
→ Em `fontes`, troque "Banco Central: Copom (via Atlas Público)" por "CNN Brasil: Copom corta a Selic para 13,75%" (https://www.cnnbrasil.com.br/economia/money/macroeconomia/bc-copom-selic-juros-setembro-2026/).
→ Troque também "IFI (Senado): RAF 113" (junho) pela matéria do Poder360 sobre a IFI citada em I1, ou pelo link https://www12.senado.leg.br/ifi.

**F4. Slide 9: Lei 15.270 sem "por mês" e "por ano".** Troque por: "Na receita, a Lei 15.270/2025 isenta quem ganha até R$ 5 mil por mês e cobra imposto mínimo de até 10% sobre rendas acima de R$ 600 mil por ano; não houve anúncio novo." Ajuste o resto da frase para não passar de 45 palavras. Por exemplo: "Mudar a regra fiscal depende do Congresso, onde o PL terá a maior bancada da Câmara: 121 de 513."

**F5. Slide 3: "No resultado primário, 2025 fechou…"** Precisa dizer de quem é o resultado. Troque por "O governo central fechou 2025 com déficit primário de R$ 13 bi na conta da meta…". Na nota do gráfico, troque por "Banda de ±0,25 p.p. em 2026 e 2027. Metas de 2027 a 2030 constam do PLDO 2027, ainda em votação", porque a LDO 2027 não foi aprovada.

**T1. Slide 6 tem 55 palavras; o limite do layout moderno é 45.** O texto de I1(b) resolve.

**V1. Slide 4, gráfico:** o rótulo "Ago/2026 (observado)" quebra em 2 linhas e sobe a base da primeira barra. Com isso, o topo da barra de 82,9% fica na mesma altura do topo da de 100%, e a leitura engana.
→ Troque o `rotulo` para "Ago/2026". A nota já diz que esse é o único dado observado e a cor já marca a diferença. Depois de renderizar, confira se as 4 barras ficam na mesma linha de base.

**V2. Slide 3, foto:** img03 (`Palacio do Planalto (5348220087).jpg`, 800×533 px) aparece quase só como céu azul. O Planalto fica escondido atrás do texto e do degradê, e a resolução é baixa.
→ Troque por `File:Esplanada dos Ministérios - 50494085438.jpg` (já está nas alternativas da img04) ou por uma foto do Ministério da Fazenda (`incategory:"Esplanada dos Ministérios, Bloco P (Brasília)"`), com o prédio na metade de cima.

**V3. Slide 8 repete a img04, a mesma vista da Esplanada do slide 4,** com outro enquadramento.
→ Use outra foto, por exemplo a do Ministério da Fazenda (bloco P) ou `File:Esplanada dos Ministérios - 50494849186.jpg`, e mantenha a da V2 diferente desta.

**I2. Crédito "Foto: Michel Temer" no slide 6,** que fala de Lula. É o nome da conta oficial do Planalto no Flickr da época, mas fora de contexto pode parecer recado político.
→ Troque a img06 por outra foto do Planalto de autor institucional, como Senado Federal ou Agência Brasil. Uma opção é usar `File:Fachada do Palácio do Planalto - 49727772326.jpg` com outro foco, ou buscar em `incategory:"Palácio do Planalto"` uma foto da Agência Brasil.

**L1. Legenda: "Continuação do post sobre dívida pública de 29 de outubro."** O post `2026-10-29-divida-publica` só tem `pauta.md`, sem `post.json` nem aprovação.
→ Tire a frase, ou mantenha só se o post de 29 out estiver `agendado` antes de este ir para aprovação.

**D1. Dados que vencem antes de 31 out.** A DBGG de setembro sai entre 29 e 30 out. Se sair, atualize o slide 2, a capa e a legenda (valor, mês e série), ou acrescente "último dado disponível em 30 out". Confira também se houve fala nova de Lula sobre o fiscal entre 27 e 30 out: se houver, o slide 6 ("não tratou") fica incompleto.

Opcional, não bloqueia: os gráficos de número dos slides 2 e 5 só repetem o número que já está no texto. Dá para tirar ou trocar por um dado complementar, como "Critério FMI: 94,5% do PIB" no slide 2.

## Fontes da verificação
- https://www.poder360.com.br/poder-economia/divida-bruta-atinge-829-do-pib-em-agosto-diz-banco-central/
- https://www.jornaldocomercio.com/economia/2026/09/1265225-divida-bruta-do-governo-geral-sobe-para-829-do-pib-em-agosto-mostra-bc.html
- https://www.cnnbrasil.com.br/economia/money/macroeconomia/bc-copom-selic-juros-setembro-2026/
- https://www.infomoney.com.br/economia/taxa-selic-copom-corta-juros-13-75-set-2026/
- https://exame.com/economia/divida-do-brasil-pode-chegar-a-100-do-pib-em-2027-diz-fmi/
- https://forbes.com.br/forbes-money/2026/04/divida-a-100-do-pib-o-alerta-do-fmi-e-o-impacto-nos-investimentos-no-brasil/
- https://www.poder360.com.br/poder-economia/instituicao-fiscal-independente-projeta-deficit-de-r-861-bi-em-2027/
- https://istoedinheiro.com.br/pldo-fixa-meta-de-superavit-primario-de-050-do-pib-para-2027-com-banda-de-025-pp
- https://www.poder360.com.br/poder-economia/durigan-quer-mudar-constituicao-para-cumprir-centro-da-meta-fiscal/
- https://bmcnews.com.br/economia/lula-venceu-a-economia-sera-seu-calcanhar-de-aquiles/
- https://exame.com/brasil/pl-amplia-bancada-e-tera-121-deputados-veja-a-nova-composicao-da-camara/
- https://www.brasil247.com/entrevistas/jose-luis-oreiro-destrincha-plano-de-flavio-bolsonaro-terra-arrasada-contra-os-mais-pobres-e-entrega-de-patrimonio-publico/
- https://platobr.com.br/como-uma-reducao-das-despesas-impactara-as-contas-publicas-a-xp-fez-esse-calculo
- https://timesbrasil.com.br/brasil/ajuste-fiscal-deveria-ser-anunciado-apos-eleicao-e-diluido-em-ate-4-anos-diz-felipe-salto/
- https://www.band.com.br/politica/divida-publica-nao-me-causa-panico-e-irreal-diz-lula
- https://www.diariodepernambuco.com.br/politica/2026/09/11725085-lula-cita-reservas-internacionais-e-diz-que-divida-publica-nao-lhe-provoca-panico.html
