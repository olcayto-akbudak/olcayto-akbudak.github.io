import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import sql_plan_regression_lab as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'sql_plan_regression_lab_scenario.json').read_text(encoding='utf-8'))

    def test_equivalence(self):
        q = c.benchmark(10, 6, 1)['queries']
        self.assertEqual(q['correlated']['sha256'], q['preaggregate']['sha256'])

    def test_fanout_detected(self):
        self.assertFalse(c.benchmark(10, 6, 1)['queries']['fanout_bug']['correct'])

    def test_independent_expected(self):
        self.assertTrue(c.benchmark(3, 4, 1)['queries']['correlated']['correct'])

    def test_index_plan(self):
        self.assertTrue(any(('orders_customer_status' in str(row) for row in c.benchmark(10, 6, 1)['queries']['correlated']['plan'])))

    def test_noindex_correct(self):
        self.assertTrue(c.benchmark(10, 6, 1, False)['queries']['preaggregate']['correct'])

    def test_bad_dimension(self):
        with self.assertRaises(ValueError):
            c.benchmark(0)

    def test_digest_change(self):
        self.assertNotEqual(c.digest([(1, 2)]), c.digest([(1, 3)]))

    def test_plan_available(self):
        self.assertTrue(all((q['plan'] for q in c.benchmark(10, 6, 1)['queries'].values())))
if __name__ == '__main__':
    unittest.main()
