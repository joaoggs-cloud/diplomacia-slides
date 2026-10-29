REPROVADO

Revisão de posts/2026-11-02-coronel-1914 (SHA 6f5cfc6) — 3 correções curtas; o resto está ok.

| Item | Resultado |
|---|---|
| Fatos: 1 nov 1914, Spee x Cradock ao largo de Coronel | ok (Canadian Encyclopedia, Historyofwar, Dawlish Chronicles) |
| Good Hope e Monmouth afundados sem sobreviventes; Monmouth afundado pelo Nürnberg | ok (worldwar1.co.uk, Canadian Encyclopedia, MercoPress) |
| "cerca de 1.600 mortos" atribuído + 1.570/1.800 | ok (Canadian Encyclopedia "mais de 1.600"; infobox 1.570) |
| Paiol do Good Hope ~19h50 | ok (worldwar1.co.uk + Royal Marines History/WHN da pauta) |
| "Os alemães não perderam nenhum navio nem tiveram mortos" | PROBLEMA: 2 fontes dão "3 feridos" (Masonic Great War Project, Citizendium/infobox); nenhuma diz explicitamente "sem mortos" |
| "Pior derrota em mais de um século" | ok ("first defeat for the RN in more than a century"; "most disastrous defeat for over a hundred years") |
| Malvinas 8 dez 1914; 4 navios afundados; Spee e dois filhos mortos | ok (History Hit, RMG, Britannica) |
| Isenção / tom | ok, sem glorificação |
| Licenças | ok, as 8 em domínio público; crédito em todos os slides |
| Foto x texto | PROBLEMA no slide 7: foto festiva do Monmouth (bandeirolas, salva) sob o texto dos 1.600 mortos |
| P&B | ok, justificado (fotos de 1900–1914); pinturas da capa e dos slides 2, 6 e 8 em cor |
| Texto: máx. 45 palavras (44/32/29/32/34/42/33), sem títulos, sem tag, sem emoji, sem pergunta | ok |
| Ortografia | PROBLEMA pequeno: "terminado pelo" (slide 6) e "Von Spee" (legenda) |
| Visual 01–09: nada cortado, numeração 2/9…9/9, legível | ok |
| Legenda: 531 caracteres; `payload --rascunho` rc=0 | ok |

## Correções exatas

1. **Slide 7 (`slides[5].texto_html`)**: troque
   `Os alemães não perderam nenhum navio nem tiveram mortos.`
   por
   `Do lado alemão, nenhum navio perdido e apenas três feridos.`

2. **Slide 7, imagem**: troque as fotos dos slides 3 e 7 entre si, assim:
   `slides[1].imagem` = `"img07"` (o Monmouth em tempo de paz ilustra a frota de Cradock)
   e `slides[5].imagem` = `"img03"` (a foto sóbria do Good Hope sob o texto das mortes).
   Não é preciso baixar nada; só renderizar de novo.

3. **Texto**:
   - Slide 6 (`slides[4]`): `foi terminado pelo <em>Nürnberg</em>` → `foi afundado pelo <em>Nürnberg</em>`.
   - Legenda: `do vice-almirante Von Spee` → `do vice-almirante von Spee`.

Depois, renderize de novo e faça o commit com `[skip ci]`.
