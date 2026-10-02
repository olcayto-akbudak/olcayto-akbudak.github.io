"""Mevsimsel Anomali Konsensüsü.

Problem: Haftalık dalgalanmayı gerçek işlem hatası gibi işaretlemeden kalıcı sapmaları saptamak.
Method: Median/MAD, EWMA, ardışık alarm oyları
Invariant: Baseline warmup boyunca oluşur; izleme sırasında otomatik güncellenmez.
Boundary: Eşikler demo içindir; saha verisinde yanlış alarm bütçesiyle doğrulanmalıdır."""
import statistics, math

def detect(values, period=7, warmup=35, z_limit=4, alpha=0.25):
    if period < 1 or warmup < period * 3 or (not 0 < alpha <= 1) or any((not math.isfinite(x) for x in values)):
        raise ValueError('series configuration')
    if len(values) <= warmup:
        raise ValueError('insufficient observations')
    baseline = values[:warmup]
    seasonal = [statistics.median(baseline[i::period]) for i in range(period)]
    residual = [v - seasonal[i % period] for i, v in enumerate(baseline)]
    center = statistics.median(residual)
    scale = max(1, 1.4826 * statistics.median((abs(x - center) for x in residual)))
    ewma = 0
    scores = []
    alerts = []
    for i, v in enumerate(values[warmup:], warmup):
        z = (v - seasonal[i % period] - center) / scale
        ewma = alpha * z + (1 - alpha) * ewma
        recent = [s['z'] for s in scores[-2:]] + [z]
        votes = int(abs(z) >= z_limit) + int(abs(ewma) >= z_limit * 0.65) + int(len(recent) == 3 and all((abs(x) >= z_limit * 0.65 for x in recent)))
        record = {'index': i, 'z': z, 'ewma': ewma, 'votes': votes}
        scores.append(record)
        if votes >= 2:
            alerts.append(record)
    return {'baseline_scale': scale, 'seasonal': seasonal, 'alerts': alerts, 'scores': scores}

def run(config):
    result = detect(config['values'], config.get('period', 7), config.get('warmup', 35))
    labels = set(config.get('anomaly_indices', []))
    detected = {r['index'] for r in result['alerts']}
    result['evaluation'] = {'true_positive': len(labels & detected), 'false_positive': len(detected - labels), 'missed': len(labels - detected)}
    return result

import argparse, json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='anomaly_consensus_engine_scenario.json')
    parser.add_argument('--output', default='anomaly_consensus_engine_report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
