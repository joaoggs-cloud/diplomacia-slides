APROVADO (coordenador, 14 nov 2026, rodada 2), no SHA 27167695074f1998264505258999f5c20186653f.

Os itens 1 a 10 da rodada 1 foram aplicados pelo roteirista.

O coordenador:
- incluiu o corte da primeira chapa (jun 2024, Itaguaí) no slide 5 e na legenda;
- conferiu os slides em montagem (capa nova, S41 no slide 8, Gripen no slide 9, factbox no slide 5).

Story e Reel foram regerados.

--- Rodada 1 ---

REPROVADO

Revisão de `posts/2026-11-16-brasil-submarino-gripen` no SHA 8636b6b (revisor, 14 nov 2026).

| Item | Resultado |
|---|---|
| 1. Fatos | problema: "só começou em 20 out", "2037 ou 2038", quilha 2027, AIEA e "7 nov" |
| 2. Isenção e tom | ok (nem ufanista nem desdenhoso) |
| 3. Imagens: licenças | ok (CC BY 2.0 / CC BY-SA 2.0 / CC BY-SA 4.0) |
| 3. Imagens: coerência | problema: capa (mão), slides 5, 7 e 8 |
| 4. Texto | ok: ≤45 palavras, 2 títulos, 1 factbox, sem emoji nem pergunta |
| 5. Visual | problema: crédito cortado nos slides 3 e na cena 03 do Reel |
| 6. Legenda | ok no tamanho (1.543 caracteres), mas tem os mesmos erros de fato do item 1 |
| 7. Reel | problema: cenas 02, 04 e 05 (foto e fato); 6 frases ≤18 palavras e legíveis; legenda do Reel com 1.003 caracteres, ok |
| Story | refazer depois da troca da capa |

## Fatos conferidos por conta própria
- 25 mar 2026, Gavião Peixoto, Embraer + Saab + FAB: **ok** (Poder Aéreo, IstoÉ Dinheiro, Tecnodefesa).
- "Primeiro da América Latina a produzir jatos supersônicos": **ok**, atribuído à Pesquisa FAPESP (ed. 363) e repetido por Movimento Econômico e Xataka.
- 15 dos 36 com montagem final na Embraer: **ok** (FAPESP, Tecnodefesa).
- 20 out 2026, Cherbourg, componente do casco: **ok** (Defesa em Foco, Zona Militar, Militarnyi).
- Reator brasileiro, LABGENE em Aramar/Iperó, França sem transferência: **ok** e atribuído (Sociedade Militar, Pesquisa FAPESP, GBN, Jornal Cruzeiro).
- Armamento convencional: **ok**. O nome oficial da Marinha é "Submarino Nuclear Convencionalmente Armado".
- **ERRADO: "começou a ser fabricado só em 20 out" e "é o começo da obra".** A Marinha cortou a primeira chapa do casco em 12 jun 2024, em Itaguaí (marinha.mil.br/prosub, DefesaNet, Defesa Aérea & Naval). A Nuclep entregou uma seção do casco em set 2026 (Sociedade Militar). O 20 out foi um marco na França, não o início da obra.
- **Lançamento: é 2038, não "2037 ou 2038".** Ofício do Ministério da Defesa à Câmara, jun 2026, de 2034 para 2038, por falta de recursos e de previsibilidade orçamentária (Poder Naval 8 jul, Metrópoles, Zona Militar 13 jul). O 2037 é de tabela antiga da Wikipedia.
- **Sem 2ª fonte: quilha "2027", "testes do reator e negociação com a AIEA" como motivos do atraso, e o alerta da Marinha "em 7 nov"** (só Sociedade Militar, que cita o Estadão, sem data confirmada). Corte.

## Correções exatas (post.json)

1. **capa.imagem**: `img01` → `img03`. A foto da janela é vertical, mostra o jato inteiro e é colorida. A mão desfocada da img01 ocupa 1/3 da capa e, no recorte 4:5, sobram dois dedos que parecem um gesto (V). Não serve para a capa. Autor da img03: `"Palácio do Planalto"`, porque hoje o crédito sai cortado em "Brasilia, Bra...".
2. **capa.gancho**: `"Uma das duas coisas já voa. A outra ainda está no começo da obra."`
3. **Slide 3** (`imagens[img03]` vira a capa): use `"imagem": "img01", "foco": "85% 50%"` e confira se a mão sumiu do recorte. Se ainda aparecer, use `img02` com `"foco": "15% 50%"`.
4. **Slide 5** `texto_html`: `"O <strong>Álvaro Alberto</strong>, do PROSUB, ainda está no começo da construção. Em 20 out 2026, em Cherbourg, na França, uma cerimônia marcou o início da fabricação de um componente do casco. Navio pronto, ainda não há."`
   Mova o factbox do slide 8 para cá: `{"label": "Na foto", "texto": "o Riachuelo, submarino convencional do PROSUB, em construção em Itaguaí (RJ)."}`. Sem isso, a foto passa por Álvaro Alberto.
5. **Slide 7**: troque `img09`. É o diretor da AIEA, de máscara, num helicóptero: pessoa identificável, sem ligação com o texto e sem Aramar à vista. Use `img05` (Riachuelo atracado em Itaguaí). Novo `texto_html`: `"O cronograma é longo. Em junho, o Ministério da Defesa informou à Câmara que o lançamento passou de 2034 para <strong>2038</strong>, por falta de recursos e de previsibilidade no orçamento."`
6. **Slide 8**: tire o factbox. A img07 é uma plateia sob uma tenda e não mostra submarino nenhum, então o "Na foto: submarino convencional" está falso. Troque a foto por uma em que apareça um submarino Riachuelo ou Humaitá (`scripts/imagens.py posts/<slug> --so img07` com query do Commons do S41 Humaitá ou do S40 Riachuelo). Novo `texto_html`: `"Propulsão nuclear não é arma nuclear. O nome oficial já diz: Submarino Nuclear Convencionalmente Armado. O reator move o navio, e o armamento será convencional, segundo o Ministério da Defesa."`
7. **Slide 9**: hoje usa `img05`, que passa para o slide 7. Use uma foto nova de Gripen da FAB (`--so img09`, query `incategory:"Saab JAS 39 Gripen of the Brazilian Air Force"`) ou outra foto colorida que ainda não esteja no post.
8. **legenda**, troque a frase do submarino por: `"Já o submarino Álvaro Alberto está no começo da construção: em 20 out, em Cherbourg, na França, começou a fabricação de um componente do casco, e o lançamento foi reprogramado para 2038 por falta de recursos."` O resto do parágrafo fica. Última linha: `"As fotos de submarino mostram convencionais da classe Riachuelo."`
9. **fontes**: tire "Sociedade Militar, out 2026: primeiro voo" e "Sociedade Militar, jul 2026: 20 Gripens adicionais", que não estão no post. Inclua Poder Naval, 8 jul 2026 (https://www.naval.com.br/blog/2026/07/08/submarino-nuclear-alvaro-alberto-tem-lancamento-reprogramado-para-2038/), Metrópoles (https://www.metropoles.com/colunas/grande-angular/marinha-adia-lancamento-do-submarino-nuclear-para-2038) e Poder Aéreo, 25 mar 2026 (https://www.aereo.jor.br/2026/03/25/embraer-saab-e-a-forca-aerea-brasileira-apresentam-primeiro-caca-gripen-produzido-no-brasil/).
10. **Reel, cena 1** (`img01`): troque por `img03`, pelo mesmo motivo da capa.
11. **Reel, cena 4**: troque `img08` por `img06`, porque o Riachuelo em construção, sem legenda e com "na França", passa por Álvaro Alberto. Texto, com 18 palavras: `"O <em>Álvaro Alberto</em> está no começo da obra. Em 20 out, na França, começou uma peça do casco."`
12. **Reel, cena 5**: troque `img06` por `img05`. Texto, com 17 palavras: `"O reator é brasileiro. O nuclear só vai ao mar em <em>2038</em>; o da foto é convencional."`
13. Renderize de novo os slides, o `story.py` (a capa muda) e o `reel.py`. Na cena 03 do Reel, o crédito sai cortado em "Brasilia, Bra..."; o item 1 resolve. Detalhe, sem bloquear: o crédito nas cenas fica em y≈1550 de 1920, perto da faixa de legenda do Instagram.

Sem bloquear: a foto do slide 4 (visita do ministro a Gavião Peixoto) é provavelmente anterior à linha do Gripen, de 2023. Sem legenda, passa como "fábrica da Embraer". Se houver foto da linha do Gripen, prefira.
