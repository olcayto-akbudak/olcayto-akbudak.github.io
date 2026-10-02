"""Kısıtlı Müşteri Eşleştirme.

Problem: Benzer müşteri adlarını birleştirirken çelişkili vergi kimliklerinin dolaylı birleşmesini önlemek.
Method: Unicode normalizasyonu, blocking, cluster constraint
Invariant: Küme seviyesinde en fazla bir dolu vergi kimliği; boş kimlik eşleşmeyi tek başına engellemez.
Boundary: Tam adres ve dil çözümlemesi yoktur; eşikler etiketli gerçek çiftlerle doğrulanmalıdır."""
import unicodedata, re
from difflib import SequenceMatcher

def normalize(value):
    return re.sub('[^a-z0-9]+', ' ', unicodedata.normalize('NFKD', value.casefold().replace('ı', 'i')).encode('ascii', 'ignore').decode()).strip()

def resolve(records, threshold=0.82):
    if not 0 < threshold <= 1 or len({r['id'] for r in records}) != len(records):
        raise ValueError('ids/threshold')
    parent = {r['id']: r['id'] for r in records}
    members = {r['id']: {r['id']} for r in records}
    byid = {r['id']: r for r in records}

    def root(key):
        while parent[key] != key:
            key = parent[key]
        return key
    candidates = []
    for i, a in enumerate(records):
        for b in records[i + 1:]:
            if a.get('country') != b.get('country'):
                continue
            na, nb = (normalize(a['name']), normalize(b['name']))
            if not na or not nb or na[0] != nb[0]:
                continue
            score = SequenceMatcher(None, na, nb).ratio()
            if a.get('email') and a['email'].strip().casefold() == b.get('email', '').strip().casefold():
                score = max(score, 0.98)
            if score >= threshold:
                candidates.append((score, a['id'], b['id']))
    evidence = []
    for score, a, b in sorted(candidates, key=lambda x: (-x[0], x[1], x[2])):
        ra, rb = (root(a), root(b))
        if ra == rb:
            continue
        identities = {byid[k]['tax_id'] for k in members[ra] | members[rb] if byid[k].get('tax_id')}
        accepted = len(identities) <= 1
        evidence.append({'left': a, 'right': b, 'score': score, 'accepted': accepted, 'reason': 'compatible' if accepted else 'cluster_tax_id_conflict'})
        if accepted:
            parent[rb] = ra
            members[ra] |= members.pop(rb)
    return {'clusters': [sorted(v) for _, v in sorted(members.items())], 'evidence': evidence, 'candidate_count': len(candidates)}

def run(config):
    return resolve(config['records'], config.get('threshold', 0.82))

import argparse, json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='entity_resolution_workbench_scenario.json')
    parser.add_argument('--output', default='entity_resolution_workbench_report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
