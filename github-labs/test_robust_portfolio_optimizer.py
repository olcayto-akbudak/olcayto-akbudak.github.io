import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import robust_portfolio_optimizer as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'robust_portfolio_optimizer_scenario.json').read_text(encoding='utf-8'))

    def test_budget(self):
        r = c.run(self.config)
        for k, v in r['costs'].items():
            self.assertLessEqual(v, self.config['budgets'][k])

    def test_dependencies(self):
        r = c.run(self.config)
        self.assertTrue('B' not in r['selected'] or 'A' in r['selected'])

    def test_conflict(self):
        self.assertFalse({'B', 'C'} <= set(c.run(self.config)['selected']))

    def test_exact_bruteforce(self):
        import itertools
        items = self.config['items']
        best = 0
        for bits in itertools.product([0, 1], repeat=len(items)):
            chosen = [x for x, b in zip(items, bits) if b]
            ids = {x['id'] for x in chosen}
            if any((not set(x.get('requires', [])) <= ids or set(x.get('conflicts', [])) & ids for x in chosen)):
                continue
            if any((sum((x['costs'].get(k, 0) for x in chosen)) > v for k, v in self.config['budgets'].items())):
                continue
            best = max(best, min((sum((x['values'][s] for x in chosen)) for s in range(2))))
        self.assertEqual(c.run(self.config)['score'], best)

    def test_negative(self):
        with self.assertRaises(ValueError):
            c.optimize([], {'money': -1})

    def test_empty(self):
        self.assertEqual(c.optimize([], {'money': 1})['score'], 0)

    def test_nonfinite_value(self):
        with self.assertRaises(ValueError):
            c.optimize([{'id': 'X', 'values': [float('nan')], 'costs': {}}], {'money': 1})

    def test_unknown_dependency(self):
        with self.assertRaises(ValueError):
            c.optimize([{'id': 'X', 'values': [1], 'costs': {}, 'requires': ['Y']}], {'money': 1})
if __name__ == '__main__':
    unittest.main()
