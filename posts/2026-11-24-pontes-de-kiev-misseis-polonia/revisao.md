# APROVADO (coordenador, rodada 2, 21 nov): correções 1–6 aplicadas; slides relidos. Reconferir em 23 nov: Artigo 4 e comentário do Kremlin.

REPROVADO

# Revisão: 2026-11-24-pontes-de-kiev-misseis-polonia
Revisor, 21 nov 2026. Arquivos lidos: post.json, pauta.md, slides 01 a 10, story/story.jpg e o payload do Metricool (`metricool.py payload --sha x`).
Os fatos foram rechecados por conta própria com WebSearch (o WebFetch não abre os sites de notícias, mas abre o Commons).

| Item | Resultado |
|---|---|
| 1. Fatos | **problema**: há um erro de leitura nos números (slide 3); faltam a direção do fechamento da ponte (slide 4), a formulação exata do Rutte (slide 9) e o "Kremlin" (slide 8) |
| 2. Isenção | **problema leve**: não há posição russa sobre a Polônia, e o slide 8 sugere que o Kremlin falou |
| 3. Imagens | **problema**: o Kh-101 de 2023 aparece em 5 de 9 fotos e passa por "míssil caído na Polônia"; as licenças e os créditos estão ok |
| 4. Texto | ok (35 a 43 palavras por slide, sem títulos nem tags, ortografia ok) |
| 5. Visual | ok (nada cortado, contador 2/10 a 10/10 correto, texto legível, fotos coloridas, logo e créditos visíveis) |
| 6. Legenda | ok no tamanho (1.186 caracteres com fontes e créditos); **problema**: a hashtag tem acento, faltam os balísticos e falta o aviso de foto de arquivo |
| 7. Reel | não se aplica (`reel.gerar: false`) |
| Story | ok; renderizar de novo depois de trocar o crédito da capa |

## Checagem independente (o que bate)
- **Zelensky**: "more than 400 attack drones and over 110 missiles, 27 of them ballistic". Está no post dele no X e em Al Jazeera e UNN. OK.
- **ISW, "maior de novembro"**: o boletim de 20 nov chama de "largest Russian strike package thus far in November 2026" (Kyiv Post e criticalthreats.org). OK.
- **Ministério da Defesa russo**: diz ter mirado pontes rodoviárias e ferroviárias usadas para levar armas e equipamentos ao front (The National, ABC Austrália, Al Jazeera). OK.
- **Putin**: prometeu resposta "muito mais dolorosa" depois dos ataques ucranianos à ponte "nesta semana" (ABC e The National). O plural "novos ataques" está ok.
- **Polônia**: Kh-101 em Nowy Lipowiec e provável drone a jato em Mołodycz (Hromadske, Interfax-Ucrânia, UNITED24, RMF24). Nowa Dęba, Coalizão dos Dispostos e Eastern Sentry também batem. Tusk falou em "provocação intencional" e disse que os objetos eram russos (RTE, Spokesman/AFP, HuffPost). Sem feridos. OK.
- **Mortos**: "ao menos 8" aparece em Al Jazeera, CBS News e ABC. O Kyiv Independent dá 9 (7 em Kiev, segundo Klitschko, e 2 em outras regiões) e depois 12 em 24 h, mas somando outros ataques. "Ao menos 8" continua certo e agora tem 3 fontes.

## Problemas e correções exatas

### P1. Slide 3: as duas contagens NÃO divergem (erro factual)
O ISW diz que "Zelensky and the Ukrainian Air Force reported 27 ballistic missiles, 84 cruise missiles, and 404 drones". Logo 84 + 27 = 111, que são os "mais de 110 mísseis" de Zelensky. A Força Aérea não contou menos; ela separou os tipos. Também chama atenção que só 3 dos 27 balísticos foram abatidos (o Kyiv Independent liga isso à falta de mísseis Patriot).
**Texto novo do slide 3 (42 palavras):**
> Os números batem com os da Força Aérea ucraniana: <strong>84 mísseis de cruzeiro, 27 balísticos e 404 drones</strong>. Ela informou o abate de 79 mísseis de cruzeiro, 380 drones e só 3 dos balísticos. Os dados não foram verificados de forma independente.

**Legenda**: troque "A Força Aérea ucraniana contou 84 mísseis de cruzeiro e 404 drones." por
> A Força Aérea ucraniana contou 84 mísseis de cruzeiro, 27 balísticos e 404 drones.

### P2. Slide 4: a ponte não fechou nos dois sentidos, e a fonte das mortes pode ficar só no `fontes`
Klitschko disse que o tráfego da margem direita para a esquerda está fechado na Podilsko-Voskresenskyi.
**Texto novo do slide 4 (40 palavras):**
> Em Kiev, três pontes sobre o Dnipro foram danificadas, segundo o prefeito Vitali Klitschko. A <strong>Podilsko-Voskresenskyi</strong> teve o tráfego fechado no sentido da margem esquerda; a Darnytskyi e a Pivdennyi seguiram abertas. Ao menos 8 pessoas morreram no país.

Inclua no `fontes`: `{"nome": "CBS News", "url": "https://www.cbsnews.com/news/ukraine-war-russia-intentional-provocation-poland-missiles-nato/"}`.

### P3. Slide 8: "o Kremlin não admitiu intenção" dá a entender que o Kremlin falou
Não achei declaração de Peskov nem do Kremlin sobre o caso. Os relatos falam em "no immediate comment from Moscow" (AP, via PBS). Há ainda uma ressalva do lado polonês: segundo a Charter'97, o chanceler Sikorski disse aguardar "confirmação final" de que os objetos eram russos. A Sputnik também deu isso, mas não serve como fonte. São só uma fonte e meia, então fica fora do texto.
**Texto novo do slide 8 (36 palavras):**
> Kosiniak-Kamysz disse que o momento provavelmente não foi acidental: um exercício da Coalizão dos Dispostos ocorria em Nowa Dęba, perto dos locais de queda. A investigação polonesa segue em curso. Até 21 nov, Moscou não havia comentado o caso.

Inclua no `fontes`: `{"nome": "PBS NewsHour / AP", "url": "https://www.pbs.org/newshour/world/nato-calls-russian-missiles-landing-in-poland-a-grave-violation-of-airspace"}`.
Antes do agendamento, o coordenador deve checar se o Kremlin se pronunciou entre 21 e 24 nov. Se sim, troque a última frase pela posição russa, atribuída.

### P4. Slide 9: Rutte não condenou "o ataque" (a frase sugere o ataque inteiro à Ucrânia)
Rutte chamou a violação do espaço aéreo de "perigosa" e "inaceitável" e disse que os aliados estão em "plena solidariedade" com a Polônia (Anadolu). Antes, já tinha falado em "grave violação" (PBS/AP).
**Texto novo do slide 9 (39 palavras):**
> Ninguém ficou ferido na Polônia, e não houve dano a infraestrutura crítica. O país <strong>não acionou o Artigo 4 da OTAN</strong>, mas pediu mais meios para a operação Eastern Sentry. O secretário-geral Mark Rutte chamou a violação de "perigosa" e "inaceitável".

Inclua no `fontes`: `{"nome": "Anadolu (Rutte)", "url": "https://www.anews.com.tr/world/2026/11/21/allies-stand-with-poland-after-airspace-breach-by-russia-nato-chief"}`.
**Artigo 4**: a maioria das fontes (Al Jazeera, Nacionale, Latin Times) diz que não foi acionado, mas uma newsletter afirma o contrário. Reconfirme no dia 23 ou 24 antes de mudar o rascunho para agendado. Se tiver sido acionado, troque a frase e a legenda.

### P5. Fotos: o Kh-101 de 2023 aparece em 5 fotos (capa, 2, 3, 6, 8), sempre num campo com neve
É repetitivo e, ao lado de "Três objetos caíram na Polônia", parece o míssil polonês. **Precisa de aviso de foto de arquivo.** Distribuição nova, com o Kh-101 só na capa e no slide 3:

| Slide | Foto nova | Licença (conferida no Commons) |
|---|---|---|
| Capa | img01 (manter) + `capa.credito` = `"Foto de arquivo: Kh-101 abatido na Ucrânia em 2023 · Air Force Command of Ukraine · CC BY 4.0"` (o render.py aceita `capa.credito`; já foi usado em 2026-10-26) | CC BY 4.0 |
| 2 | img05 Tu-95MS (o bombardeiro que lança o Kh-101) | CC BY-SA 2.0 |
| 3 | img09 Kh-101 (05) | CC BY 4.0 |
| 4 | nova img07: `File:2019-07-13 Dnieper River in Kyiv and Podil Bridge.jpg` (5184×3456), a ponte que fechou; alternativa `File:Podil Bridge, sunrise, 2020.jpg` (Zinnsoldat, CC BY-SA 4.0, em obras) | conferir na página (categoria Podilskyi Bridge) |
| 5 | img04 Darnytsia (ponte rodoviária e ferroviária, com trem: casa com "pontes rodoviárias e ferroviárias") | CC BY-SA 4.0 |
| 6 | img06 F-16 polonês, `foco` "50% 40%" | CC BY 2.0 |
| 7 | img06 com `foco` "15% 40%" (como está no 9 hoje) ou, sem repetir, a nova img08 do item 8 | |
| 8 | nova img08: `File:Władysław Kosiniak-Kamysz at the Pentagon, Washington, D.C., Aug 29, 2024 (cropped).jpg` (1251×1672, foto do Departamento de Defesa dos EUA) | domínio público (PD-USGov-Military) |
| 9 | nova img10: `File:2025 NATO Secretary General Mark Rutte in 2025 (cropped).jpg` (1453×1938, Pentágono, 24 abr 2025) | domínio público (PD-USGov-Military) |

Descartados: `Bateria Patriot - panoramio.jpg`, porque é uma bateria americana em Morąg (2010) e enganaria como "defesa polonesa"; e o retrato de Tusk da KPRM, com 401×526 px e licença ambígua (CC BY 3.0 PL, com mudança para NC-ND em 2022).
No slide 7, o slide de Tusk, manter o F-16 é aceitável. Depois de trocar, leia de novo os JPEGs: o rosto (8 e 9) precisa ficar acima do degradê.
Atualize o `alt_text`, por exemplo: "Carrossel sobre o ataque russo de 19 para 20 de novembro, com fotos de arquivo de um míssil Kh-101, um bombardeiro Tu-95, pontes de Kiev, um caça F-16 polonês, o ministro Kosiniak-Kamysz e Mark Rutte."

### P6. Legenda e hashtags
- Troque `"#mísseis"` por `"#misseis"`.
- "Arraste para o lado." no fim está **ok** (o CLAUDE.md pede "arraste para o lado"; não tem emoji nem pergunta ao leitor). Logo antes, acrescente uma linha própria: `Fotos de arquivo, sem relação direta com os fatos do dia.` O mesmo padrão foi usado em 2026-11-15.
- Aplique a troca da legenda do P1. O tamanho segue bem abaixo de 2.200.

### Depois das correções
Renderize de novo `render.py` e `story.py` (a capa muda o crédito) e mande ao revisor numa nova rodada. Os slides 2, 5, 6 e 7 só mudam de foto, e o texto deles está aprovado.
