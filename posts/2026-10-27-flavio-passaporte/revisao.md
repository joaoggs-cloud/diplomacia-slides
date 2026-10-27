REPROVADO

Revisão de 26 out 2026, 22h50 (Brasília), commit 85f5b4b. Os erros são pequenos e se corrigem em minutos, sem precisar renderizar de novo: só `legenda` e `imagens[0].autor`. Se o roteirista também aplicar a recomendação R1 (gancho), aí precisa renderizar.

| Item | Resultado |
|---|---|
| 1. Fatos (2 fontes, atribuição) | ok, com 1 ajuste recomendado (R3) |
| 2. Isenção | ok (R1 equilibra melhor o card) |
| 3. Imagem / licença / crédito | **problema** (P2) |
| 4. Texto (ortografia, sem emoji, sem cara de IA) | ok; gancho de 58 palavras, legível mas denso (R1) |
| 5. Visual (slides/01.jpg) | ok |
| 6. Legenda (payload, tamanho) | **problema** (P1); payload roda sem erro (rc=0), cerca de 1.350 caracteres, abaixo de 2.200 |
| Atualidade (fato novo?) | ok até 22h50 de 26 out: nenhuma fonte confirma entrega feita nem recurso apresentado |

## Checagem própria (WebSearch, modo extended)
- Moraes mandou entregar os passaportes comum e diplomático à PF em 24 h, proibiu a saída do país e o contato com Willer Tomaz, e o caso foi divulgado na segunda (26): confirmado por Agência Brasil, Exame, CNN Brasil, Poder360, Gazeta do Povo e Diario de Pernambuco.
- Inquérito por suspeita de lavagem de dinheiro: confirmado (Agência Brasil, Gazeta). Várias fontes (Exame, Fórum, Jovem Pan) citam também **evasão de divisas**. O texto não está errado, só incompleto. Opcional: "lavagem de dinheiro e evasão de divisas".
- Posição do senador (nunca planejou sair, chama de intimidação, vai entregar e se defender): confirmado (CNN, Poder360, CartaCapital, Metrópoles).
- Defesa de Tomaz: contesta as medidas, chama de desproporcionais, nega vínculo com Flávio e nega irregularidades (Jovem Pan, Focus). "Nega ilegalidade" está correto.
- Fato novo: nenhuma fonte confirma a entrega dos passaportes nem um recurso formal. Uma fonte isolada fala em "confirmação da entrega", mas sem segunda fonte. Na terça (27), o prazo de 24 h deve vencer perto da hora do post (08:01). O publicador precisa refazer a busca logo antes do agendamento. Se a entrega estiver confirmada em 2 fontes, acrescentar à legenda: "O senador entregou os passaportes na terça-feira (27), segundo [fonte 1] e [fonte 2]."
- Termo "apreensão": não aparece. Ok.

## Problemas (correção exata)

**P1. Legenda com bloco de fontes e créditos duplicado, e com crédito errado.** O `metricool.py` já acrescenta "Fontes: …" e "Imagens via Wikimedia Commons: …". Do jeito que está, o post sai com duas linhas "Fontes:", e a linha automática diz "Demais: domínio público", o que não vale aqui porque só há uma imagem.
Correção: em `post.json → legenda`, apagar o trecho final
`\n\nFotos: Agência Senado / Wikimedia Commons, conforme crédito na imagem.\nFontes: Agência Brasil, Poder360, CNN Brasil.`
(a legenda passa a terminar em "…onde prefere se informar."). Se o `metricool.py` acrescentar "Demais: domínio público" mesmo com uma imagem só, o roteirista ou o coordenador deve corrigir o script para omitir esse trecho quando todas as imagens tiverem crédito.

**P2. O crédito da foto não traz o autor.** Pela página do Commons, a foto (original do Flickr do Senado Federal, 17 fev 2025) é de **Pedro França/Agência Senado**, e a licença CC BY 2.0 exige o crédito ao autor. "Agência Senado from Brasilia, Brazil" é só o nome da conta do Flickr. A licença CC BY 2.0 está confirmada. A foto é colorida, mostra a fachada do STF sem pessoas e combina com o título.
Correção: em `post.json → imagens[0].autor`, trocar por `"Pedro França/Agência Senado"` e renderizar de novo (o crédito do slide passa a ser "Foto: Pedro França/Agência Senado · CC BY 2.0").

## Recomendações (não bloqueiam, mas melhoram)

**R1. Gancho mais curto e mais equilibrado.** Hoje são 58 palavras em 6 linhas: dá para ler, mas fica denso para um card de notícia. Além disso, só a defesa de Flávio aparece no card, e Tomaz, apresentado como investigado, fica sem voz. Versão exata, com 50 palavras:
`Ele também fica proibido de sair do país e de falar com o advogado Willer Tomaz. Os dois são investigados por suspeita de lavagem de dinheiro e negam irregularidades. O senador diz que nunca planejou deixar o Brasil, chama a ordem de intimidação e vai entregar os documentos e contestar.`
("Medida cautelar, não condenação" continua na legenda e no quadro "Investigado / Decisão sob sigilo".)

**R2. Título.** A decisão é monocrática (do ministro Moraes), não do plenário. Para ser mais preciso, o roteirista pode trocar por: `Moraes (STF) manda senador <span class="hl2">Flávio Bolsonaro (PL)</span> entregar passaportes à PF`. Opcional: "STF manda" também é usado pela imprensa.

**R3. Fundamento.** As reportagens dizem que foi o próprio senador quem atribuiu a decisão à fala de Eduardo. Na legenda, trocar "segundo a imprensa, o fundamento teria relação" por "segundo o senador e a imprensa, o fundamento teria relação".

**R4. Agendamento.** `2026-10-27T08:01` (slot extra) ainda está no futuro e é coerente com "segunda-feira (26)". Se passar para outro dia, trocar por "na segunda-feira (26 out)".

## O que está ok
- Isenção: sem adjetivos, sem foto de político, nome e partido presentes (PL; PL-RJ na legenda), posição do senador e da defesa de Tomaz incluídas. A pergunta e o primeiro comentário não pedem preferência.
- Nenhum emoji na legenda nem no primeiro comentário. Ortografia e concordância ok. Hashtags neutras, `usar_hashtags_base: false`.
- Visual: nada cortado, título legível sobre o céu e as colunas, degradê não cobre nada importante, crédito presente no rodapé, quadros alinhados.
