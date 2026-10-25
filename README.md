# diplomacia-slides

Sistema automático de conteúdo para o Instagram **@diplomaciadaguerra**.

```
pesquisa (WebSearch) ─► roteiro (post.json) ─► imagens livres (Wikimedia Commons)
      ─► slides 1080×1080 (render.py) ─► rascunho no Metricool ─► APROVAÇÃO DO JOÃO
      ─► agendamento automático ─► métricas ─► análise semanal ─► nova estratégia
```

- O passo a passo que o Claude segue está em [`CLAUDE.md`](CLAUDE.md).
- A estratégia atual (frequência, horários, pilares) está em
  [`config/estrategia.json`](config/estrategia.json).
- Cada post fica em `posts/<data>-<tema>/` com roteiro, imagens, créditos,
  slides e, depois de publicado, métricas.
- Relatórios semanais em [`analytics/`](analytics/).

## Rodar à mão

```bash
python3 scripts/metricool.py proximo-horario
python3 scripts/imagens.py posts/<slug> --candidatos 3
python3 scripts/render.py posts/<slug>
python3 scripts/metricool.py payload posts/<slug> --sha $(git rev-parse HEAD) --rascunho
python3 scripts/analise.py analytics/dados/posts-<data>.json
```

Dependências: Python 3 com `requests`, `pillow`, `numpy`; Node com `playwright`
(Chromium) para exportar os slides.
