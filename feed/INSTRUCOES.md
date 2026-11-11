# Feed geopolítico diário — manual do Claude

Briefing diário para o João: as principais notícias geopolíticas do dia **e o que os
principais analistas brasileiros e internacionais estão dizendo sobre elas**.
É leitura pessoal do João (e matéria-prima de pauta para a @diplomaciadaguerra),
**não é post**: nada daqui vai para o Metricool.

Roda sozinho todo dia às **06:38 (America/Sao_Paulo)** como tarefa agendada do Claude
Code; cada execução abre uma sessão nova e o João recebe uma notificação no celular
quando termina.

## Arquivos

| Arquivo | Para quê |
|---|---|
| `feed/INSTRUCOES.md` | Este manual. |
| `feed/analistas.json` | Lista de analistas (BR e internacionais) com onde cada um publica. Pode crescer: acrescente quem aparecer com frequência nas fontes. |
| `feed/historico.json` | Quem foi citado e quais veículos foram usados em cada edição — serve para **variar** as vozes e as fontes. |
| `feed/edicoes/AAAA-MM-DD.md` | A edição do dia. |

Branch: `claude/blissful-mayer-tl63ws` (separado do sistema do Instagram para não
interferir nas rotinas de post).

## Passo a passo

1. `git fetch origin claude/blissful-mayer-tl63ws && git checkout claude/blissful-mayer-tl63ws && git pull`.
   Leia `analistas.json`, `historico.json` e as **3 últimas edições** (para não repetir
   notícia sem fato novo — se o assunto continua, diga o que mudou).
2. **Notícias (últimas 24–36 h).** WebSearch em modo `extended`, várias buscas no mesmo
   turno: guerras em curso (Ucrânia, Oriente Médio, Sudão…), EUA/China, Rússia/OTAN,
   Indo-Pacífico, América Latina, África, eleições e cúpulas, energia/sanções/comércio,
   e **o Brasil no mundo** (Itamaraty, Planalto, BRICS, Mercosul).
   Escolha **5 a 7** notícias por relevância internacional e interesse para o Brasil.
   Cada fato com **2 fontes independentes confiáveis**; fato com uma fonte só entra
   como "não confirmado" ou fica de fora.
3. **Varie as fontes.** Misture a cada dia veículos de regiões e linhas diferentes
   (ex.: Reuters, AP, AFP, BBC, FT, The Economist, NYT, WaPo, WSJ, Le Monde, El País,
   DW, Al Jazeera, SCMP, Nikkei Asia, The Hindu, Meduza, Kyiv Independent, Haaretz,
   Folha, Estadão, O Globo, Valor, Agência Brasil, CNN Brasil; think tanks: Crisis Group,
   ISW, CSIS, Chatham House, ECFR, Carnegie, Brookings, IISS, CEBRI). Consulte
   `historico.json`: evite que o mesmo veículo seja a fonte principal em mais de
   2 notícias da edição, e traga ao menos 1 veículo não ocidental e 1 brasileiro.
   Quando a cobertura de um lado (ex.: mídia russa, chinesa, iraniana) for relevante
   para entender a notícia, cite **como versão daquele governo**, sem tratá-la como fato.
4. **O que dizem os analistas.** Para as notícias principais, procure declarações,
   artigos, colunas, entrevistas, podcasts ou posts **dos últimos 7 dias** de nomes de
   `analistas.json` (e de outros especialistas reconhecidos que apareçam).
   - **3 a 4 brasileiros** e **3 a 4 internacionais**, com perspectivas diferentes
     (realistas e liberais; ocidentais, Rússia/China, Sul Global).
   - **Rodízio:** prefira quem não foi citado nas últimas 5 edições, mas relevância vem
     antes do rodízio.
   - **Regra inegociável: nunca invente nem "reconstrua" opinião.** Só entra o que a
     pessoa disse de fato, com link e data. Citação literal entre aspas só se ela
     estiver no texto da fonte; caso contrário, paráfrase fiel ("Para Stuenkel, …").
     Se não achar nada recente de alguém, não cite essa pessoa — escolha outra.
     Uma posição antiga e conhecida pode aparecer só se marcada como tal
     ("em artigo de março, …").
   - Diga em uma linha onde cada um se situa (ex.: "realista, crítico da expansão da
     OTAN"; "ex-chanceler"), para o João calibrar a leitura.
5. **Escreva** `feed/edicoes/AAAA-MM-DD.md` no formato abaixo. Tom sério, direto,
   português do Brasil, sem emoji, sem sensacionalismo, sem tomar partido.
6. **Atualize** `historico.json` (acrescente a edição: data, notícias, analistas
   citados, veículos usados). Se descobrir um analista relevante que não está na
   lista, acrescente em `analistas.json`.
7. `git add feed && git commit -m "Feed geopolítico AAAA-MM-DD" && git push -u origin claude/blissful-mayer-tl63ws`.
8. **Termine a sessão com a edição completa na resposta final** (é o que o João lê
   no app ao tocar na notificação). A primeira linha da resposta é o resumo para a
   notificação: "Feed geopolítico DD mmm: <manchete 1>; <manchete 2>; <manchete 3>".

## Formato da edição

```markdown
# Feed geopolítico — 12 nov 2026

**Em uma frase:** <o fio que liga o dia>.

## As notícias

### 1. <Manchete objetiva>
<3–5 linhas: o que aconteceu, quem, onde, números com fonte.>
**Por que importa:** <1–2 linhas, inclusive para o Brasil quando couber.>
Fontes: [Veículo A](url) · [Veículo B](url)

### 2. …

## O que dizem os analistas

**Brasil**
- **Nome** (instituição; linha em poucas palavras) — sobre <notícia>: <citação ou
  paráfrase fiel>. [Fonte, data](url)
- …

**Mundo**
- **Nome** (instituição; linha) — …

**Onde eles divergem:** <2–3 linhas comparando as leituras: quem vê escalada,
quem vê blefe, o que cada um acha que o Brasil deveria fazer.>

## No radar
<Próximos 7 dias: cúpulas, votações, prazos, eleições, efemérides militares.>

## Ideia de pauta para a @diplomaciadaguerra
<1 tema com gancho, pilar sugerido e por que renderia — só sugestão; a Rotina A decide.>
```

Tamanho: o suficiente para ler em 5–7 minutos. Qualidade e checagem acima de volume.
