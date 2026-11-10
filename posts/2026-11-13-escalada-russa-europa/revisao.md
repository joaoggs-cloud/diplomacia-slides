APROVADO (coordenador, 10 nov 2026, rodada 2), no SHA 6f9e545bca4ea1fdbad999c397d95a121af7ee13. As 4 correções obrigatórias foram aplicadas:
1. Slide 6: a fala de Peskov agora se refere às geladeiras.
2. Slide 5: a data passou a 'Entre 2 e 6 nov'.
3. Créditos da img05 e da img09 encurtados; conferi o crédito no slide 5.
4. Slide 8: a foto do TransPulp foi trocada por uma imagem de satélite do Golfo da Finlândia (NOAA, domínio público).
As recomendações dos slides 3 e 4 e da legenda também entraram.

--- Rodada 1 ---

REPROVADO

Revisão do post `2026-11-13-escalada-russa-europa` (SHA 49bbb82, agendado para 10 nov 2026, 06:01).
Faltam 4 correções rápidas (texto/crédito/foto). Depois delas, o post pode ser aprovado sem nova pesquisa.

| Item | Resultado |
|---|---|
| Fatos | problema (slides 5 e 6) |
| Isenção | ok: nenhuma frase afirma autoria russa; suspeita atribuída ao FT e negativa do Kremlin presente na capa, no slide 6, no slide 9 e na legenda |
| Imagens e licenças | problema (slide 8); licenças ok: PD, CC BY 2.0, CC BY-SA 3.0/4.0, nenhuma foto de agência |
| Créditos | problema (slides 5 e 9 truncados) |
| Texto | ok: 2 títulos e 1 factbox, sem emoji e sem pergunta; o slide 6 tem 55 palavras (acima das 45 do layout, abaixo de 60) |
| Visual | ok: numeração 2/10 a 10/10, nada cortado e Inter legível; o crédito do slide 5 encosta no rodapé |
| Legenda | ok: 1.410 caracteres, sem emoji, créditos presentes |
| Story | ok |

## Fatos conferidos por conta própria (WebSearch)
- Geladeiras, 2 nov, em 9 países da UE (11 na Europa contando Alemanha, Romênia e Reino Unido), e 1a onda na França em out: ok (Al Jazeera, Irish Examiner, CNBC 13 out).
- Fala de Hansen ("deliberate attempt to disrupt our food supply chain"): ok. ENISA e Europol: houve **reunião** da força-tarefa interinstitucional já existente, com ENISA e Europol (porta-voz Regnier), não a criação de uma nova.
- EFS: 3 locais de plasma, sem perda de produto, via fornecedor de refrigeração (Coolworld): ok (Euronews, NBC, CBS). O EFS fala em "segunda-feira" = 2 nov.
- Ameaças de bomba: começaram em **2 nov** (voo da Wizz Air Londres–Sófia desviado para Budapeste e escoltado por um Gripen), não em 3 nov. "Dezenas", Praga e Madri, desvios, caças e nenhum explosivo: ok.
- Peskov, 5 nov, "absurdas": ok, mas a frase se referia aos **ataques às geladeiras** (Interfax via The Star, Arab News e Brussels Signal), não às ameaças de bomba.
- Romênia (31 out à noite, 4 F-16 e helicóptero) e avaliação letã de 3 nov (um drone provavelmente russo, o Geran de domingo, e outro provavelmente ucraniano): ok.
- Fitburg: 5 nov, capitão a 3 anos e 6 meses, sentença ainda não definitiva e o capitão vai recorrer: ok (gCaptain, Marine Insight, Ukrinform).
- Briefing da House of Commons Library "Russia's hybrid warfare campaign in Europe", 4 nov: existe. Ele fala em campanha "intensifying" e registra que a Rússia nega. Aceitável com a atribuição que já está no slide.

## Correções obrigatórias
1. **Slide 6, contexto da fala de Peskov.** No texto, a negativa aparece como resposta às ameaças de bomba. Troque a última frase por:
   `Em 5 nov, o porta-voz do Kremlin, Dmitri Peskov, chamou de “absurdas” as acusações sobre os ataques às geladeiras.`
   A troca também corta palavras do slide.
2. **Slide 5, data.** Troque `De 3 a 6 nov,` por `Entre 2 e 6 nov,`.
3. **Créditos truncados.** Em `post.json → imagens`:
   - img05: `"autor": "Pavel Hrdlička"`. O crédito atual estoura e encosta em "DIPLOMACIA DA GUERRA".
   - img09: `"autor": "7th Army JMTC"`. Hoje aparece "7th Army Joint Multinational Training...", e a CC BY exige atribuição legível.
4. **Slide 8, foto.** O navio TransPulp mostra em letras grandes os nomes "TRANSPULP" e "TRANSATLANTIC", de uma empresa sueca que não tem relação com o caso. O leitor vai tomá-lo pelo Fitburg, e isso é engano com risco de associar a empresa à sabotagem. Troque a foto:
   - opção A: a foto do próprio navio, `File:Fitburg Kantvik 2.JPG` (Category:IMO 9250397), via `scripts/imagens.py --so img08`, se a licença for livre;
   - opção B: mar ou costa do Golfo da Finlândia sem navio identificável.
   Depois renderize de novo.

## Recomendadas (não bloqueiam)
- Slide 3: troque `Bruxelas montou uma força-tarefa com ENISA e Europol` por `Bruxelas reuniu sua força-tarefa de cibersegurança, com ENISA e Europol`.
- Slide 4: troque `Entre 2 e 3 nov,` por `Em 2 nov,`.
- Legenda: atribua a frase da OTAN, assim: `Segundo briefing do Parlamento britânico, a OTAN e serviços de inteligência avaliam...`. Troque também `O Kremlin chama as acusações de absurdas` por `O Kremlin chama de absurdas as acusações sobre as geladeiras`.
- Slide 2: a foto é de um freezer de supermercado com marcas americanas. Serve como ilustração genérica, mas uma foto de loja europeia seria melhor.
- O slug diz 13 nov, mas o post sai em 10 nov (e a pauta fala em "dia de Reel"). É só interno, não precisa renomear às pressas.
- A rede desta sessão não alcança `commonslibrary.parliament.uk` nem `commons.wikimedia.org`. O briefing foi conferido só pelo resultado de busca, e a licença da foto do Fitburg ainda precisa ser conferida.
