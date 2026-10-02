"""Veri Sözleşmesi ve Karantina.

Problem: Şema ve veri hatalarının downstream raporlara sessizce girmesini engellemek.
Method: Type/range/reference/unique/freshness, PSI
Invariant: Bilinmeyen alan REVIEW; geçersiz satır BLOCK; kabul edilen ve karantinadaki satırlar ayrılır.
Boundary: PSI kategorik histogram karşılaştırmasıdır; kendi başına istatistiksel anlamlılık testi değildir."""
import math

def psi(baseline, current):
    if len(baseline) != len(current) or not baseline or any((x < 0 for x in baseline + current)) or (not sum(baseline)) or (not sum(current)):
        raise ValueError('histogram')
    a = [max(1e-06, x / sum(baseline)) for x in baseline]
    b = [max(1e-06, x / sum(current)) for x in current]
    return sum(((y - x) * math.log(y / x) for x, y in zip(a, b)))

def gate(rows, contract, now):
    fields = contract['fields']
    unique = contract.get('unique')
    seen = set()
    accepted = []
    quarantine = []
    schema_review = False
    for index, row in enumerate(rows):
        errors = []
        if set(row) - set(fields):
            schema_review = True
            errors.append('UNKNOWN_FIELD')
        for name, rule in fields.items():
            v = row.get(name)
            if v is None:
                if not rule.get('nullable', False):
                    errors.append(name + ':NULL')
                continue
            types = {'string': str, 'integer': int, 'number': (int, float)}
            if rule['type'] not in types:
                raise ValueError('unsupported contract type')
            if isinstance(v, bool) or not isinstance(v, types[rule['type']]):
                errors.append(name + ':TYPE')
                continue
            if isinstance(v, (int, float)) and (not math.isfinite(v) or v < rule.get('min', float('-inf')) or v > rule.get('max', float('inf'))):
                errors.append(name + ':RANGE')
            if 'allowed' in rule and v not in rule['allowed']:
                errors.append(name + ':REFERENCE')
        if unique:
            key = row.get(unique)
            if key in seen:
                errors.append(unique + ':DUPLICATE')
            seen.add(key)
        fresh = contract.get('freshness')
        if fresh:
            at = row.get(fresh['field'])
            if isinstance(at, bool) or not isinstance(at, (float, int)) or (not math.isfinite(at)) or (at > now) or (now - at > fresh['max_age']):
                errors.append('FRESHNESS')
        if errors:
            quarantine.append({'index': index, 'errors': errors, 'row': row})
        else:
            accepted.append(row)
    return {'accepted': accepted, 'quarantine': quarantine, 'gate': 'REVIEW' if schema_review else 'BLOCK' if quarantine else 'PASS', 'row_count': len(rows)}

def run(config):
    result = gate(config['rows'], config['contract'], config['now'])
    if 'baseline_histogram' in config:
        result['psi'] = psi(config['baseline_histogram'], config['current_histogram'])
    return result

import argparse, json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='data_contract_quality_gate_scenario.json')
    parser.add_argument('--output', default='data_contract_quality_gate_report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
