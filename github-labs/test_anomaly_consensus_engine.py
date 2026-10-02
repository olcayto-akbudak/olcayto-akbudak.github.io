import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import anomaly_consensus_engine as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'anomaly_consensus_engine_scenario.json').read_text(encoding='utf-8'))

    def test_flat(self):
        self.assertEqual(c.detect([100] * 80)['alerts'], [])

    def test_shift(self):
        self.assertGreater(len(c.detect([100] * 40 + [150] * 40)['alerts']), 0)

    def test_short(self):
        with self.assertRaises(ValueError):
            c.detect([1] * 10)

    def test_nonfinite(self):
        with self.assertRaises(ValueError):
            c.detect([float('nan')] * 80)

    def test_alpha(self):
        with self.assertRaises(ValueError):
            c.detect([1] * 80, alpha=0)

    def test_baseline_frozen(self):
        self.assertEqual(c.detect([100] * 40 + [500] * 40)['seasonal'], [100] * 7)

    def test_seasonality_no_alarm(self):
        self.assertEqual(c.detect([100 + i % 7 * 10 for i in range(100)])['alerts'], [])

    def test_period(self):
        with self.assertRaises(ValueError):
            c.detect([1] * 80, period=0)
if __name__ == '__main__':
    unittest.main()
