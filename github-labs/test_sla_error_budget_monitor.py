import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import sla_error_budget_monitor as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'sla_error_budget_monitor_scenario.json').read_text(encoding='utf-8'))

    def test_volume_guard(self):
        self.assertFalse(c.monitor([{'at': 10, 'ok': False, 'latency_ms': 2}], 10)['page'])

    def test_sustained(self):
        self.assertTrue(c.monitor([{'at': 10, 'ok': False, 'latency_ms': 2}] * 30, 10)['page'])

    def test_future_excluded(self):
        self.assertEqual(c.monitor([{'at': 11, 'ok': False, 'latency_ms': 2}], 10)['windows'][0]['requests'], 0)

    def test_boundary(self):
        self.assertEqual(c.monitor([{'at': 0, 'ok': True, 'latency_ms': 2}], 300)['windows'][0]['requests'], 0)

    def test_good(self):
        self.assertFalse(c.monitor([{'at': 10, 'ok': True, 'latency_ms': 2}] * 30, 10)['page'])

    def test_slo(self):
        with self.assertRaises(ValueError):
            c.monitor([], 10, slo=1)

    def test_nonfinite_latency(self):
        with self.assertRaises(ValueError):
            c.monitor([{'at': 1, 'ok': True, 'latency_ms': float('nan')}], 10)

    def test_p95(self):
        self.assertEqual(c.monitor([{'at': 1, 'ok': True, 'latency_ms': i} for i in range(1, 101)], 10)['windows'][0]['p95_ms'], 95)
if __name__ == '__main__':
    unittest.main()
