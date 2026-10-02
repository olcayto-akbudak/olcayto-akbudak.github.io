"""Dayanıklı Proje Portföyü Optimizasyonu.

Problem: Birden fazla kaynak bütçesinde en kötü senaryo değerini en yükseğe çıkaran proje setini bulmak.
Method: Exact branch and bound, min-max scenarios, bağımlılık
Invariant: Değerler ve maliyetler negatif olamaz; en fazla 26 aday; hedef min(scenario totals).
Boundary: NP-hard arama büyük portföyde pahalıdır; süre sınırlı MILP çözümü ayrıca gerekir."""
import math

def optimize(items, budgets):
    byid = {x['id']: x for x in items}
    names = sorted(byid)
    dimensions = list(budgets)
    if len(byid) != len(items) or any((not math.isfinite(v) or v < 0 for v in budgets.values())) or len(items) > 26:
        raise ValueError('portfolio size/budget')
    scenario_count = len(items[0]['values']) if items else 1
    for x in items:
        if len(x['values']) != scenario_count or not scenario_count or any((not math.isfinite(v) or v < 0 for v in x['values'])) or any((not math.isfinite(c) or c < 0 for c in x['costs'].values())):
            raise ValueError('values/costs')
        if any((d not in byid for d in x.get('requires', []) + x.get('conflicts', []))) or set(x['costs']) - set(budgets):
            raise ValueError('references/dimensions')
    best = {'score': -1, 'selected': [], 'scenario_values': [], 'costs': {}}
    visited = 0

    def search(index, selected, costs, values):
        nonlocal visited, best
        visited += 1
        upper = min((values[s] + sum((byid[k]['values'][s] for k in names[index:])) for s in range(scenario_count)))
        if upper < best['score']:
            return
        if index == len(names):
            if any((not set(byid[k].get('requires', [])) <= selected for k in selected)):
                return
            score = min(values)
            candidate = sorted(selected)
            if score > best['score'] or (score == best['score'] and candidate < best['selected']):
                best = {'score': score, 'selected': candidate, 'scenario_values': values, 'costs': costs}
            return
        k = names[index]
        x = byid[k]
        search(index + 1, selected, costs, values)
        if any((c in selected for c in x.get('conflicts', []))) or any((k in byid[c].get('conflicts', []) for c in selected)):
            return
        new = {d: costs[d] + x['costs'].get(d, 0) for d in dimensions}
        if any((new[d] > budgets[d] for d in dimensions)):
            return
        search(index + 1, selected | {k}, new, [v + a for v, a in zip(values, x['values'])])
    search(0, set(), dict.fromkeys(dimensions, 0), [0] * scenario_count)
    best['visited_nodes'] = visited
    return best

def run(config):
    return optimize(config['items'], config['budgets'])

import argparse, json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='robust_portfolio_optimizer_scenario.json')
    parser.add_argument('--output', default='robust_portfolio_optimizer_report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
