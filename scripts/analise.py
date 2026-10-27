#!/usr/bin/env python3
"""Análise de desempenho dos posts e recomendação de horários/pilares.

Entrada: um JSON salvo pelo Claude a partir de getAnalyticsDataByMetrics do
Metricool, no formato {"metricas": ["IGPO02", ...], "rows": [[...], ...]}
(as linhas vêm na mesma ordem das métricas pedidas).

Cruza cada post publicado com o post.json correspondente (pelo horário de
publicação) para saber pilar, slot e nº de slides, e calcula um score de
engajamento que valoriza o que o algoritmo do Instagram mais distribui:
salvamentos e compartilhamentos.

Uso:
    python3 scripts/analise.py analytics/dados/posts-2026-11-01.json [--aplicar]
"""
import argparse
import json
import statistics
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

RAIZ = Path(__file__).resolve().parent.parent
ESTRATEGIA = RAIZ / "config" / "estrategia.json"
DIAS = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]

CAMPOS = {
    "IGPO02": "data_hora", "IGPO03": "texto", "IGPO06": "url", "IGPO07": "tipo",
    "IGPO14": "alcance", "IGPO28": "views", "IGPO13": "likes", "IGPO08": "comentarios",
    "IGPO15": "salvos", "IGPO27": "compartilhamentos", "IGPO12": "interacoes",
    "IGPO10": "engajamento", "IGPO29": "seguidores_ganhos",
}
NUMERICOS = {"alcance", "views", "likes", "comentarios", "salvos", "compartilhamentos",
             "interacoes", "engajamento", "seguidores_ganhos"}
MIN_POR_GRUPO = 3   # abaixo disso a média é ruído
MIN_PARA_OTIMIZAR = 9


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def score(p):
    """Interações ponderadas por 100 pessoas alcançadas."""
    pesos = p["likes"] + 2 * p["comentarios"] + 3 * p["salvos"] + 4 * p["compartilhamentos"] \
        + 5 * p["seguidores_ganhos"]
    return round(100 * pesos / max(p["alcance"], 1), 2)


def parse_data(v, tz):
    v = str(v)
    if len(v) == 14 and v.isdigit():  # formato do Metricool: AAAAMMDDHHMMSS em UTC
        return datetime.strptime(v, "%Y%m%d%H%M%S").replace(tzinfo=ZoneInfo("UTC")).astimezone(tz)
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y%m%d%H%M", "%Y%m%d"):
        try:
            dt = datetime.strptime(v, fmt)
            return dt if dt.tzinfo else dt.replace(tzinfo=tz)
        except ValueError:
            continue
    return datetime.fromisoformat(v).astimezone(tz)


def carregar_publicados(arquivo, tz):
    dados = json.loads(Path(arquivo).read_text(encoding="utf-8"))
    out = []
    for row in dados["rows"]:
        p = {}
        for mid, valor in zip(dados["metricas"], row):
            campo = CAMPOS.get(mid)
            if campo:
                p[campo] = num(valor) if campo in NUMERICOS else valor
        for c in NUMERICOS:
            p.setdefault(c, 0.0)
        if not p.get("data_hora"):
            continue
        p["dt"] = parse_data(p["data_hora"], tz)
        out.append(p)
    return out


def casar_com_repositorio(publicados, tz):
    locais = []
    for f in (RAIZ / "posts").glob("*/post.json"):
        post = json.loads(f.read_text(encoding="utf-8"))
        quando = post.get("agendamento", {}).get("data_hora")
        if quando:
            locais.append((datetime.fromisoformat(quando).astimezone(tz), f.parent, post))
    for p in publicados:
        candidatos = [l for l in locais if abs(l[0] - p["dt"]) <= timedelta(minutes=30)]
        if candidatos:
            dt, pasta, post = min(candidatos, key=lambda l: abs(l[0] - p["dt"]))
            p["slug"] = post["slug"]
            p["pilar"] = post.get("pilar", "?")
            p["slides"] = len(post.get("slides", [])) + 2
            p["pasta"] = pasta
        else:
            p["slug"], p["pilar"], p["slides"], p["pasta"] = None, "fora_do_sistema", None, None
        p["slot"] = p["dt"].strftime("%H:%M")
        p["dia"] = DIAS[p["dt"].weekday()]
        p["faixa"] = f"{p['dt'].hour:02d}h"
        p["score"] = score(p)


def agrupar(publicados, chave):
    grupos = defaultdict(list)
    for p in publicados:
        grupos[p[chave]].append(p["score"])
    return {k: {"n": len(v), "media": round(statistics.mean(v), 2)} for k, v in grupos.items()}


def tabela(titulo, grupos):
    linhas = [f"### {titulo}", "", "| Grupo | Posts | Score médio |", "|---|---:|---:|"]
    for k, g in sorted(grupos.items(), key=lambda kv: -kv[1]["media"]):
        aviso = "" if g["n"] >= MIN_POR_GRUPO else " *(poucos dados)*"
        linhas.append(f"| {k}{aviso} | {g['n']} | {g['media']} |")
    return "\n".join(linhas)


def recomendar(publicados, est):
    rec = {"alteracoes": [], "observacoes": []}
    medidos = [p for p in publicados if p["slug"]]
    if len(medidos) < MIN_POR_GRUPO:
        rec["observacoes"].append(
            f"Só {len(medidos)} post(s) do sistema com métricas — mantenha a exploração.")
        return rec

    # Horário: considera slot pelo horário configurado (±30 min).
    por_slot = defaultdict(list)
    for p in medidos:
        slot = min(est["horarios"]["slots"], key=lambda s: abs(
            int(s[:2]) * 60 + int(s[3:]) - (p["dt"].hour * 60 + p["dt"].minute)))
        por_slot[slot].append(p["score"])
    validos = {s: statistics.mean(v) for s, v in por_slot.items() if len(v) >= MIN_POR_GRUPO}
    if est["horarios"].get("fixo"):
        # Horário definido pelo João: a análise só recomenda (ver tabela "Faixa horária").
        rec["observacoes"].append("Horário fixo em " + ", ".join(est["horarios"]["slots"])
                                  + " por decisão do João; mudanças só por recomendação.")
        validos = {}
    if validos:
        melhor = max(validos, key=validos.get)
        if melhor != est["horarios"].get("melhor_slot"):
            rec["alteracoes"].append(("horarios.melhor_slot", melhor))
        if len(medidos) >= MIN_PARA_OTIMIZAR and est.get("fase") != "otimizacao":
            rec["alteracoes"].append(("fase", "otimizacao"))
        piores = [s for s, m in validos.items() if m < 0.6 * validos[melhor]]
        for s in piores:
            rec["observacoes"].append(
                f"Slot {s} rende {validos[s]:.1f} vs {validos[melhor]:.1f} do melhor — "
                "considere trocá-lo por um horário novo para continuar testando.")

    # Pilares: desloca até 0,05 de peso por semana em direção aos melhores.
    pilares = agrupar(medidos, "pilar")
    pesos = dict(est["pesos_pilares"])
    validos_p = {k: v["media"] for k, v in pilares.items() if v["n"] >= 2 and k in pesos}
    if len(validos_p) >= 2:
        media_geral = statistics.mean(validos_p.values())
        for k, m in validos_p.items():
            delta = 0.05 if m > media_geral * 1.15 else -0.05 if m < media_geral * 0.85 else 0
            pesos[k] = min(0.5, max(0.05, round(pesos[k] + delta, 2)))
        total = sum(pesos.values())
        pesos = {k: round(v / total, 2) for k, v in pesos.items()}
        if pesos != est["pesos_pilares"]:
            rec["alteracoes"].append(("pesos_pilares", pesos))
    return rec


def aplicar(est, rec, data):
    for caminho, valor in rec["alteracoes"]:
        alvo = est
        *pais, folha = caminho.split(".")
        for p in pais:
            alvo = alvo[p]
        alvo[folha] = valor
    if rec["alteracoes"]:
        est["historico_ajustes"].append({
            "data": data,
            "motivo": "Análise semanal: " + "; ".join(f"{c} → {v}" for c, v in rec["alteracoes"]),
        })
    ESTRATEGIA.write_text(json.dumps(est, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dados")
    ap.add_argument("--aplicar", action="store_true", help="grava as alterações em config/estrategia.json")
    args = ap.parse_args()

    est = json.loads(ESTRATEGIA.read_text(encoding="utf-8"))
    tz = ZoneInfo(est["metricool"]["timezone"])
    publicados = carregar_publicados(args.dados, tz)
    casar_com_repositorio(publicados, tz)
    hoje = datetime.now(tz).date().isoformat()

    for p in publicados:
        if p["pasta"]:
            (p["pasta"] / "metricas.json").write_text(json.dumps(
                {k: v for k, v in p.items() if k not in ("dt", "pasta")} | {"coletado_em": hoje},
                ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")

    rec = recomendar(publicados, est)
    ranking = sorted(publicados, key=lambda p: -p["score"])
    rel = [f"# Relatório de desempenho — {hoje}", "",
           f"Posts analisados: **{len(publicados)}** · Score = interações ponderadas "
           "(like 1, comentário 2, salvo 3, compartilhamento 4, seguidor 5) por 100 contas alcançadas.", "",
           "## Ranking", "", "| Post | Data | Alcance | Salvos | Compart. | Score |", "|---|---|---:|---:|---:|---:|"]
    for p in ranking:
        nome = p["slug"] or (p.get("texto") or "")[:40]
        rel.append(f"| {nome} | {p['dt']:%d/%m %H:%M} ({p['dia']}) | {p['alcance']:.0f} | "
                   f"{p['salvos']:.0f} | {p['compartilhamentos']:.0f} | {p['score']} |")
    rel += ["", "## Por recorte", "",
            tabela("Faixa horária", agrupar(publicados, "faixa")), "",
            tabela("Dia da semana", agrupar(publicados, "dia")), "",
            tabela("Pilar de conteúdo", agrupar(publicados, "pilar")), "",
            "## Recomendações automáticas", ""]
    rel += [f"- Alterar `{c}` → `{json.dumps(v, ensure_ascii=False)}`" for c, v in rec["alteracoes"]] \
        or ["- Nenhuma alteração automática nesta semana."]
    rel += [f"- {o}" for o in rec["observacoes"]]

    saida = RAIZ / "analytics" / f"relatorio-{hoje}.md"
    saida.write_text("\n".join(rel) + "\n", encoding="utf-8")
    print(saida)
    print(json.dumps({"alteracoes": rec["alteracoes"], "observacoes": rec["observacoes"]},
                     ensure_ascii=False, indent=2))
    if args.aplicar:
        aplicar(est, rec, hoje)


if __name__ == "__main__":
    main()
