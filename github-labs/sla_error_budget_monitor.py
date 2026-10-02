"""SLA ve Çok Pencereli Burn Rate.

Problem: Kısa süreli küçük örneklem sıçraması ile kalıcı hizmet bozulmasını ayırmak.
Method: SLO, düşük hacim koruması, p95, hata bütçesi
Invariant: Pencereler now-window < at <= now; alarm tüm pencerelerde eşik aşılınca açılır.
Boundary: Uzun dönem hata bütçesi ayrıca tutulmalıdır; remaining değeri son pencerenin bütçesidir."""
import math

def monitor(events, now, slo=0.99, windows=(300, 3600), minimum=20, burn_threshold=6):
    if not 0 < slo < 1 or minimum < 1 or any((w <= 0 for w in windows)):
        raise ValueError('SLO contract')
    if any((not math.isfinite(e['at']) or not math.isfinite(e['latency_ms']) or e['latency_ms'] < 0 for e in events)):
        raise ValueError('event contract')
    results = []
    for w in windows:
        selected = [e for e in events if now - w < e['at'] <= now]
        errors = sum((not e['ok'] for e in selected))
        burn = errors / max(1, len(selected)) / (1 - slo)
        latencies = sorted((e['latency_ms'] for e in selected))
        results.append({'window_seconds': w, 'requests': len(selected), 'errors': errors, 'burn_rate': burn, 'p95_ms': latencies[min(len(latencies) - 1, math.ceil(0.95 * len(latencies)) - 1)] if latencies else None, 'eligible': len(selected) >= minimum})
    alert = all((r['eligible'] and r['burn_rate'] >= burn_threshold for r in results))
    return {'page': alert, 'windows': results, 'remaining_error_budget': max(0, (1 - slo) * results[-1]['requests'] - results[-1]['errors'])}

def run(config):
    return monitor(config['events'], config['now'], config.get('slo', 0.99), tuple(config.get('windows', [300, 3600])), config.get('minimum', 20))

import argparse, json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='sla_error_budget_monitor_scenario.json')
    parser.add_argument('--output', default='sla_error_budget_monitor_report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
