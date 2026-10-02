import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import tenant_fair_queue as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'tenant_fair_queue_scenario.json').read_text(encoding='utf-8'))

    def test_exact_once(self):
        self.assertEqual(len({r['id'] for r in c.run(self.config)['execution']}), len(self.config['jobs']))

    def test_cost_conservation(self):
        self.assertEqual(c.run(self.config)['makespan'], sum((j['cost'] for j in self.config['jobs'])))

    def test_big_job(self):
        self.assertEqual(c.schedule({'A': 1}, [{'id': 'x', 'tenant': 'A', 'cost': 100}])['makespan'], 100)

    def test_weight_order(self):
        r = c.schedule({'A': 3, 'B': 1}, [{'id': str(i), 'tenant': 'A' if i < 10 else 'B', 'cost': 1} for i in range(20)], 1)
        self.assertEqual([x['tenant'] for x in r['execution'][:4]], ['A', 'A', 'A', 'B'])

    def test_unknown(self):
        with self.assertRaises(ValueError):
            c.schedule({'A': 1}, [{'id': 'x', 'tenant': 'B', 'cost': 1}])

    def test_bad_weight(self):
        with self.assertRaises(ValueError):
            c.schedule({'A': 0}, [])

    def test_duplicate_jobs(self):
        with self.assertRaises(ValueError):
            c.schedule(self.config['tenants'], self.config['jobs'] * 2)

    def test_nonfinite_weight(self):
        with self.assertRaises(ValueError):
            c.schedule({'A': float('nan')}, [])
if __name__ == '__main__':
    unittest.main()
