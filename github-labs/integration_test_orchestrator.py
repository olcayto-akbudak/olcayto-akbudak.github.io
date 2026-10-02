"""Entegrasyon Test DAG Orkestratörü.

Problem: Başarısız ön koşuldan sonraki testleri atlamak ve tekrarın yan etkisini kontrol etmek.
Method: Sanal scheduler, timeout, safe retry, bağımlılık
Invariant: Retry yalnız idempotent veya idempotency_key içeren görevlerde açılır.
Boundary: Yerel sanal görevlerdir; gerçek HTTP transport ve JUnit adaptörü bu sürümde yoktur."""
import heapq, math

def orchestrate(tasks, workers=3):
    byid = {t['id']: t for t in tasks}
    if workers < 1 or len(byid) != len(tasks):
        raise ValueError('workers/ids')
    for t in tasks:
        if any((k not in byid for k in t.get('depends', []))) or not math.isfinite(t['duration']) or t['duration'] <= 0 or (not math.isfinite(t.get('timeout', 60))) or (t.get('timeout', 60) <= 0) or (type(t.get('retries', 0)) is not int) or (t.get('retries', 0) < 0):
            raise ValueError('task contract')
        if t.get('retries', 0) and (not (t.get('idempotent') or t.get('idempotency_key'))):
            raise ValueError('unsafe retry')
    colors = {}

    def visit(k):
        if colors.get(k) == 1:
            raise ValueError('DAG cycle')
        if colors.get(k) == 2:
            return
        colors[k] = 1
        for d in byid[k].get('depends', []):
            visit(d)
        colors[k] = 2
    for k in byid:
        visit(k)
    pending = set(byid)
    running = []
    results = {}
    now = 0
    serial = 0
    log = []

    def start(k, attempt):
        nonlocal serial
        t = byid[k]
        serial += 1
        end = now + min(t['duration'], t.get('timeout', 60))
        heapq.heappush(running, (end, serial, k, attempt))
        log.append({'id': k, 'attempt': attempt, 'start': now, 'end': end})
    while pending or running:
        for k in sorted(list(pending)):
            deps = byid[k].get('depends', [])
            if any((d in results and results[d]['status'] != 'passed' for d in deps)):
                results[k] = {'status': 'skipped', 'attempts': 0}
                pending.remove(k)
            elif all((d in results for d in deps)) and len(running) < workers:
                pending.remove(k)
                start(k, 1)
        if not running:
            if pending:
                raise RuntimeError('unresolved scheduler')
            break
        now, _, k, attempt = heapq.heappop(running)
        t = byid[k]
        timed = t['duration'] > t.get('timeout', 60)
        failed = timed or attempt <= t.get('fail_first', 0) or t.get('actual') != t.get('expected')
        if failed and attempt <= t.get('retries', 0):
            start(k, attempt + 1)
        else:
            results[k] = {'status': 'timeout' if timed else 'failed' if failed else 'passed', 'attempts': attempt, 'finished': now}
    return {'results': results, 'makespan': now, 'execution': log, 'gate': 'PASS' if all((v['status'] == 'passed' for v in results.values())) else 'BLOCK'}

def run(config):
    return orchestrate(config['tasks'], config.get('workers', 3))

import argparse, json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='integration_test_orchestrator_scenario.json')
    parser.add_argument('--output', default='integration_test_orchestrator_report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
