REPROVADO

# Revisão: 2026-11-10-lasers-antidrone (SHA 6e82d3c)

| Item | Resultado |
|---|---|
| Fatos: £316 mi, MBDA UK, Type 45 em 2027, "cinco anos antes" | ok (GOV.UK, Register, Janes, Marine Insight) |
| Fatos: £10 por tiro, estimativa oficial | ok |
| Fatos: moeda de £1 a 1 km, Hébridas | ok (GOV.UK, STV) |
| Fatos: Iron Beam entregue em 28 dez 2025, 100 kW | ok (Globes, Defense Post) |
| Fatos: alcance do Iron Beam "7 a 10 km" | problema: o 7 km só aparece em fontes secundárias fracas (Thairath, SEA Asia); Globes diz cerca de 10 km |
| Fatos: LOCUST 20 kW AMP-HEL, JLTV, Mar-a-Lago em 31 out, sem disparo confirmado | ok (TWZ, Jerusalem Post, DroneXL; NORAD confirmou a TWZ; as fotos de 31 out são de Andrew Harnik/Getty e nenhuma fonte confirma interceptação) |
| Fatos: El Paso em 10 fev 2026, fontes divergem sobre o alvo | ok |
| Fatos: El Paso "menos de 8 horas" | problema: as fontes divergem (Flightradar24 diz 7 h 24; outros veículos falam em cerca de 8 h ou mais de 9 h) |
| Capa: "míssil de US$ 100 mil" | problema: nenhum míssil é nomeado, e o número não está nas fontes. Contradiz o slide 3 ("centenas de milhares de libras") e a legenda ("dezenas de milhares de dólares") |
| Isenção (Mar-a-Lago) | ok: texto técnico, sem nome nem opinião. A foto do slide 4 vem de um evento político (Hegseth "Drone Dominance"); será trocada no item 4 |
| Licenças | ok: só domínio público e CC BY 2.0, nenhuma foto de agência |
| Créditos | ok nos slides e na legenda |
| Coerência foto–texto | problema nos slides 3, 4, 5 e 7 (ver abaixo). Capa (LaWS dos EUA), slide 2 (HMS Daring, que é um Type 45), slide 8 (El Paso) e slide 9: aceitáveis |
| Cor | problema: slide 3 em P&B sem `pb: true` nem justificativa |
| Texto e "cara de IA" | 2 títulos e 1 factbox (ok); todos os slides com ≤ 45 palavras. Problema: o título "O limite do feixe" é seguido de "O feixe tem limites." |
| Visual | ok: nada cortado, numeração 2/10 a 10/10 certa, texto legível |
| Legenda | ok: 1.001 caracteres, sem emoji, sem pergunta. Primeira linha a corrigir (item 1) |
| Story | ok, mas precisa ser refeito depois da troca da capa |

## Correções obrigatórias

1. **Capa e legenda (valor do míssil).** Em `capa.titulo_html`, troque por:
   `Um tiro de <span class="hl">US$ 13</span> contra mísseis de <span class="hl2">centenas de milhares</span>`
   Na legenda, troque a 2ª frase por: "Um míssil interceptor tradicional custa centenas de milhares de libras."
   Assim a capa, o slide 3 e a legenda dizem a mesma coisa que a fonte britânica.
2. **Slide 5 (Iron Dome no lugar do Iron Beam).** Engana o leitor. Rode `scripts/imagens.py posts/<slug> --so img05` com `"query": "File:Iron Beam, October 2024 (cropped).jpeg"` (Ministério da Defesa de Israel, CC BY-SA 4.0 ou PD). Se o filtro recusar, mantenha a foto e troque o texto por:
   "Em Israel, o <strong>Iron Beam</strong>, laser de 100 kW que reforça o Iron Dome (na foto), foi entregue às Forças de Defesa em 28 dez 2025. A Rafael e o Ministério da Defesa o apresentam como o primeiro laser de alta potência em serviço operacional regular."
3. **Slide 3 (HELIOS americano, em P&B, sob texto do DragonFire).** O leitor entende que a foto mostra o DragonFire disparando de um navio, e ele ainda não está embarcado. Troque img03 por `File:Dragonfire laser system test firing.webp` se a licença passar (OGL equivale a Attribution). Senão, use uma foto colorida de um Type 45 (`incategory:"Type 45 destroyers"`, sem repetir a do slide 2).
4. **Slide 4 (drones americanos de um evento do Hegseth sob texto dos testes britânicos).** Bandeiras dos EUA num slide sobre testes britânicos, e a foto vem de um evento político. Troque img04 por um drone-alvo britânico (`Banshee target drone`, alternativa `incategory:"Meggitt Banshee"`) ou pela área de testes (`Hebrides Range South Uist`, alternativa `incategory:"South Uist"`). A foto tem de ser colorida.
5. **Slide 7 (JLTV comum sem laser).** Do jeito que está, o leitor entende que é o veículo de Mar-a-Lago. Tente img07 = `File:US Army HEL-TVD (laser).jpg` ou `incategory:"Locust Laser Weapon System"`. Se mantiver o JLTV, troque o texto por:
   "Nos EUA, o <strong>LOCUST</strong>, da AeroVironment, é um laser de classe 20 kW do programa AMP-HEL do Exército, voltado a drones pequenos. Em 31 out, um deles, montado num JLTV (como o da foto, sem o laser), foi fotografado em Mar-a-Lago; não há disparo confirmado."
6. **Slide 6 (alcance e repetição).** Troque `texto_html` por:
   "O alcance do Iron Beam é estimado em cerca de 10 km, e neblina, nuvem, poeira e chuva forte reduzem sua eficácia. Por isso ele complementa o Iron Dome, e não o substitui."
7. **Slide 8 (duração).** Troque "e suspendeu a restrição em menos de 8 horas" por "e suspendeu a restrição horas depois, na manhã seguinte".
8. **Slide 9 (frase pouco clara).** Troque "A economia vem dos tiros baratos, não do sistema." por "O tiro é barato; o sistema, não."
9. Depois das trocas, renderize de novo, refaça o Story (`scripts/story.py`) e confira se os créditos das fotos novas aparecem (as CC BY-SA levam autor e licença).
