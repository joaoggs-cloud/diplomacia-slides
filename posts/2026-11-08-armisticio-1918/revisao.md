REPROVADO

Revisão de `posts/2026-11-08-armisticio-1918` no SHA c67eb07 (revisor, 06 nov 2026). Os problemas são de correção pontual (rodada 1).

| Item | Resultado |
|---|---|
| 1. Fatos | problema (slide 2: signatários; slide 7: vagão de 1950 e réplica tratados como duas coisas) |
| 2. Isenção | ok |
| 3. Imagens / licenças | problema (crédito do Bundesarchiv incompleto no slide 6). Todas PD ou CC BY-SA, nenhuma de agência |
| 4. Texto | ok (máx. ~42 palavras/slide, 1 título + CTA, 1 factbox, sem emoji nem pergunta) |
| 5. Visual | ok com ressalvas (ver recomendações) |
| 6. Legenda | ok (1.153 caracteres com fontes e hashtags) |
| Layout | ok: P&B justificado (1918/1940), slide 7 em cor, texto legível |

## Fatos conferidos por conta própria (WebSearch, fontes não-Wikipedia)
- Assinatura por volta das 5h (5h10 a 5h20), vigência às 11h: ok (FRUS/history.state.gov, Long Long Trail, germanhistorydocs).
- Condições entregues em 8 nov, protesto alemão, ordem de assinar: ok (Long Long Trail, History Learning Site).
- 5.000 canhões / 25.000 metralhadoras / 3.000 morteiros: ok, é o texto oficial (FRUS 1919, germanhistorydocs). Jornais de 1918 trazem 30.000/2.000, versão preliminar.
- 34 cláusulas: ok, há fonte que conta 35; manter.
- Ocupação da margem esquerda com Mainz, Coblença e Colônia; bloqueio mantido (cláusula XXVI): ok.
- Gunther às 10h59, "considerado o último": ok (Time, Military.com; Pershing o citou como último americano morto).
- Exibição em Berlim a partir de 5 jul 1940; destruição em 1945, provavelmente pela SS: ok (musee-armee.fr, history.co.uk).
- 2439 D em 1950, abertura em 11 nov 1950: ok (fontes francesas, armistice-museum.com).
- **Signatários: problema.** Foch e Wemyss **assinaram** pelos Aliados; Erzberger assinou com outros três delegados alemães. "assinou diante do marechal Foch" dá a entender que Foch só assistiu.

## Correções obrigatórias (aplicar exatamente)
1. **Slide 2 (`slides[0].texto_html`)**: troque a segunda frase por:
   `Por volta das <strong>5h</strong> de 11 nov 1918, a delegação alemã chefiada por Matthias Erzberger assinou o texto com o marechal Foch e o almirante britânico Wemyss.`
2. **Slide 6, crédito (licença CC BY-SA do Bundesarchiv)**: em `imagens[img06].autor` use
   `Bundesarchiv, B 145 Bild-P50284 / Carl Weinrother` (assim o slide e a legenda saem com o crédito pedido pelo Bundesarchiv).
3. **Slide 6 (`slides[4].texto_html`)**: identifique quem aparece na foto. Texto exato:
   `Em 22 jun 1940, Hitler obrigou a França a assinar o armistício no mesmo vagão, retirado do museu. O general Charles Huntziger assinou pelos franceses. O memorial da clareira foi destruído e a carruagem seguiu para Berlim, exibida a partir de 5 jul 1940.`
4. **Slide 7 (`slides[5].texto_html`)**: o vagão de 1950 **é** o que está exposto hoje, não há uma segunda réplica. Texto exato:
   `A carruagem original foi destruída em 1945, provavelmente pela SS. Em 11 nov 1950, um vagão da mesma série, montado com os objetos originais, foi instalado na clareira. É ele que está exposto hoje no memorial de Compiègne.`
5. Renderize de novo (slides e story) e reenvie para revisão.

## Pontos levantados pelo roteirista (nenhum é bloqueante)
- **Slide 4, ponte de Remagen**: não bloqueia. É uma foto de 1918 de tropas aliadas cruzando o Reno durante a ocupação (Remagen fica na zona americana, ao norte de Coblença), e o texto não diz que a foto é de Mainz, Coblença ou Colônia. Fica.
- **Slide 5, soldados comemorando sobre texto de mortes**: não bloqueia. A foto registra a reação ao cessar-fogo das 11h, que o texto menciona. Não há vítima nem violência, e o contraste serve à história.
- **Slide 6, Huntziger não nomeado**: resolvido pela correção 3.
- **Slide 7, número de página pouco legível**: não bloqueia; recomendável (ver abaixo).
- **Slide 3, borda do scan**: não bloqueia; recomendável (ver abaixo).

## Recomendações (opcionais)
- Slide 5 e legenda: dá para trocar "Segundo estimativas citadas pela imprensa britânica, milhares de homens morreram" por "Segundo o historiador Joseph Persico, cerca de 2.700 soldados morreram naquela manhã" (a estimativa é do livro de Persico, repetida pela AP, PBS e Daily Mail), que fica mais preciso e mais forte. Na legenda: "segundo o historiador Joseph Persico".
- Slide 4: "até o tratado de paz final" → "até depois do Tratado de Versalhes, em 1919".
- Legenda: "Hitler fez a França assinar sua rendição" → "Hitler fez a França assinar o armistício".
- Slide 7: a pílula "7/8" some sobre a árvore escura. Escureça o fundo da pílula ou desloque o `foco` da imagem para o céu ficar atrás dela.
- Slide 3: a borda e o rasgo do papel aparecem no topo. Ajuste o `foco` (ex.: "70% 55%") ou dê um zoom leve para cortar a margem.
