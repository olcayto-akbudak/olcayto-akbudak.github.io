"""Sipariş Saga ve Telafi Laboratuvarı.

Problem: Stok/ödeme/kargo zincirinde çöken koordinatörü yeniden başlatmak ve güvenli telafi etmek.
Method: Kalıcı adımlar, çökme enjeksiyonu, compensation
Invariant: Katılımcılar order+step anahtarlı kalıcı yerel mock; kargo gerçekleşmişse manuel inceleme gerekir.
Boundary: Gerçek dağıtık transaction yoktur; remote katılımcı idempotency ve outbox gereklidir."""
import sqlite3, tempfile
from pathlib import Path
from contextlib import contextmanager

@contextmanager
def sqlite_session(path, **kwargs):
    """Commit or roll back, then always close the OS file handle."""
    connection = sqlite3.connect(path, **kwargs)
    try:
        with connection:
            yield connection
    finally:
        connection.close()

class Saga:

    def __init__(self, path):
        self.path = str(path)
        with self.connect() as db:
            db.executescript('CREATE TABLE IF NOT EXISTS orders(id TEXT PRIMARY KEY, state TEXT); CREATE TABLE IF NOT EXISTS effects(order_id TEXT, step TEXT, active INTEGER, PRIMARY KEY(order_id,step));')

    def connect(self):
        return sqlite_session(self.path)

    def state(self, key):
        with self.connect() as db:
            row = db.execute('SELECT state FROM orders WHERE id=?', (key,)).fetchone()
        return row[0] if row else 'NEW'

    def execute(self, key, fail_step=None, crash_after=None):
        if not key:
            raise ValueError('order id')
        state = self.state(key)
        if state in ('COMPLETED', 'COMPENSATED', 'MANUAL'):
            return state
        with self.connect() as db:
            db.execute('INSERT OR IGNORE INTO orders VALUES (?,?)', (key, 'NEW'))
        for step in ('inventory', 'payment', 'shipping'):
            with self.connect() as db:
                row = db.execute('SELECT active FROM effects WHERE order_id=? AND step=?', (key, step)).fetchone()
            if row and row[0]:
                continue
            if step == fail_step:
                self.compensate(key)
                return self.state(key)
            with self.connect() as db:
                db.execute('INSERT INTO effects VALUES (?,?,1) ON CONFLICT(order_id,step) DO UPDATE SET active=1', (key, step))
            if crash_after == step:
                raise RuntimeError('injected crash')
            with self.connect() as db:
                db.execute('UPDATE orders SET state=? WHERE id=?', (step.upper(), key))
        with self.connect() as db:
            db.execute('UPDATE orders SET state="COMPLETED" WHERE id=?', (key,))
        return 'COMPLETED'

    def compensate(self, key):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            shipped = db.execute('SELECT active FROM effects WHERE order_id=? AND step="shipping"', (key,)).fetchone()
            if shipped and shipped[0]:
                db.execute('UPDATE orders SET state="MANUAL" WHERE id=?', (key,))
                return
            db.execute('UPDATE effects SET active=0 WHERE order_id=?', (key,))
            db.execute('UPDATE orders SET state="COMPENSATED" WHERE id=?', (key,))

    def effects(self, key):
        with self.connect() as db:
            return dict(db.execute('SELECT step,active FROM effects WHERE order_id=?', (key,)).fetchall())

def run(config):
    with tempfile.TemporaryDirectory() as d:
        s = Saga(Path(d) / 'saga.db')
        out = []
        for order in config['orders']:
            try:
                s.execute(order['id'], fail_step=order.get('fail_step'), crash_after=order.get('crash_after'))
            except RuntimeError:
                pass
            state = s.execute(order['id'], fail_step=order.get('fail_step'))
            out.append({'id': order['id'], 'state': state, 'effects': s.effects(order['id'])})
        return {'orders': out, 'participants': 'durable local mocks, not distributed services'}
import argparse, json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='order_saga_recovery_scenario.json')
    parser.add_argument('--output', default='order_saga_recovery_report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
