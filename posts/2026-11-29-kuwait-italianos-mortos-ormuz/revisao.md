# APROVADO (coordenador, rodada 2, 26 nov): correções 1–8 aplicadas; slides relidos. Reconferir em 28 nov.

REPROVADO

# Revisão: 2026-11-29-kuwait-italianos-mortos-ormuz (rodada 1, 26 nov 2026, noite)

O WebFetch está bloqueado para aljazeera.com e cyprus-mail.com nesta sessão. Refiz a checagem com WebSearch (modo extended) e com a API do Wikimedia Commons, que funcionou.

| Item | Resultado |
|---|---|
| 1. Mortes, Ministério da Defesa do Kuwait (4 feridos e depois 2 mortes), Tajani/Rheinmetall Italia, estação antiaérea, acusação ao Irã | ok (Al Jazeera, ABC News AU, CBC/Reuters, Yahoo/Reuters, Al-Monitor) |
| 2. Negação iraniana: embaixada em Roma "categoricamente" | ok (Reuters via Arab Times/Iran International, CBS) |
| 2b. Araqchi e investigação conjunta "com o Kuwait" | **problema**: as fontes dizem que ele ofereceu a Tajani, por telefone, uma comissão de inquérito conjunta. Não há menção ao Kuwait |
| 3. "Protestar formalmente" | **problema**: Tajani disse "Ci lamenteremo con l'ambasciata dell'Iran" (Al Jazeera: "lodge a complaint"). É queixa, não protesto formal. Von der Leyen: ok (post no X + CBS + Arab Times) |
| 4. IRGC: 2 petroleiros, minas ao norte de Khasab, rota não autorizada, sem verificação | ok (Reuters via Yahoo, US News, Arab News, Internazionale, todos de 26 nov) |
| 5. Bloqueio dos EUA em 13 abr e 14 jul | ok (NPR 12 abr; CENTCOM "US forces to resume naval blockade": 1ª fase de 13 abr a 18 jun; Al Jazeera 14 jul; AP/ABC7) |
| 6. "Reabre em até 48 horas" | **problema**: o "plano de dois dias" é de 1 a 2 nov (Africanews 2 nov, Gulf News, Arab News PK), não de 26 nov. Está apresentado como notícia do dia e fere a regra dos 7 dias para conflito_atual. A tafs.uz/Anews/MEMO de 26 nov falam só das exigências |
| 7. Isenção | **problema** (capa): o destaque amarelo (`hl`) cobre só "Itália e Kuwait acusam o Irã", e "Teerã nega" fica sem destaque. Nos slides 3/4 está equilibrado. Nenhum nome de vítima: ok |
| 8a. Imagem img01 (Skynex, capa e slide 3) | **problema (bloqueante)**: licença duvidosa. A página do Commons tem Autor = Rheinmetall e "Permission" = link de notícia do mil.in.ua, enviada pelo assistente da uk.wp. É foto de imprensa da empresa, relicenciada por terceiro. Além disso tem 1200×630 (cara de frame de vídeo), fica ampliada cerca de 2× no corte 4:5 e aparece suave e com compressão |
| 8b. img02 Boxer/Skyranger (slides 2 e 5) | licença ok (self, CC BY-SA 4.0, Wolpat, Eurosatory 2018). Repetida em 2 slides: recomendação |
| 8c. img07 Kuwait (slide 4) | ok (CC BY 2.0, Flickr revisado, Francisco Anzola, 2016) |
| 8d. img04 MODIS (slide 6) | ok (NASA, domínio público) |
| 8e. img05 caça-minas 2013 (slide 7) | ok (US Navy, domínio público). Sem aviso de ano no slide: recomendação |
| 8f. img06 HMS Middleton (slide 8) | ok (CC BY-SA 2.0, Flickr Defence Images revisado). 1000×738, um pouco suave mas aceitável |
| 8g. Crédito da capa | **problema**: "Foto de arquivo: sistema antiaéreo Skynex" não traz autor nem licença. Todos os posts anteriores trazem, e CC BY-SA exige |
| 9. Texto, até 45 palavras | **problema**: o slide 7 tem 50 palavras. Os demais têm de 26 a 39 |
| 10. Cara de IA: títulos, tags, emoji, perguntas | ok (sem títulos nos slides, sem emoji, sem perguntas, primeiro comentário vazio) |
| 11. Visual | ok: numeração de 2/9 a 9/9 certa, nada cortado, texto legível, fotos coloridas, assunto acima do texto |
| 12. Legenda | ok: 1.401 caracteres com fontes, créditos e hashtags. 6 hashtags específicas. Tem "Arraste para o lado" e o aviso de fotos de arquivo. Precisa acompanhar as correções abaixo |
| 13. CTA | ok |
| 14. Story | ok no visual. Renderizar de novo depois de trocar a capa |
| Reel | não se aplica (`reel.gerar: false`) |

## Correções exatas

**C1. Capa: destaque igual para acusação e negação.**
`titulo_html`:
`Dois italianos morreram no Kuwait. <span class="hl">Itália e Kuwait acusam o Irã; Teerã nega</span>`

**C2. Trocar a img01 (Skynex), que tem licença duvidosa e baixa resolução, na capa e no slide 3.**
Sugestão: `"query": "File:DSC05548 Feuerleitgerät 75 95 Skyguard, Bundesheer, 2023-10.jpg"`, com a alternativa `"File:Skyguard radar of Malaysian Army in display in AKM Pahang 2022.jpg"` (CC BY-SA 4.0). Rodar `imagens.py --so img01` e conferir no .json se a licença é livre e a resolução é de pelo menos 1920 px.
Segunda opção: `File:Skynex AC West.jpg` (CC BY-4.0, Comando Aéreo Oeste da Ucrânia). Nesse caso o crédito precisa dizer "em serviço na Ucrânia".
Se o slide 3 usar uma foto diferente da capa, melhor ainda.
Crédito da capa no formato dos posts anteriores, por exemplo:
`"credito": "Foto de arquivo: radar antiaéreo Skyguard (Áustria) · <autor> · <licença>"`.
Não escrever que é o sistema da estação do Kuwait: isso não está confirmado em 2 fontes.

**C3. Slide 4 (negação). Tira o "com o Kuwait", que não está nas fontes, e reforça a negação (38 palavras):**
`<strong>O Irã nega.</strong> A embaixada iraniana em Roma rejeitou a acusação "categoricamente", e o porta-voz das Forças Armadas negou qualquer ataque ao Kuwait. Em telefonema com Tajani, o chanceler Abbas Araqchi se disse disposto a uma investigação conjunta.`
Fontes: CBC/Reuters (porta-voz Abolfazl Shekarchi), Quotidiano.net e ANSA (telefonema e comissão conjunta).

**C4. Slide 5 (protesto):**
`A Itália disse que vai apresentar uma queixa à embaixada iraniana. A presidente da Comissão Europeia, <strong>Ursula von der Leyen</strong>, pediu mais pressão sobre o Irã.`

**C5. Slide 7 (bloqueio). Corta para 45 palavras; as datas foram confirmadas:**
`O pano de fundo é o impasse. O <strong>bloqueio naval dos EUA</strong> a portos iranianos começou em 13 abr, após o fracasso das conversas em Islamabad, e foi retomado em 14 jul. Teerã condiciona a normalização da navegação ao fim do bloqueio, entre outras exigências.`
Acrescentar em `fontes`: CENTCOM https://www.centcom.mil/MEDIA/PUBLIC-RELEASES/Article/4542098/us-forces-to-resume-naval-blockade-against-iran/ e Al Jazeera https://www.aljazeera.com/news/2026/7/14/us-strikes-new-targets-in-iran-as-tehran-hits-gulf-states-hormuz

**C6. Slide 8 (mediação). Cortar as "48 horas", que são de 1 a 2 nov e não do dia (42 palavras):**
`Mediadores do Catar e do Paquistão seguem levando mensagens entre Teerã e Washington. Em 26 nov, o chanceler Araqchi disse que o Irã examina novas ideias, mas insiste nas suas exigências para reabrir Ormuz, como o fim do bloqueio e das sanções.`
Fontes: Middle East Monitor https://www.middleeastmonitor.com/20261126-iran-says-qatari-pakistani-mediation-in-talks-with-us-continues/ e Anews https://www.anews.com.tr/middle-east/2026/11/26/iran-says-qatari-pakistani-mediation-in-talks-with-us-continues (mais a tafs.uz que já está na lista).

**C7. Legenda. Trocar duas frases:**
- "A Itália vai protestar formalmente, e Ursula von der Leyen pediu mais pressão sobre Teerã." passa a ser "A Itália vai apresentar queixa à embaixada iraniana, e Ursula von der Leyen pediu mais pressão sobre Teerã."
- "Mediadores do Catar e do Paquistão seguem atuando, e o Irã fala em reabrir Ormuz em até 48 horas se suas condições forem atendidas." passa a ser "Mediadores do Catar e do Paquistão seguem atuando, e Araqchi disse que o Irã mantém suas exigências para reabrir Ormuz, entre elas o fim do bloqueio dos EUA."

**C8. Renderizar de novo** os slides e o story (`story.py`) depois das trocas.

## Recomendações (não bloqueiam)
- O Boxer/Skyranger (img02) aparece nos slides 2 e 5. Para o slide 5 (Itália/UE), uma foto da Farnesina ou do Berlaymont evitaria a repetição.
- Slide 7: a foto é de caça-minas num exercício de 2013. Vale usar `credito_custom` "Foto de arquivo (exercício no Golfo, 2013) · domínio público". Outra opção é trocar com o slide 6: caça-minas no slide das minas e o mapa MODIS no do bloqueio.
- Slide 8: o crédito pode ser "LA(Phot) Gary Weatherston / UK MoD · CC BY-SA 2.0", que é o fotógrafo indicado na página.
- Slide 6: a frase da Reuters ("não conseguiu verificar") foi confirmada para o caso de 26 nov só de forma indireta (Sabq). Se quiser blindar, use "Não houve confirmação independente." A IRGC já fez alegações parecidas em set e out, e o CENTCOM negou ao menos uma delas.
- A notícia de 26 nov pode mudar até domingo (investigação, novas versões). Reconfira no sábado à noite antes do APROVAR.
