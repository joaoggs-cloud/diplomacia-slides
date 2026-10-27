REPROVADO

# Revisão: 2026-10-29-divida-publica (SHA d176514), 27 out 2026

Números conferidos contra a planilha oficial (RTN `seriehistoricajul26.xlsx`, tabela 2.2, coluna 2025; BC SGS 13762) e refeitos no WebSearch. **Os dados estão certos.** A reprovação é por precisão didática (4 pontos), por rótulos que induzem a erro (capa, slides 4 e 9) e pela legibilidade do slide 8. Todas as correções são de texto ou rótulo e não pedem nova pesquisa.

| Item | Situação |
|---|---|
| (a) Mecanismo: títulos, caixa único, regra de ouro, rolagem, Selic e juros | **problema** (slides 2, 5, 7, 8 e legenda) |
| (b) Isenção (sem culpar governo; eleição não citada; Selic como mecanismo) | ok |
| (c) Capa "Quase 29 de cada 100 reais..." | **problema**: o número está certo, mas a frase induz a erro |
| (d) Detentores, indexadores, Tesouro Direto, taxas, DPF R$ 9,29 tri | ok nos números; **problema** na base da pizza do slide 4; taxas: recomendação |
| (e) Pizza do slide 8 contra a planilha | ok nos valores; a soma arredondada dá 99,9% e não há nota |
| (f) Estilo: títulos (2: slides 8 e 9), máx. 45 palavras, sem emoji, sem perguntas | ok (contagem: 40/44/22/37/23/43/10/23) |
| (f) Legibilidade dos gráficos e das legendas das pizzas | ok, exceto o subtítulo do slide 8 (**problema**) |
| (g) Licenças das fotos | ok (CC BY-SA 4.0, CC BY 2.0 e domínio público, com créditos no slide e na legenda). O Commons está bloqueado nesta sessão; vale o metadado da API registrado pelo imagens.py |
| Layout e fotos | recomendação: fotos repetidas, slide 3 sem assunto claro |
| (h) Payload | ok: `metricool.py payload ... --rascunho` rc=0, legenda com 1.455 caracteres (máx. 2.200) |

## Conferências feitas (ok)
- **Slide 8 contra a planilha (tabela 2.2, 2025, R$ mi):** 4.1 Benefícios previdenciários 1.026.872,5. Juros nominais (linha 9) 891.879,9. Transferências por repartição (2) 569.719,3. Pessoal (4.2) 402.553,1. Saúde 170.481,4 + 58.091,4 = 228.572,9. Bolsa Família 158.125,7. BPC 127.236,0. Educação 59.727,6 + 8.532,8 + 32.694,7 = 100.955,1. Abono e seguro 87.843,5. Defesa 14.205,7 + Segurança 3.964,0 = 18.169,6. Demais = 2.394.249,6 − soma = 243.928. Total 3.855.848,8. Todas as fatias e porcentagens batem, e os valores somam 100%. Os rótulos arredondados somam 99,9%.
- **Slide 2:** receita líquida 2.332,6; despesa total 2.394,2; resultado primário −61,7; nominal −950,6. Bate com a planilha.
- **Slide 7 (SGS 13762, dezembro de cada ano):** 74,44 / 86,94 / 77,31 / 71,68 / 73,83 / 76,27 / 78,64; ago/26 82,87. Bate.
- **DPF:** R$ 9.292,73 bi em ago/26 (Jornal do Comércio, Diário do Comércio/Tesouro). Selic 52,74% é recorde desde dez/2000. IPCA 23,22%, prefixados 20,31%, câmbio 3,74%. Duas ou mais fontes.
- **Detentores:** 31,22 / 22,63 / 22,52 / 9,91 (Tribuna PR/RMD e Conof). 9,91% = R$ 886,3 bi, ou seja, **a base é a DPMFi (R$ 8,94 tri), não a DPF**.
- **Tesouro Direto ago/26:** estoque R$ 272,0 bi (Balanço TD ago/26, DGABC, Diário do Comércio). Investidores ativos: 3,83 mi ("quase 4 milhões", Agência Brasil). Ok.
- **Selic 13,75%:** corte de 16 set 2026 (Agência Brasil, Atlas/BCB, 99). Ok.
- **LOA 2026 (Lei 15.346):** OFSS R$ 6.344.718.539.207, refinanciamento R$ 1.822.972.167.477 (texto da lei). 28,73%: "quase 29" está certo **na base OFSS**. Amortização sem refinanciamento: R$ 397,5 bi (parecer CMO), o que confirma o cálculo de 397,1 (diferença de arredondamento).
- **Taxas de 26 out:** Prefixado 2029 fechou em 15,26% (InvestNews, Brasil 247, Mixvale). Selic 2031 em Selic + 0,0992%. IPCA+ 2032 fechou em 7,80% (8,10% na reabertura) e IPCA+ 2050 em ~7,64%.

## Problemas e correção exata

### 1. Capa e 1ª linha da legenda (item c): induz a erro
"29 de cada 100 **reais**... **servem** para rolar" faz o leitor pensar em dinheiro de imposto sendo gasto. Na verdade, a rolagem é paga com dinheiro de títulos novos (troca de dívida por dívida) e o valor é uma dotação, não um gasto. Na base total da LOA (R$ 6,54 tri), a fatia cai para 27,9%. O número fica; muda a forma.
- `capa.titulo_html` →
  `Quase 29% do Orçamento de 2026 é só <span class="hl">rolagem</span>: trocar <span class="hl2">dívida</span> velha por nova`
- Legenda, 1ª linha → `Quase 29% do Orçamento de 2026 é só rolagem da dívida pública: trocar títulos que vencem por títulos novos.`

### 2. Slide 2 (item a): "arrecadou R$ 2,33 tri" está errado
O governo central arrecadou R$ 2,90 tri. R$ 2,33 tri é a receita **líquida**, depois dos repasses a estados e municípios.
- `texto_html` → `Em 2025, o governo central teve receita líquida de R$ 2,33 tri e despesa de R$ 2,39 tri: déficit primário de <strong>R$ 61,7 bi</strong>. Com os juros, o déficit nominal foi de <em>R$ 950,6 bi</em>. Para cobrir a diferença, o Tesouro vende títulos.` (43 palavras)

### 3. Slide 5 (item a): etapa 4 contradiz a regra de ouro
O texto diz que a Constituição não deixa a dívida pagar custeio sem aval do Congresso, mas a etapa 4 lista "Salários, saúde, educação, benefícios" como destino. O principal uso do dinheiro de títulos é pagar títulos que vencem.
- `grafico.itens[3]` → `{"quando": "4. Uso", "texto": "Paga títulos que vencem e demais despesas"}`

### 4. Slide 7 e legenda (item a): relação de causa errada
"Com a Selic ... e metade da dívida atrelada a ela, os juros entram no estoque" dá a entender que os juros só se acumulam por causa da Selic. Juros de todos os títulos se acumulam no estoque. O que a Selic muda é que o custo acompanha a taxa básica. Além disso, "juros nominais **da União**": a linha 9 do RTN é do **governo central** (inclui BC e INSS), o mesmo termo usado no slide 2.
- `texto_html` → `Com a Selic em 13,75% e mais da metade da dívida atrelada a ela, o custo segue a taxa básica, e juros não pagos viram dívida. Em 2025, o governo central teve R$ 891,9 bi de juros. A dívida bruta chegou a 82,9% do PIB.` (45 palavras; o gráfico já mostra 2019 → ago/26)
- Legenda, trecho → `Mais da metade do estoque (52,7% em ago/26, recorde da série) segue a Selic, então o custo da dívida acompanha a taxa básica, e os juros que não são pagos se somam à dívida todo mês.`

### 5. Slide 4 (item d): a base da pizza é a DPMFi, não a dívida federal toda
Os percentuais do RMD são da dívida mobiliária interna: 9,91% = R$ 886,3 bi de R$ 8,94 tri.
- `grafico.titulo` → `Quem detém a dívida interna federal (ago/26)`
- `grafico.nota` → `Fonte: Tesouro Nacional, RMD ago/26. Base: dívida interna em títulos (R$ 8,94 tri). Soma 99,9% por arredondamento.`

### 6. Slide 9 (item a): o rótulo "Juros + amortização" está errado
A amortização total da LOA é R$ 2.220 bi e **inclui** a rolagem. A fatia de R$ 1.041 bi tem só os juros e a amortização **sem** rolagem.
- `grafico.itens[1].rotulo` → `Juros + amortização sem rolagem`
- `texto_html` → `<strong>Rolagem é trocar dívida velha por nova. Somada aos juros e às demais amortizações, chega a 45,1% do Orçamento de 2026, que é dotação aprovada, não gasto.</strong>`

### 7. Slide 8 (itens a, e, f): subtítulo ilegível, juros sem explicação e soma 99,9%
- O subtítulo em negrito ("Execução de 2025, em R$ bi...") fica ilegível sobre os prédios da Esplanada. Use `"foco": "center 100%"` ou troque a foto por uma com céu atrás do título (img04, foco "center 0%", ou img06). Depois de renderizar, confira se o subtítulo está legível.
- Juros nominais seguem o critério de competência do BC: são devidos no ano, mas não são todo o dinheiro que saiu do caixa. Na pizza "para onde foi o dinheiro", isso precisa estar dito.
- `grafico.nota` → `Salários de professores, médicos e militares estão em “Servidores”. *Defesa e segurança: só discricionárias. Juros: devidos no ano (BC), parte paga, parte somada à dívida. Soma 99,9% por arredondamento.`
- `texto_html` → `<strong>Despesas de 2025, em R$ bi. Fonte: Tesouro Nacional (RTN) e Banco Central.</strong>`

## Recomendações (não bloqueiam)
- **Slide 6 (precisão):** `No vencimento, o Tesouro paga o valor com juros, em geral com o dinheiro de títulos novos: é a rolagem. Mais da metade da dívida já segue a Selic.` (29 palavras). Hoje "paga ... e rola" parece descrever duas coisas que acontecem sempre juntas.
- **Slide 3 (taxas):** use uma única data e números de fechamento: `O Tesouro Selic segue a taxa básica (Selic + 0,10% no de 2031). O Prefixado trava a taxa (cerca de 15,3% no de 2029). O IPCA+ soma inflação e taxa (de 7,6% a 7,8% nos de 2032 a 2050). Dados de 26 out.` (43 palavras). "Perto de 8%" só vale para a reabertura do IPCA+ 2032. Confira de novo na manhã de 28 out, antes de pedir aprovação.
- **Fotos repetidas:** img02 aparece 3 vezes com o mesmo enquadramento (slides 2, 6 e 8). img01 é igual na capa e no slide 9. img05 aparece nos slides 5 e 7. img06 (Planalto, domínio público) não é usada. Sugestão: slide 6 → `img06`; slide 9 → `img01` com `"foco": "center 80%"` ou img04. A img02 tem baixa resolução e sai granulada.
- **Slide 3:** a foto (viga escura contra o céu) não tem assunto reconhecível. Se der, troque por um prédio do Ministério da Fazenda (Bloco P da Esplanada) ou pela img06.
- **Legenda:** corte "O mecanismo é simples." (frase-feita).
