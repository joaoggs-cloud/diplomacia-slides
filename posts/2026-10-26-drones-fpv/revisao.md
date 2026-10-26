APROVADO

# Revisão — 2026-10-26-drones-fpv ("O drone de US$ 500 que mudou a guerra")

Revisor: agente revisor · 26 out 2026 · post já `agendado` (26/10, 18:40).
Este post foi feito antes da equipe de agentes, então não há `pauta.md`: os fatos foram
conferidos contra `post.json → fontes` e com buscas próprias.

Veredito: **aprovado para ir ao ar**. Nenhum erro factual encontrado. Há **uma correção
recomendada** (foto do slide 8) e uma ressalva sobre o número de US$ 800, nenhuma das duas
bloqueia a publicação.

## Checklist

| Item | Resultado |
|---|---|
| 1. Fatos | ok, com ressalva (US$ 800 não reconfirmado, ver P2) |
| 2. Isenção | ok |
| 3. Imagens / licenças | ok nas licenças; **problema** de contexto na foto do slide 8 (P1) |
| 4. Texto (ortografia, ≤ 60 palavras/slide, ordem) | ok |
| 5. Visual (slides 01–09 lidos um a um) | ok |
| 6. Legenda (≤ 2.200 caracteres) | ok: 1.126 caracteres com fontes, créditos e hashtags |

### 1. Fatos conferidos (buscas próprias)

| Fato | Resultado |
|---|---|
| 66% das perdas de equipamento russo em jan/2025 por drones (Syrskyi) | **Confirmado**: Ukrinform, Ukrainska Pravda, Interfax-Ucrânia (6 fev 2025). Ele disse "drones de ataque de vários tipos" (FPV = 49% dos acertos). O texto atribui a fala a ele: ok. |
| ~2/3 segundo Jack Watling (RUSI) | **Confirmado**: página da RUSI "Tech can give Europe more bang for defence buck" atribui a Watling a estimativa de que drones causaram cerca de dois terços da destruição de tanques, veículos e outros equipamentos russos "no último ano". |
| Teia de Aranha: 1 jun 2025, 117 drones, 41 aeronaves (Kiev) vs até 20 atingidas e ~10 destruídas (EUA/Reuters) | **Confirmado**: Malyuk (SBU) à Interfax-Ucrânia: "117 drones"; Kyiv Independent repercute a Reuters (2 autoridades dos EUA: até 20 atingidas, ~10 destruídas). A alegação de Kiev está atribuída e a contraestimativa aparece ao lado: ok. |
| Drone de fibra óptica ~US$ 800, "o dobro de um FPV comum" | **Não reconfirmado** (P2). A fonte citada (Euromaidan Press) estava inacessível desta sessão. Outras fontes dão valores próximos: ~30 mil UAH (≈ US$ 720–750) para os modelos mais baratos (Komersant/Vyriy, 2025) e ~US$ 1.200 para alcance de 10 km (TWZ). O valor é plausível como ordem de grandeza. |
| FPV ~US$ 500 | Coerente com as estimativas correntes (~US$ 400–500). Não tem fonte própria em `fontes`, mas é ordem de grandeza amplamente citada. |

### 2. Isenção
O tema é tecnológico. A alegação ucraniana dos 41 aviões aparece junto com a estimativa menor
dos EUA. Não há adjetivos contra nenhum lado e nada glorifica a violência.

### 3. Imagens
Todas as 8 têm licença livre: 5× CC BY 4.0 (RBC-Ukraine, MVS Ucrânia, ArmiyaInform) e 2× domínio
público (USAF). Os créditos aparecem nos slides e na legenda. O crédito do slide 3 sai truncado
("Міністерство внутрішніх справ України …"), mas fica legível e o nome completo está na legenda. Nenhuma
vítima aparece: o slide 3 mostra um tanque russo destruído em Mariupol, sem pessoas.
Observações que não exigem correção:
- O slide 2 usa uma foto de treino EUA/Quênia com óculos FPV. Como o slide é genérico ("O que é") e não diz que a foto é da Ucrânia, pode ficar.
- O slide 3 mostra um tanque destruído em 2022 (Mariupol), provavelmente sem drone FPV. O texto não afirma a causa, então pode ficar.

### 4–5. Texto e visual
Todos os slides estão dentro de 60 palavras (o maior tem cerca de 45). A numeração vai de 02/09 a 08/09, e
nada sai cortado ou ilegível. A capa tem um gancho forte e o CTA está correto.

## Problemas e correção exata

**P1 (recomendado, não bloqueia): foto do slide 8 (img08).** É um Tu-95MS **em voo**
escoltado por um **F-15 da Força Aérea dos EUA** (Alasca, 2006). O slide fala de bombardeiros
**estacionados** atingidos na Teia de Aranha. Um caça americano em destaque nesse slide pode ser
lido como envolvimento dos EUA na operação, e essa narrativa é disputada.
Correção, se ainda houver tempo antes das 18:40:
- Opção A (preferida): trocar img08 por uma foto de Tu-95/Tu-22M3 **no solo**, sem aeronave
  dos EUA (`scripts/imagens.py posts/2026-10-26-drones-fpv --so img08` com query
  `incategory:"Tupolev Tu-95MS"` ou `"Tupolev Tu-22M3" Engels/airfield`). Depois, renderizar de novo, fazer push e
  atualizar o post no Metricool com o novo SHA.
- Opção B (mínima): manter a foto e colocar no slide a legenda "Na foto: Tu-95MS russo
  escoltado por caça dos EUA perto do Alasca (2006), foto ilustrativa". Para isso, a
  factbox "Quantos?" teria de ir para o texto do slide, já que só cabe uma factbox.
Se não houver tempo, o post pode ir ao ar assim: o texto não afirma que a foto é da operação.

**P2 (ressalva, sem ação obrigatória): US$ 800 da fibra óptica.** Não consegui abrir a fonte
(Euromaidan). As fontes alternativas indicam de ≈ US$ 720 a US$ 1.200. Se quiser blindar,
troque no slide 7 "Custam cerca de US$ 800, o dobro de um FPV comum" por
"Custam mais que um FPV comum (centenas de dólares a mais)". Não é obrigatório.

## Fontes da revisão
- Ukrinform: https://ukrinform.net/rubric-ato/3957045-cinc-syrskyi-attack-drones-disabled-over-66-of-russian-equipment-in-january.html
- Ukrainska Pravda: https://www.pravda.com.ua/eng/news/2025/02/6/7496997/
- RUSI: https://www.rusi.org/news-and-comment/in-the-news/tech-can-give-europe-more-bang-defence-buck
- Kyiv Independent / Reuters: https://kyivindependent.com/reuters-ukraine-struck-fewer-russian-bombers-during-operation-spiderweb-than-estimated-us-officials-claim/
- Interfax-Ucrânia (Malyuk, 117 drones): https://ua.interfax.com.ua/news/general/1082175.html
- Komersant (preço da fibra óptica): https://komersant.ua/en/v-ukraini-vyprobuvaly-dalekobiyni-fpv-drony-na-optovolokni-shcho-z-ikh-vyrobnytstvom/
- TWZ: https://twz.com/news-features/inside-ukraines-fiber-optic-drone-war
