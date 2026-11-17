REPROVADO

# Revisão — 2026-11-20-sudao-kordofan-drones (revisor, 17 nov 2026)

Obs.: o WebFetch não alcança ohchr.org, eeas.europa.eu nem hrw.org nesta sessão (fora dos domínios permitidos). Os fatos foram conferidos por WebSearch (extended), com os resumos das páginas e coberturas independentes.

## Tabela

| Item | Resultado |
|---|---|
| 1. OHCHR: ao menos 306 mortos, 3 primeiras semanas de out, SAF e RSF | ok (OHCHR 23 out; Radio Tamazuj, Ahram, Eurasia Review) |
| 2. Quinteto 13 nov, trégua humanitária, sem apontar autor | ok (EEAS, IGAD, AA, Radio Tamazuj); falta atribuir a frase "Os drones mataram..." à nota (ajuste leve) |
| 3a. El Khuwei retomada em 13 nov (alegação do Exército) | ok (Sudan Tribune, Radio Tamazuj, New Arab) |
| 3b. "Primeiro avanço do SAF na região desde maio de 2025" | **PROBLEMA**: em 7 nov o Exército já dizia ter tomado Iyal Bakhit, na localidade de El Khuwei (Sudan Tribune). A Sudan Tribune diz "primeira localidade" (município) do estado, não "primeiro avanço" |
| 3c. Al Nahud sob controle da RSF | ok: RSF desde 2 mai 2025, segue com ela em 17 nov (Sudans Post). "Maior cidade" diverge: Sudan Tribune e Al-Monitor dizem "maior", AFP/TRT diz "segunda maior" |
| 4. El Fasher 26 out 2025, ~18 meses de cerco, <70 mil vs >1 milhão | ok (Anistia; o número vem de organizações humanitárias citadas pela Anistia, e o slide atribui assim) |
| 5. IPC fome El Fasher/Kadugli nov 2025; alerta 12 out 2026 | ok (alerta em ipcinfo.org, AP/Washington Post, Sudan Tribune). **Factbox**: "Não há nova classificação de fome em 2026" afirma demais: um alerta do IPC de fev 2026 já apontava limiares de fome superados em Um Baru e Kernoi |
| 6. Genebra 21 out, Suíça + enviado da ONU, "mais de 20 países" | ok (21 países + 5 organizações segundo a ONU, 27 segundo Boulos; "mais de 20" está certo) |
| 6b. Citação de Boulos "não há solução militar" | **PROBLEMA**: só aparece na manchete do The National. Na 2ª fonte da pauta (Qatar Tribune) não está a frase. Quem disse isso em entrevista coletiva foi o enviado da ONU, Haavisto (Arab News/eNCA), e a reunião "descartou solução militar" (Asharq Al-Awsat) |
| 7. Quad nov 2025, 3 meses; RSF aceitou, Burhan rejeitou | ok (Al Jazeera 24 nov 2025, PBS, Crisis Group). Isenção: falta a justificativa de Burhan (papel dos Emirados) e o fato de que a trégua da RSF foi unilateral e os combates seguiram |
| 8. Reel cena 06 | **PROBLEMA**: vaga e desequilibrada (só o Exército aparece como quem rejeitou) |
| 9a. Licenças | ok: todas CC BY / CC BY-SA, nenhuma de agência |
| 9b. Créditos truncados | **PROBLEMA**: slide 03 "CC BY-SA ..." e slide 06 "CC BY-S..." (a licença fica ilegível, e a CC BY-SA exige identificá-la). Nesses dois slides o rodapé "DIPLOMACIA DA GUERRA" quebra em 2 linhas |
| 9c. Créditos na legenda do Reel | **PROBLEMA**: `payload-reel` omite "Dromaius Novaehollandiae (CC BY-SA 3.0)", o mapa da cena 04 (img04). Bug em `legenda_reel`/`creditos`: só entram imagens usadas também nos slides do carrossel, e o carrossel usa img10 em vez de img04 |
| Isenção geral | ok com os ajustes dos slides 09 e da cena 06 do Reel; ataques atribuídos às duas partes; alegações marcadas |
| Texto: palavras por slide | ok (máx. 44); reel ≤ 16 |
| Texto: ortografia | problema leve: "co-presidida" → "copresidida"; slide 02 "em Cordofão" → "no Cordofão" |
| Cara de IA (títulos/factbox/emoji/perguntas) | ok: 0 títulos, 1 factbox, sem emoji, sem pergunta, comentário vazio |
| Visual carrossel | ok: número de slide certo, legível, fotos coloridas. Menor: a capa e o slide 09 repetem a mesma foto (img02) |
| Visual reel / story | ok: frases inteiras, crédito presente. Menor: na cena 04 o mapa fica quase todo sob o degradê |
| Legenda | ok: 1.494 caracteres (carrossel) e 937 (Reel), TRIAL_REEL às 19:01 de 20 nov. A linha manual "Imagens: Wikimedia Commons (créditos nos slides)." duplica a linha automática de créditos |

## Correções exatas (obrigatórias)

1. **Slide 04 (img10)**: trocar `texto_html` por:
   `No mesmo dia, o Exército e aliados disseram ter retomado <strong>El Khuwei</strong>, no Cordofão Ocidental, em poder da RSF desde maio de 2025. Seria o primeiro município do estado retomado pelo Exército. É alegação do Exército; a RSF não respondeu.`
   (38 palavras; acrescentar em `fontes` a Sudan Tribune 320981, sobre Iyal Bakhit, só como referência, se quiser.)
   Antes de pedir aprovação, conferir se a RSF já respondeu ou retomou a cidade.

2. **Slide 08 (img07)**: trocar `texto_html` por:
   `Em 21 out, a Reunião Consultiva sobre o Sudão, em Genebra, copresidida pela Suíça e pelo enviado da ONU, reuniu mais de 20 países. Os participantes descartaram uma <strong>solução militar</strong> e defenderam uma trégua humanitária.`
   Fontes: trocar Qatar Tribune por Asharq Al-Awsat (https://english.aawsat.com/arab-world/5332646-international-meeting-rules-out-military-solution-sudan-war) e Arab News (https://www.arabnews.pk/middle-east/no-military-solution-in-sudan-un-envoy-3004878).

3. **Slide 07, factbox**: trocar `texto` por:
   `O alerta de outubro não é uma nova classificação de fome: trata da piora das condições.`
   Acrescentar em `fontes` o alerta do IPC: https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/docs/IPC_Alert_Sudan_Oct2026.pdf

4. **Slide 09 (isenção)**: trocar `texto_html` por:
   `A trégua já foi tentada. Em nov 2025, o Quad (EUA, Emirados, Arábia Saudita e Egito) propôs uma pausa humanitária de três meses. A RSF disse aceitar, mas os combates seguiram; o chefe do Exército, <strong>Abdel Fattah al-Burhan</strong>, rejeitou, citando o papel dos Emirados.`
   (44 palavras; fonte: Al Jazeera https://www.aljazeera.com/news/2025/11/24/sudan-army-chief-rejects-truce-proposal-citing-uae-role)

5. **Reel, cena 06 (img07)**: trocar por (18 palavras):
   `ONU, União Africana e UE pedem <em>trégua</em>. Em 2025, a RSF disse aceitar uma pausa; o Exército rejeitou.`

6. **Créditos truncados**: em `imagens`, encurtar `autor`:
   - img03: `"Mohamed Elgoni/UNOCHA"`
   - img05: `"INPE/Observação da Terra"`
   Renderizar de novo os slides 03 e 06 e as cenas do Reel. A licença precisa aparecer inteira, e o rodapé tem de voltar a ficar em 1 linha.

7. **Legenda do Reel sem o crédito do img04**: na cena 04 (`reel.cenas[2]`), trocar `"imagem": "img04"` por `"imagem": "img10"` (mesmo arquivo e mesmo autor) e renderizar o Reel de novo. A alternativa é corrigir `scripts/metricool.py → legenda_reel` para calcular os créditos pelas imagens do Reel. Depois conferir com `payload-reel` se aparece "Dromaius Novaehollandiae (CC BY-SA 3.0)".

## Correções recomendadas

8. **Slide 02**: "em Cordofão, Darfur, Cartum e outros estados" → "no Cordofão, em Darfur, em Cartum e em outros estados".
9. **Slide 03**: "Os drones mataram civis e danificaram..." → "Segundo a nota, os ataques mataram civis e danificaram usinas de energia e unidades de saúde."
10. **Slide 05**: "maior cidade do Cordofão Ocidental" → "principal cidade do Cordofão Ocidental" (as fontes divergem entre maior e segunda maior); "Nada disso foi verificado de forma independente." → "O avanço não foi verificado de forma independente." (o controle da RSF sobre Al Nahud é fato estabelecido).
11. **Capa**: o post sai em 20 nov e o título não situa o período. Sugestão: `<span class="hl">Ao menos 306 mortos por drones</span> em três semanas de outubro: a guerra do Sudão mudou de arma`. Se ficar longo, manter "em três semanas" e pôr "Em outubro, a ONU..." no gancho.
12. **Legenda**: apagar a linha "Imagens: Wikimedia Commons (créditos nos slides)." porque o script já acrescenta a linha completa de créditos.
13. **Slide 09**: a mesma foto da capa (img02). Se houver alternativa livre (ex.: Category:Zamzam IDP camp), trocar.
