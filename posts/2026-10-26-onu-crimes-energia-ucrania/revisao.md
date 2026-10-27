REPROVADO

Revisão rápida, 27 out 2026. Formato notícia, SHA ed69e9c. Falta corrigir 4 pontos, todos rápidos.

| Item | Resultado |
|---|---|
| Fatos: comissão (presidente Erik Møse) conclui crimes de guerra + crimes contra a humanidade, 26 out | ok (OHCHR, ONU News, CNN, AP/US News, Interfax) |
| Fatos: apresentado à Assembleia Geral | ok (a AP fala no comitê de direitos humanos da AG; "à Assembleia Geral" é aceitável) |
| Fatos: 255 pessoas | ok (OHCHR/ONU News: relatos de 255 pessoas em 9 oblasts) |
| Fatos: comissão criada pelo Conselho de Direitos Humanos | ok |
| Isenção: falta o outro lado | PROBLEMA 1 |
| Isenção: "ONU conclui" no título | PROBLEMA 2 |
| Data / tempo verbal / agendamento | PROBLEMA 3 |
| Imagem: licença | ok. CC BY 2.0, autor é usuário do Flickr, não agência. Crédito aparece no card e na legenda. Não consegui abrir a página no Commons (sem rede) |
| Imagem: coerência, violência, data | PROBLEMA 4 (sem data; dá a entender que é de hoje). Não é violenta, não mostra vítima e combina com o tema |
| Texto do card / ortografia | ok |
| Visual (01.jpg): legível, nada cortado, foto colorida, chaminés visíveis acima do texto | ok |
| Legenda sem emoji, ≤ 2.200 caracteres, payload | ok (`metricool.py payload` saiu com rc=0) |

## Correções exatas

1. **Lado russo (isenção).** Acrescentar na legenda, depois do parágrafo "Segundo o órgão, ...":
   "A Rússia não reconhece o mandato da comissão; sua missão na ONU disse que as conclusões se baseiam em dados falsificados."
   (A missão russa na ONU fez essa declaração na segunda, segundo a cobertura da CNN e o resumo do WebSearch. A AP diz que Moscou não respondeu aos pedidos de comentário. Se o roteirista não conseguir confirmar a parte dos "dados falsificados", use só: "A Rússia não reconhece o mandato da comissão.")

2. **Título.** A conclusão é de uma comissão de inquérito, não da ONU como instituição. Trocar `capa.titulo_html` por:
   `Comissão da ONU conclui que ataques russos à <span class="hl2">rede de energia</span> da Ucrânia são crimes de guerra`
   Ajustar também a 1ª frase da legenda para "Uma comissão de inquérito da ONU concluiu ...". O resto pode ficar como está.

3. **Data.** Hoje é 27 out e `agendamento.data_hora` (2026-10-26T23:05) já passou. Trocar "nesta segunda (26)" por "na segunda (26)" no `gancho` e na legenda. Atualizar `agendamento.data_hora` para o horário real de publicação. Depois, renderizar de novo e gerar um novo SHA.

4. **Foto de arquivo.** A foto não tem data (o ID do Flickr, 54201641094, sugere upload em dez 2024, mas não confirmei) e o card dá a entender que é de agora. Trocar o rodapé de crédito para:
   "Foto de arquivo: usina TEC-5, Kiev, após ataque · Estemelmo Nólemë · CC BY 2.0"
   (ou incluir o ano, se o Commons confirmar a data).

Opcional: o box "Crimes apontados: 2" fica vago. Pode virar "Crimes apontados / Guerra e contra a humanidade" sem o número, ou ser mantido.
