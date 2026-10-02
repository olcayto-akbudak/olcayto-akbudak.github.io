"""SQL Doğruluk ve Plan Regresyonu.

Problem: Daha hızlı görünen SQL değişikliğinin tutarları katlamasını sonuç doğruluğuyla yakalamak.
Method: Preaggregation, join fanout, digest, query plan
Invariant: Para tamsayı; iki ticket join fanout hatasını bilerek gösterir; sürelerden önce doğruluk değerlendirilir.
Boundary: SQLite yerel ölçümüdür; PostgreSQL planlarına veya gerçek üretim yüküne genellenmez."""
import sqlite3, time, statistics, hashlib, json
QUERIES = {'correlated': 'SELECT c.id, (SELECT COALESCE(SUM(amount),0) FROM orders o WHERE o.customer_id=c.id AND o.status="paid") total FROM customers c ORDER BY c.id', 'preaggregate': 'SELECT c.id,COALESCE(o.total,0) FROM customers c LEFT JOIN (SELECT customer_id,SUM(amount) total FROM orders WHERE status="paid" GROUP BY customer_id) o ON c.id=o.customer_id ORDER BY c.id', 'fanout_bug': 'SELECT c.id,COALESCE(SUM(o.amount),0) FROM customers c LEFT JOIN orders o ON c.id=o.customer_id AND o.status="paid" LEFT JOIN tickets t ON t.customer_id=c.id GROUP BY c.id ORDER BY c.id'}

def digest(rows):
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()

def benchmark(customers=200, orders_per_customer=10, repeats=5, indexed=True):
    if customers < 1 or orders_per_customer < 1 or repeats < 1:
        raise ValueError('benchmark dimensions')
    db = sqlite3.connect(':memory:')
    try:
        db.executescript('CREATE TABLE customers(id INTEGER PRIMARY KEY);CREATE TABLE orders(id INTEGER PRIMARY KEY,customer_id INTEGER,amount INTEGER,status TEXT);CREATE TABLE tickets(id INTEGER PRIMARY KEY,customer_id INTEGER);')
        db.executemany('INSERT INTO customers VALUES (?)', [(i,) for i in range(customers)])
        db.executemany('INSERT INTO orders VALUES (?,?,?,?)', [(i * orders_per_customer + j, i, 100 + j, 'paid' if j % 3 else 'pending') for i in range(customers) for j in range(orders_per_customer)])
        db.executemany('INSERT INTO tickets VALUES (?,?)', [(i * 2 + j, i) for i in range(customers) for j in range(2)])
        if indexed:
            db.execute('CREATE INDEX orders_customer_status ON orders(customer_id,status)')
        expected = [(i, sum((100 + j for j in range(orders_per_customer) if j % 3))) for i in range(customers)]
        out = {}
        for name, sql in QUERIES.items():
            durations = []
            rows = db.execute(sql).fetchall()
            for _ in range(repeats):
                start = time.perf_counter()
                db.execute(sql).fetchall()
                durations.append((time.perf_counter() - start) * 1000)
            out[name] = {'correct': rows == expected, 'row_count': len(rows), 'sha256': digest(rows), 'median_ms': statistics.median(durations), 'plan': [list(r) for r in db.execute('EXPLAIN QUERY PLAN ' + sql)]}
        return {'queries': out, 'expected_sha256': digest(expected), 'indexed': indexed, 'sqlite_version': sqlite3.sqlite_version, 'scope': 'Local timing varies; correctness gates precede performance comparison.'}
    finally:
        db.close()

def run(config):
    return benchmark(**config)

import argparse, json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='sql_plan_regression_lab_scenario.json')
    parser.add_argument('--output', default='sql_plan_regression_lab_report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
