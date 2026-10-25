# Diplomacia da Guerra — manual de operação do Claude

Este repositório é o sistema que alimenta o Instagram **@diplomaciadaguerra**.
O Claude faz tudo — pesquisa, roteiro, imagens, slides, agendamento e análise —
e o dono da página (João) só **aprova** cada post antes de ele ir ao ar.

Regra de ouro: **nada é publicado sem aprovação explícita do João.** Todo post
entra no Metricool como **rascunho** (`draft: true`) e só vira agendamento
depois de um "aprovar".

## Peças do sistema

| Peça | Para quê |
|---|---|
| `config/estrategia.json` | Frequência, dias, horários (slots), pesos dos pilares, hashtags. A análise semanal reescreve. |
| `posts/<AAAA-MM-DD-slug>/post.json` | Roteiro completo do post: slides, legenda, fontes, buscas de imagem, agendamento, status. |
| `scripts/imagens.py` | Busca e baixa imagens livres (domínio público / CC0 / CC BY / CC BY-SA) no Wikimedia Commons e registra os créditos. |
| `scripts/render.py` | Gera `carrossel.html` + `slides/01.jpg…` (1080×1080) com a identidade visual da página. |
| `scripts/metricool.py` | `proximo-horario` (data/slot da vez), `payload` (JSON para o Metricool), `avancar-slot`. |
| `scripts/analise.py` | Score de engajamento por post, por horário, dia e pilar; recomenda e aplica ajustes. |
| `.github/workflows/gerar-slides.yml` | Plano B: se a sessão não alcança o Wikimedia, o GitHub baixa as imagens e renderiza ao receber o `post.json`. |
| `analytics/` | Dados brutos do Metricool (`dados/`) e relatórios semanais. |

Metricool: `blogId` **7647378**, fuso **America/Sao_Paulo**, rede `instagram`.
As imagens vão para o Metricool como URLs públicas
`https://raw.githubusercontent.com/joaoggs-cloud/diplomacia-slides/<sha>/posts/<slug>/slides/NN.jpg`,
por isso os slides precisam estar **commitados e enviados** antes do agendamento.

Branch de trabalho: `claude/instagram-diplomacia-guerra-automation-zt7ejh`
(o valor oficial está em `config/estrategia.json → repositorio.branch`).
Sempre `git pull` antes de começar e `git push` ao terminar — o estado do
sistema vive no repositório.

### Status de um post (`post.json → status`)
`rascunho` → `aguardando_aprovacao` → `agendado` → `publicado`
(ou `descartado`). Mantenha o status e `metricool.id/uuid` sempre atualizados.

---

## Rotina A — Produzir o próximo post

1. **Preparar.** `git pull`. Leia `config/estrategia.json` e os `post.json` dos
   últimos 30 dias. Se já existem **2 ou mais** posts `aguardando_aprovacao`,
   não crie outro: apenas lembre o João dos pendentes (com as prévias) e pare.
2. **Escolher o pilar** sorteando pelos `pesos_pilares`, evitando repetir o
   pilar dos dois últimos posts. Não repita tema dos últimos 30 dias.
3. **Pesquisar.** Use WebSearch (modo `extended` para atualidades). Para
   `conflito_atual` e `diplomacia`, só use fatos dos últimos 7 dias confirmados
   em **duas fontes confiáveis** (agências, grandes jornais, órgãos oficiais,
   think tanks). Se a atualidade não estiver bem confirmada, troque por um tema
   histórico — de preferência ligado a uma efeméride da semana. Credibilidade é
   o ativo da página: na dúvida, corte o fato.
4. **Roteirizar** o `post.json` (use `posts/2026-10-28-crise-dos-misseis/post.json`
   como modelo de formato):
   - 8 a 10 slides no total (capa + conteúdo + CTA), **máx. 60 palavras** por slide;
   - capa com gancho forte (número, contradição, "o erro que…", "X fatos…");
   - legenda: abertura que prende, contexto em 3–5 linhas, "arraste para o lado",
     e uma **pergunta** no fim para gerar comentários; `primeiro_comentario` com
     outra pergunta; 5–7 hashtags específicas (as de base entram sozinhas);
   - `fontes` com nome e URL; `busca_imagens` em inglês, com `alternativas`;
   - `agendamento` = saída de `python3 scripts/metricool.py proximo-horario`.
5. **Imagens.** `python3 scripts/imagens.py posts/<slug> --candidatos 3`.
   Se falhar por rede (403 / host não encontrado), faça commit + push só do
   `post.json`: o workflow **Gerar slides** baixa as imagens e renderiza.
   Espere com a ferramenta Monitor (loop `until` que faz `git fetch` e testa
   `git cat-file -e origin/<branch>:posts/<slug>/slides/01.jpg`, timeout 15 min)
   e depois `git pull`.
6. **Renderizar** `python3 scripts/render.py posts/<slug>` (se o workflow ainda
   não fez) e **revisar visualmente cada slide** lendo os JPEGs. Confira:
   foto coerente com o título, texto legível, nada cortado, créditos presentes.
   Foto ruim → troque por uma de `imagens/candidatos/` (atualize `imagens` no
   post.json com os dados do `.json` do candidato) ou rode
   `scripts/imagens.py posts/<slug> --so imgNN`, e renderize de novo.
7. **Publicar os arquivos.** Commit + push. Pegue o SHA com `git rev-parse HEAD`
   (o commit precisa conter os slides finais).
8. **Rascunho no Metricool.**
   `python3 scripts/metricool.py payload posts/<slug> --sha <SHA> --rascunho`
   e chame `createScheduledPost` com `blogId`, `date` e `info` (o objeto `info`
   serializado como string JSON). Guarde `id` e `uuid` em `post.json → metricool`,
   mude o status para `aguardando_aprovacao`, rode
   `python3 scripts/metricool.py avancar-slot`, commit + push.
9. **Pedir aprovação.** Envie ao João (SendUserFile, `display: render`) a capa e
   os slides, e escreva: tema, data/hora sugerida, legenda completa e fontes.
   Termine com: **"Responda APROVAR, AJUSTAR (diga o quê) ou DESCARTAR."**
   Avise que ele também pode aprovar direto no app do Metricool (o rascunho
   está no planejador).

## Rotina B — Responder à aprovação

Vale em qualquer sessão: se o João disser "aprovar"/"aprovado"/"pode postar"
(ou ajustar/descartar) sobre um post `aguardando_aprovacao`:

- **APROVAR:** `getScheduledPosts` (fuso America/Sao_Paulo, janela que cubra a
  data do post) para obter `id`/`uuid` atuais; `updateScheduledPost` com o mesmo
  `info` do payload, agora com `draft: false` e `autoPublish: true`. Se a data
  já passou, use o próximo horário de `proximo-horario`. Status `agendado`,
  grave o novo `id`, commit + push. Confirme ao João data e hora.
- **AJUSTAR:** aplique o pedido no `post.json`, renderize, revise, push, novo
  SHA, `updateScheduledPost` mantendo `draft: true`, e mostre de novo.
- **DESCARTAR:** status `descartado`, commit + push, e peça ao João para apagar
  o rascunho no Metricool (a API não apaga posts).

Nunca troque `draft` para `false` sem um "aprovar" do João nesta conversa.

## Rotina C — Análise semanal e ajuste da estratégia

1. `git pull`. Marque como `publicado` os posts `agendado` cuja data já passou.
2. `getAnalyticsDataByMetrics` (brandId 7647378, últimos 60 dias) com as métricas
   `["IGPO02","IGPO03","IGPO06","IGPO07","IGPO14","IGPO28","IGPO13","IGPO08","IGPO15","IGPO27","IGPO12","IGPO10","IGPO29"]`.
   Salve em `analytics/dados/posts-<AAAA-MM-DD>.json` como
   `{"metricas": [...a mesma lista...], "rows": <rows>}`.
3. Evolução da conta (`IGEV01` seguidores, `IGEV06` alcance, `IGEV43`/`IGEV44`
   ganhos/perdas, `IGEV37` nº de posts) dos últimos 60 dias →
   `analytics/dados/conta-<AAAA-MM-DD>.json`.
4. `python3 scripts/analise.py analytics/dados/posts-<data>.json --aplicar`
   (gera `analytics/relatorio-<data>.md`, grava `metricas.json` em cada post e
   ajusta melhor slot, fase e pesos dos pilares).
5. `getBestTimeToPostByNetwork` (instagram, próximos 7 dias). Quando houver
   valores > 0, se o melhor horário do Metricool não estiver entre os slots,
   **substitua o slot de pior desempenho** por ele (a exploração continua).
6. **Frequência** (decida e registre em `historico_ajustes`):
   - alcance médio por post estável ou subindo e posts aprovados em dia → +1
     post/semana (máx. 7);
   - alcance médio por post caiu > 25% em relação às semanas anteriores após
     aumentar a frequência → volte ao valor anterior;
   - João atrasando aprovações (posts vencendo sem aprovação) → −1.
   Ajuste `dias_preferidos` para os dias com melhor score quando houver ≥ 3
   posts por dia.
7. Acrescente no fim do relatório uma seção **"Leitura do Claude"** com 3–5
   conclusões práticas (formato de gancho que mais rendeu, temas que geraram
   salvamentos/compartilhamentos, o que testar na semana seguinte).
8. Commit + push. Envie ao João um resumo curto (seguidores, melhor post,
   o que mudou na estratégia e por quê) e o relatório.

---

## Regras editoriais

- Tom sério, direto, sem sensacionalismo; nunca glorificar violência ou
  desumanizar vítimas. Sem desinformação: todo número tem fonte.
- Português do Brasil, acessível. Datas no formato "22 out 1962".
- Imagens **só** de licença livre (o `imagens.py` filtra). Nunca usar fotos de
  agências (Reuters, AP, Getty) nem de bancos pagos. Créditos ficam no slide e
  na legenda (gerados automaticamente).
- Conteúdo gerado/alterado por IA: as fotos são reais e o texto é editorial;
  `ia_gerado` fica `false` salvo se usarmos imagem gerada por IA.
