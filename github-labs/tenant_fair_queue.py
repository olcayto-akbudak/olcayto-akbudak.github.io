"""Tenant Adil Kuyruk Motoru.

Problem: Bir tenantın pahalı işlerinin diğerlerinin kuyruğunu tek başına tüketmesini önlemek.
Method: Weighted deficit round robin, değişken maliyet
Invariant: Tüm işler başlangıçta hazırdır; adalet tamamlanan maliyet üzerinden ölçülür.
Boundary: Canlı varış, öncelik yaşlandırma ve tenant rate cap bu sürümde bulunmaz."""
from collections import deque
import math

def schedule(tenants, jobs, quantum=2):
    if quantum < 1 or not tenants or any((not math.isfinite(w) or w <= 0 for w in tenants.values())):
        raise ValueError('weights')
    if len({j['id'] for j in jobs}) != len(jobs) or any((j['tenant'] not in tenants or type(j['cost']) is not int or j['cost'] < 1 for j in jobs)):
        raise ValueError('jobs')
    queues = {k: deque() for k in tenants}
    for j in jobs:
        queues[j['tenant']].append(j)
    deficits = dict.fromkeys(tenants, 0)
    clock = 0
    out = []
    rounds = 0
    served = dict.fromkeys(tenants, 0)
    while any(queues.values()):
        rounds += 1
        for tenant, weight in tenants.items():
            if not queues[tenant]:
                deficits[tenant] = 0
                continue
            deficits[tenant] += weight * quantum
            while queues[tenant] and queues[tenant][0]['cost'] <= deficits[tenant]:
                j = queues[tenant].popleft()
                cost = j['cost']
                deficits[tenant] -= cost
                out.append({'id': j['id'], 'tenant': tenant, 'start': clock, 'finish': clock + cost, 'round': rounds})
                clock += cost
                served[tenant] += cost
    normalized = [served[k] / w for k, w in tenants.items()]
    fairness = sum(normalized) ** 2 / (len(normalized) * sum((x * x for x in normalized))) if any(normalized) else 1
    return {'execution': out, 'service_units': served, 'makespan': clock, 'rounds': rounds, 'normalized_jain_index': fairness, 'scope': 'All jobs available at time zero; non-preemptive weighted deficit round robin.'}

def run(config):
    return schedule(config['tenants'], config['jobs'], config.get('quantum', 2))

import argparse, json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='tenant_fair_queue_scenario.json')
    parser.add_argument('--output', default='tenant_fair_queue_report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
