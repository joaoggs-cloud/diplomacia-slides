# Diagnóstico de crescimento: por que a conta não sai de 21 seguidores

Data: 20 nov 2026 · Dados do Metricool (blogId 7647378) de 20 out a 20 nov, puxados hoje
(todas as chamadas funcionaram). Brutos em `analytics/dados/posts-2026-11-20.json` e `conta-2026-11-20.json`.
Nada em `config/estrategia.json` foi alterado.

## Resposta curta

A conta não cresce porque **quase ninguém fora dos 21 seguidores vê os posts**. Cada post chega a
cerca de 6 contas, nunca mais de 11, e nenhum Reel foi publicado até hoje. Quem vê interage, mas
sem alcance novo não existe seguidor novo. Há também **10 dias sem post** desde 25 out, 3 deles
seguidos (13 a 15 nov), o que enfraquece o pouco sinal que a conta gera. O conteúdo não parece ser
o problema; o problema é distribuição e tamanho do ponto de partida (conta nova, sem rede inicial).

## Números (o que os dados mostram)

| Indicador | Valor |
|---|---:|
| Seguidores | 22 (24 out) → 21 (desde 25 out), 21 hoje |
| Seguidores ganhos / perdidos no período | 0 ganhos registrados nos 26 posts; saldo -1 |
| Posts no feed medidos (25 out a 17 nov) | 26 (20 carrosséis, 6 imagens únicas) |
| Alcance médio por post | **6,2 contas** (mediana 6; mín. 3; máx. 11) |
| Alcance médio desde 1 nov (12 posts) | 5,5 |
| Alcance médio: carrossel / imagem única | 5,8 / 7,7 (imagens únicas eram eleição/notícia) |
| Alcance médio do dia da conta | 7,9; pico 18 (25 out, dia de eleição); nunca acima de 18 |
| Visualizações médias por post | 20,9 (~3,4 por conta alcançada) |
| Interações totais | 45: 39 curtidas, 4 comentários, **1 salvamento, 1 compartilhamento** |
| Taxa de interação sobre o alcance | 9% a 80% por post; no geral ~28% (45 interações / 161 de alcance somado) |
| Stories (amostra até 2 nov, 27 stories) | alcance médio ~9,5; só chegam a seguidores |
| Reels | **0 publicados** (consulta IGRE retorna vazio) |
| Visitas ao perfil e taxa visita → seguidor | **Indisponível**: o Metricool deprecou o campo (IGEV07) e não há outro |
| Alcance de não seguidores | **Indisponível** na API para posts/conta |

Lido assim: o alcance do dia da conta (média 7,9, máximo 18) nunca passou do número de seguidores (21).
Isso é compatível com alcance praticamente só de seguidores (hipótese, ver abaixo).

## Regularidade real de publicação

Dias com post no feed (fuso BRT, segundo o Metricool): 25, 26, 27, 28, 29 out; 1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 16 e 17 nov.
**Dias sem post entre 25 out e 20 nov: 10 de 27.**

| Lacuna | Causa |
|---|---|
| 30 e 31 out | falhas de agendamento, reagendados e saíram 4 e 5 nov |
| 3 nov | sem post |
| 9 nov | sem post |
| 13, 14 e 15 nov | posts (lasers antidrone, muro de Berlim, Irã/Ormuz) com ERROR: limite da conta Metricool; status `falha_publicacao` |
| 18, 19 e 20 nov | posts aprovados (`aprovado_manual`), mas **ainda não aparecem no Metricool**. Os de 16 e 17 nov apareceram em menos de 1 dia, então ou o João ainda não postou ou o Metricool não sincronizou. A confirmar com ele |

Desde 16 nov o João posta manualmente. Os Reels previstos (seg, qua, sex) **nunca saíram**: o limite da conta
bloqueou os rascunhos de Reel e, na fase manual, só há carrossel.

## Causas prováveis

### O que os dados mostram
1. **Alcance minúsculo e estável**: 26 posts, 3 a 11 contas, sem tendência de alta (média 6,2 nos primeiros posts, 5,5 desde 1 nov). O algoritmo não está testando a página com ninguém de fora.
2. **Sem Reels**: é o único formato que o Instagram usa para mostrar conta pequena a desconhecidos. Zero Reels, zero chance dessa via.
3. **Sinais fracos para o algoritmo**: 1 salvamento e 1 compartilhamento em 26 posts. Curtida pesa pouco.
4. **Zero seguidores ganhos** em todos os posts, e a conta perdeu 1 em 25 out.
5. **Irregularidade**: 10 dias sem post, incluindo 3 seguidos; o dia sem post tem alcance 0 a 1.
6. **Mistura de temas** nos primeiros 15 dias: 9 dos 26 posts foram política e economia do Brasil (eleição, B3, dívida), fora do núcleo guerra/geopolítica. Desde 4 nov o tema está concentrado.
7. **Horário**: não é a causa. Alcance em 06:01 (5 a 7) é igual ao de posts em outras horas; o Metricool não tem dados de melhor horário.

### Hipóteses (não dá para provar com esta API)
- **Conta nova e sem rede**: com 21 seguidores, provavelmente amigos e conhecidos, a conta não tem histórico para o algoritmo recomendar.
- **Quase todo alcance vem de seguidores**: o teto de 18 contas/dia sugere isso, mas o Metricool não separa seguidor de não seguidor.
- **Perfil/bio**: sem acesso ao perfil não dá para avaliar; se a bio não diz o que a página entrega, quem chega não segue.
- **Hashtags**: 7 a 12 por post, no fim da legenda. Em conta de 21 seguidores o efeito é pequeno; não há dado para dizer se ajudam ou atrapalham.
- **Capa pouco "compartilhável"**: posts longos, muito bem fontados, mas sem gancho que a pessoa mande a um amigo. Os poucos números não permitem testar.
- **Nicho e idioma**: geopolítica em português é um nicho com grandes páginas já estabelecidas; sem colaborações nem comentários em páginas maiores, a conta é invisível.
- **Primeira hora sem interação**: os posts saem às 06:01 para 21 contas, a maioria dormindo; o sinal inicial é quase nulo.

## Recomendações priorizadas (além do que o sistema já faz)

1. **Publicar os Reels e confirmar que saem.** Meta: 3 Reels na semana de 24 a 30 nov (seg, qua, sex) e 3 na seguinte; cada um acima de 100 contas alcançadas. Se o Metricool continua no limite, o João posta o `reel.mp4` pelo app como "Reel de teste". Com a voz dele, melhor.
2. **15 min por dia de interação ativa (todo dia, antes do post sair).** Comentar com conteúdo em 5 posts de páginas grandes de geopolítica e história militar, responder todo comentário e seguir/curtir quem interage. Meta: 10 comentários/dia, 140 em duas semanas.
3. **Semear a primeira audiência pela rede do João.** Mandar o carrossel do dia no WhatsApp e em 3 a 5 grupos de interesse (história, RI, concursos militares) e pedir que salvem/enviem. Meta: 20 novos seguidores até 4 dez; 3 salvamentos ou compartilhamentos por post.
4. **Colaboração.** Convidar 2 páginas pequenas parecidas para post em colaboração. Meta: 2 convites enviados até 27 nov, 1 post em colaboração até 4 dez.
5. **Regularidade sem buracos.** Meta: 14 de 14 dias com post (hoje 17 de 27). Confirmar hoje se os posts de 18, 19 e 20 nov saíram; um dia sem post custa mais que um post fraco.
6. **Perfil pronto para converter.** Bio em uma linha ("Guerras e geopolítica explicadas com fontes, todo dia às 6h"), 3 carrosséis fixados (Crise dos Mísseis, Tsar Bomba, Tirpitz) e destaques. Meta: feito até 22 nov; depois o João me diz quantas visitas ao perfil aparecem em Insights do app (a API não entrega).
7. **Testar capas feitas para compartilhar**: 4 dos próximos 8 carrosséis com capa de comparação, número ou "o erro que…", e último slide pedindo para enviar a alguém. Comparação com os outros 4 por salvamentos e compartilhamentos.

### Metas para 2 semanas (até 4 dez)
- Alcance médio por post acima de 15 (hoje 6,2).
- Pelo menos 1 Reel acima de 100 contas.
- Seguidores: 21 → 40 (meta modesta; ganhos totais a partir de hoje: 19).
- 14 dias com post, 6 Reels, 3 salvamentos+compartilhamentos por post.

## Limites desta análise
- O Metricool não informa visitas ao perfil nem alcance de não seguidores; essa taxa de conversão não pôde ser calculada. O João pode ler esses dois números em Insights do próprio Instagram e passar.
- Amostra pequena (26 posts, alcance 3 a 11): diferenças entre formatos, pilares e horários são ruído, e nenhuma conclusão de "formato vencedor" é segura.
- `IGEV37` (nº de conteúdos) voltou com valores incoerentes com a contagem real; a regularidade acima vem das datas dos posts, não dessa métrica.
