## APROVADO (coordenador, rodada 2, 14 nov)

Todas as correções bloqueantes da rodada 1 foram aplicadas no commit 494f9d3 (capa "a pergunta", 13 nov, posição de Kiev, Kostiantynivka separada, foto de von der Leyen, resumo da troca, fontes novas, foto CC0 do reencontro). Conferido em folha de contato. Pendente: reconferir na noite de 16 nov a resposta de EUA/Kremlin, a troca de prisioneiros e a data da próxima rodada.

---

REPROVADO

# Revisão: 2026-11-17-donbas-por-otan (commit 4381be2)

Revisado em 14 nov 2026. Agendamento: 17 nov 2026, 06:01.

| Item | Resultado |
|---|---|
| 1. Fatos | **problema**: a capa exagera a alegação, a data da fala está errada, o local da declaração de Putin está errado, a frase do slide 5 mistura dois assuntos e o resumo do slide 8 erra sobre a troca |
| 2. Isenção | **problema**: falta a posição da própria Ucrânia sobre o Donbas (sem retirada; referendo se houver garantias). O "sem resposta de EUA/Kremlin" segue verdadeiro hoje |
| 3. Imagens | **problema**: slide 7 com Mark Carney (Canadá) em destaque num slide sobre europeus. Slide 6 fraco (recomendado trocar). Licenças ok |
| 4. Texto | ok no geral (todos os slides ≤ 45 palavras: 36/40/42/40/44/43/25; 1 título; nenhuma factbox; sem emoji; sem pergunta; `primeiro_comentario` vazio). Frase do ISW no slide 5 está truncada ("quereria concentrar forças") |
| 5. Visual | ok: números 2/9 a 9/9 certos, nada cortado, texto legível, fotos coloridas, rostos acima do degradê. Story ok |
| 6. Legenda | ok no tamanho (1.269 caracteres), mas herda os erros de data e de "sugeriram" (ver abaixo) |
| 7. Reel | não se aplica (`reel.gerar: false`) |

## Checagem de fatos (WebSearch extended, 14 nov)

| Fato | Situação | Fontes |
|---|---|---|
| Witkoff e Kushner com Putin em Moscou, 12 nov, depois de 2 dias em Abu Dhabi (terminou 11 nov) sem grande avanço | confirmado | NPR 12 nov, Kyiv Post 89964, Time, Moscow Times |
| Pergunta "Donbas por OTAN" | confirmada como **alegação de Zelensky**, mas: (a) a fala é de **13 nov** (sexta), divulgada no sábado 14; (b) ele descreveu como **uma pergunta, não uma oferta**, e disse que **não há proposta concreta**; (c) disse que a Ucrânia não retira tropas, mas poderia levar o tema a referendo com garantias de segurança firmes | Kyiv Independent, Kyiv Post 90115, Al Jazeera 14 nov, The New Arab, CNBC/Reuters (CP24) |
| "A OTAN voltou à agenda" / "primeira vez" | confirmado (atribuído a Zelensky) | The New Arab, Al Jazeera, Kyiv Post |
| Resposta dos EUA/Kremlin à alegação | **nenhuma até 14 nov**. A Politico registra que a Casa Branca e o Departamento de Estado não responderam a pedido de comentário. O slide 4 segue correto, mas **reconfira na noite de 16 nov** | Globe and Mail, Kyiv Independent, Politico (citada) |
| Witkoff: Putin aceitou europeus na próxima rodada | confirmado (declaração à TV estatal russa) | Kyiv Post 89964, Politis/NPR |
| Ushakov, "receita para guerra sem fim" | confirmado | Kyiv Post 89964, Yahoo/Reuters, SRN |
| Peskov, Putin "nunca recusou contatos com europeus" | confirmado (13 nov) | TASS 2217817, IR-PRESS 13 nov, APA |
| Kushner, "maior troca de prisioneiros" | confirmado. Depois de Dublin, Kushner disse que a troca foi "finalizada"; números em aberto | Moscow Times 13 nov, Newsweek, Interfax-Ucrânia |
| 1.000x1.000 / 1.500x1.500 (Zelensky) | confirmado como fala de Zelensky (uma reportagem cita também 1.200x1.200) | Newsweek, Interfax-Ucrânia |
| Kostiantynivka: proposta de Putin nos moldes de Oleshky; recusa de Zelensky | confirmado. Zelensky chamou a proposta de manobra para tomar a cidade. **A frase "Putin pessoalmente não apoia um cessar-fogo" se refere ao cessar-fogo energético, não a Kostiantynivka** | NV 50659198, Euromaidan Press 13 nov, Kyiv Post 90119, United24 |
| ISW: o Kremlin quer a pausa local para concentrar forças (rumo a Druzhkivka) | confirmado, como avaliação | Euromaidan Press 13 nov, RBC-Ucrânia, NV |
| Putin rejeita tropas ocidentais | confirmado, mas foi dito **por Putin em 12 nov, depois do encontro em Moscou**, não "em Abu Dhabi" | Kyiv Post 89979, NV (ISW), ynet |

## Correções exatas

1. **Capa (exagero factual).** "puseram na mesa" contradiz o próprio Zelensky (pergunta, sem oferta concreta). Troque:
   - `titulo_html`: `<span class="hl">Donbas por OTAN:</span> a pergunta que, segundo Zelensky, os EUA fizeram`
   - `gancho`: `A versão é de Kiev, sem oferta concreta. Washington e Moscou não comentaram.`

2. **Slide 3 (`slides[1].texto_html`): data e verbo.** Substitua por (41 palavras):
   `Em 13 nov, Zelensky disse que os negociadores dos EUA perguntaram se a Ucrânia deixaria o <strong>Donbas</strong> caso entrasse na OTAN. Segundo ele, foi a primeira vez que a aliança apareceu ligada a território, ainda sem oferta concreta: <em>“a OTAN voltou à agenda”</em>.`

3. **Slide 4 (`slides[2].texto_html`): isenção e local.** Falta a posição da Ucrânia; Putin falou em Moscou em 12 nov, não "em Abu Dhabi". Substitua por (44 palavras):
   `Até 14 nov, EUA e Kremlin não haviam comentado essa versão. Zelensky disse que a Ucrânia não retira tropas, mas levaria o tema a referendo com garantias firmes. Moscou segue exigindo o Donbas, e Putin repetiu em 12 nov que rejeita tropas ocidentais no país.`
   Antes de pedir aprovação (e de novo na noite de 16 nov), refaça a busca por resposta da Casa Branca, do Departamento de Estado ou de Peskov. Se alguém tiver respondido, troque a primeira frase pela resposta atribuída.

4. **Slide 5 (`slides[3].texto_html`): mistura de assuntos e frase do ISW.** Substitua por (43 palavras):
   `Putin propôs uma pausa humanitária em <strong>Kostiantynivka</strong>, nos moldes da de Oleshky. Zelensky recusou: chamou a proposta de manobra para tomar a cidade, que Moscou não conseguiu conquistar. Para o ISW, o Kremlin provavelmente quer a pausa para concentrar forças rumo a Druzhkivka (foto de 2024).`

5. **Slide 7 (img03): foto enganosa.** O enquadramento mostra Mark Carney, premiê do Canadá (fora da UE), em destaque ao lado de von der Leyen, num slide sobre a participação **europeia**. Zelensky nem aparece. Troque a img03 por uma foto só de líderes europeus ou de símbolos da UE, por exemplo um retrato oficial de Ursula von der Leyen (2024–2026, CC BY 4.0, European Union) ou bandeiras da UE na sede do Conselho/Comissão. Use WebSearch com `allowed_domains: ["commons.wikimedia.org"]` e `"query": "File:<nome exato>"`, ou `incategory:"Ursula von der Leyen in 2026"`. Não basta mudar o `foco`: com 12% Carney continua no quadro.

6. **Slide 8 (`slides[6].texto_html`): resumo errado.** A troca de prisioneiros foi acertada (Kushner e Zelensky); o que falta é número e data. Substitua por:
   `Confirmado: a reunião com Putin, a troca de prisioneiros acertada e a continuidade das conversas. Alegação de Kiev: a pergunta Donbas por OTAN. Sem confirmação: números e data da troca e a participação europeia.`

7. **Legenda:** troque a frase do segundo parágrafo
   `Em 14 nov, o presidente ucraniano disse que negociadores dos EUA sugeriram que a Ucrânia deixasse o Donbas caso entrasse na aliança. Não há resposta pública de Washington nem do Kremlin.`
   por
   `Em 13 nov, o presidente ucraniano disse que negociadores dos EUA perguntaram se a Ucrânia deixaria o Donbas caso entrasse na aliança; segundo ele, não houve oferta concreta, e Kiev não pretende retirar tropas. Até 14 nov, Washington e o Kremlin não haviam comentado.`
   Na abertura, mantenha "segundo Zelensky".

8. **Fontes:** acrescente as fontes do item 3 (posição da Ucrânia / referendo): Kyiv Independent (https://kyivindependent.com/us-floats-nato-membership-for-ukraine-in-exchange-for-donbas-withdrawal-zelensky-says/) e Al Jazeera 14 nov (https://www.aljazeera.com/news/2026/11/14/three-killed-in-russia-as-ukraine-claims-us-floated-nato-membership-option). Para Kostiantynivka/ISW, acrescente NV (https://english.nv.ua/russian-war/zelenskyy-calls-russia-s-kostiantynivka-plan-a-ploy-50659198.html) e Euromaidan Press 13 nov. Para Peskov: TASS (https://tass.com/politics/2217817). Para Putin e as tropas: Kyiv Post (https://www.kyivpost.com/post/89979).

9. **Slide 6 (recomendado, não bloqueia sozinho):** a foto mostra guardas de fronteira com uma bandeira, sem prisioneiros visíveis. Prefira a alternativa já listada, `File:Hugging at exchange of prisoners of war event in Ukraine, 23 May 2025 (cropped).jpg` (CC0), que mostra o reencontro. Mantenha "(foto de troca em maio de 2025)".

10. **Atualidade (antes de agendar):** o post sai 3 dias depois da pesquisa. Na noite de 16 nov, confira: (a) resposta de EUA/Kremlin à alegação (item 3); (b) se a troca de prisioneiros já aconteceu (Kushner disse que estava "finalizada"); se aconteceu, atualize os slides 6 e 8 com os números oficiais; (c) data/local da próxima rodada.

## Licenças e créditos
- img01: domínio público (DoD dos EUA); img02 e img05: Kremlin.ru, CC BY 4.0; img03: European Union, CC BY 4.0 (conferido na API: 3 maio 2026, Yerevan); img04: Presidência da Ucrânia, CC BY 4.0; img06: National Police of Ukraine, CC BY 4.0; img07: CC0; img08: Robert Haandrikman, CC BY 2.0. Todas livres, créditos em cada slide e na legenda. (A API do Commons limitou as requisições; só a img03 foi reconferida, as demais seguem o registro do `imagens.py`.)
- Nenhuma foto violenta nem com vítima identificável. A do slide 5 mostra dano material e um policial.

## Visual
Todos os JPEGs foram lidos: numeração 2/9 a 9/9 certa, texto legível, nada cortado, créditos visíveis, fotos coloridas, assunto acima do degradê. Story (1080×1920) ok, sem texto extra. Depois das correções, renderize de novo e confira se os slides 4 e 5 continuam dentro da área de texto.
