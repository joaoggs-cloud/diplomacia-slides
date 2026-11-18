# APROVADO (coordenador, rodada 2, 18 nov): correções 1–6 aplicadas; slides relidos. Reconferir tráfego/reparo em 20 nov.

REPROVADO

# Revisão: 2026-11-21-ponte-da-crimeia (revisor, 18 nov 2026)

| Item | Resultado |
|---|---|
| 1. Ataques de 16 e 17 nov, vão caído (Estado-Maior/SBU), NBC | ok (Ukrinform, PBS, TWZ, The Insider confirmam: arco e vão rodoviário caíram no ataque da noite de 16 para 17 nov) |
| 2. Versão russa (Ministério dos Transportes / Peskov) | **problema**: atribuição do "dano pequeno" e tráfego desatualizado (slide 3 e legenda) |
| 3. Zelensky "sem precedentes", "sétima fase" | ok (Kyiv Independent, Ukrainska Pravda, NV) |
| 4. Armas (AP) | **problema**: "golpe final" não confirmado (slide 5) |
| 5. ISW | ok com ressalva: só CNBC na pauta; os resumos do ISW no Kyiv Post vão na mesma linha. Pode ficar porque está atribuído |
| 6. Inauguração 15 mai 2018, Kamaz, 19 km, condenações | ok |
| 7. Ataques anteriores (2022, 2023, 2025) | ok; sugestão de atribuição em 2022 (opcional) |
| 8. Pontes de Kiev, 7 mísseis, 2 mortos | ok com ressalva: o número de mísseis é de Zelensky ("segundo a Ucrânia" já está no texto); as mortes em Obolonskyi não estão ligadas às pontes |
| 9. Fato novo até 18 nov | **problema**: os trens voltaram a circular (Ministério dos Transportes via Interfax; Aksyonov); a pista segue fechada; Peskov: "sem dúvida a ponte será restaurada", "ainda melhor que antes" |
| 10a. Licenças e créditos | ok (CC BY-SA 4.0 / 3.0 / 3.0 IGO, CC0; créditos no slide e na legenda) |
| 10b. Fotos repetidas | **problema**: img01 na capa e no slide 4, img06 nos slides 2 e 7, img02 nos slides 3 e 8 (3 de 6 fotos repetidas, mesmo enquadramento) |
| 10c. Isenção | ok no geral; a capa pede ajuste (ver abaixo) |
| 10d. Regras (emoji, pergunta, título/factbox, hashtags) | ok: sem emoji, sem pergunta, 0 título, 1 factbox, 6 hashtags específicas, primeiro comentário vazio |
| Texto (≤45 palavras) | ok: 44/40/29/29/44/35/36/39 |
| Legenda (≤2.200) | ok: 1.168 caracteres no payload |
| Visual | ok: nada cortado, numeração 2/10 a 10/10 certa, texto legível, fotos coloridas; a capa tem foto com neblina, mas aceitável |
| Story | ok: capa centralizada, sem texto extra |
| Reel | não se aplica (`gerar: false`) |

## Correções obrigatórias

1. **Slide 3 (2º de conteúdo): atribuição de Peskov e tráfego.** Peskov chamou de "pequeno" o dano do **primeiro** ataque (16 nov, Meduza e Military.com). Depois do segundo ataque, ele prometeu reconstruir a ponte ("ainda melhor que antes", Kyiv Post 90352). E os trens já voltaram a circular, só a pista segue fechada. Texto novo (45 palavras):
   > Moscou dá outra medida. O Ministério dos Transportes confirmou dano por drones, sem vítimas: a pista segue fechada, mas os trens voltaram. Peskov, que antes chamou de pequeno o dano de 16 nov, promete reconstruir. A extensão do estrago não foi verificada de forma independente.

   Fontes novas em `fontes`: Kyiv Independent, "New video shows damage to Crimean Bridge as train traffic resumes" (https://kyivindependent.com/new-video-shows-damage-to-crimean-bridge-as-train-traffic-resumes/), e Meduza, 16 nov (https://meduza.io/en/feature/2026/11/16/ukrainian-drone-attack-damages-crimea-bridge-shutting-down-road-traffic-for-hours-kremlin-says-damage-is-minor).

2. **Legenda.** Troque "Moscou confirma dano por drones e suspensão do tráfego, sem vítimas, e fala em reparo." por:
   > Moscou confirma dano por drones, sem vítimas; a pista segue fechada, os trens voltaram a circular e o Kremlin promete reconstruir a ponte.

3. **Slide 5 (4º de conteúdo): armas.** Não consegui confirmar "golpe final" (a AP/ABC não abre nesta sessão). As outras fontes, que citam Zelensky (Ukrainska Pravda, NV, Kyiv Independent), falam em Palianytsia na pista, Neptune e drones na ferrovia e Flamingo em "ataques de precisão". Se o roteirista não achar a frase no texto da AP, use (33 palavras):
   > Zelensky detalhou as armas: drones-mísseis ucranianos Palianytsia atingiram a pista, mísseis Neptune e outros drones miraram a ferrovia, e mísseis Flamingo fizeram ataques de precisão. Nada disso foi confirmado por fonte independente.

4. **Capa: título.** "Moscou, em dano" soa truncado e a oposição ficou desatualizada, porque Moscou agora promete reconstruir. Novo `titulo_html`:
   > `<span class="hl">A ponte que Putin abriu em 2018</span> foi atingida duas noites seguidas. Kiev diz que um vão caiu; Moscou promete reconstruir`

   O gancho pode ficar como está.

5. **Fotos repetidas.** A capa e o slide 4 usam a mesma img01, e os slides 2 e 7 repetem a img06 com o mesmo corte:
   - Slide 7 (inauguração): troque por uma foto oficial da abertura, com o assunto da frase. Use `"query": "incategory:\"Opening of the Crimean Bridge\""` (fotos do kremlin.ru, CC BY 4.0), de preferência o Kamaz na ponte.
   - Slide 4 (Zelensky): troque a img01 por outra foto da ponte, por exemplo `File:Kerch Strait Bridge, 2018-04-14.jpg` (satélite, já sugerida na pauta) ou uma de `incategory:"Crimean Bridge in 2021"`. Também dá para usar a img06 aqui e tirá-la do 7.
   - Slide 8: a repetição da img02 é tolerável, mas é melhor usar outra foto da mesma categoria, se houver.

## Recomendadas (não bloqueiam)

- **Slide 9:** para não ligar as mortes às pontes, troque a última frase por "O Serviço de Emergência ucraniano relatou **dois mortos** em Obolonskyi, no ataque à capital." (fica em ~40 palavras).
- **Slide 8:** "Em 8 out 2022, um caminhão-bomba destruiu dois vãos rodoviários, ataque que o SBU só assumiu em 2023." Use só se achar 2 fontes da admissão de Maliuk (ago 2023); se não achar, deixe como está, que o texto atual é correto.
- **Slide 2:** "Em 16 e 17 nov ... dois dias seguidos" é redundante. Pode ficar "Em 16 e 17 nov, a Ucrânia atacou a **Ponte da Crimeia** (Kerch) duas vezes."
- **Slide 5, crédito:** está "domínio público" para uma foto CC0 (e na legenda "Demais: domínio público"). É aceitável; se o template permitir, use "CC0".
- Antes de pedir aprovação, confira de novo, em 20 nov, o estado do tráfego e do reparo.
