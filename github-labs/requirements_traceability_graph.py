"""Gereksinim ve Test İzlenebilirliği.

Problem: Yüksek riskli gereksinimlerin güncel test kanıtı olmadan sürüme çıkmasını engellemek.
Method: DAG, risk ağırlığı, revision freshness, impact BFS
Invariant: Her gereksinimden erişilebilen güncel başarılı test kapsama sayılır.
Boundary: Bağlantının iş anlamını insan doğrular; grafik tek başına test kalitesini ispatlamaz."""
from collections import deque

def analyze(nodes, edges, changed=()):
    lookup = {n['id']: n for n in nodes}
    if len(lookup) != len(nodes):
        raise ValueError('duplicate node')
    graph = {k: [] for k in lookup}
    reverse = {k: [] for k in lookup}
    for a, b in edges:
        if a not in lookup or b not in lookup:
            raise ValueError('dangling edge')
        graph[a].append(b)
        reverse[b].append(a)
    visiting = set()
    visited = set()

    def visit(k):
        if k in visiting:
            raise ValueError('traceability cycle')
        if k in visited:
            return
        visiting.add(k)
        for x in graph[k]:
            visit(x)
        visiting.remove(k)
        visited.add(k)
    for k in lookup:
        visit(k)

    def descendants(start):
        queue = deque(start)
        seen = set(start)
        while queue:
            for x in graph[queue.popleft()]:
                if x not in seen:
                    seen.add(x)
                    queue.append(x)
        return seen
    coverage = []
    numerator = denominator = 0
    for n in nodes:
        if n['kind'] != 'requirement':
            continue
        risk = n.get('risk', 1)
        if risk <= 0:
            raise ValueError('risk weight')
        tests = [lookup[x] for x in descendants([n['id']]) if lookup[x]['kind'] == 'test']
        passing = [t for t in tests if t.get('status') == 'passed' and t.get('tested_revision', 0) >= n.get('revision', 1)]
        covered = bool(passing)
        denominator += risk
        numerator += risk * covered
        coverage.append({'requirement': n['id'], 'covered': covered, 'tests': [t['id'] for t in tests], 'risk': risk})
    if any((x not in lookup for x in changed)):
        raise ValueError('unknown change')
    return {'coverage': coverage, 'weighted_coverage': numerator / max(1, denominator), 'gate': 'PASS' if all((x['covered'] for x in coverage)) and coverage else 'BLOCK', 'impact': sorted(descendants(changed)), 'orphans': sorted((k for k in lookup if not reverse[k] and lookup[k]['kind'] != 'requirement'))}

def run(config):
    return analyze(config['nodes'], config['edges'], config.get('changed', []))

import argparse, json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='requirements_traceability_graph_scenario.json')
    parser.add_argument('--output', default='requirements_traceability_graph_report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
