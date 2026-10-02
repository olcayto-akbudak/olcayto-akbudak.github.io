import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import data_contract_quality_gate as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'data_contract_quality_gate_scenario.json').read_text(encoding='utf-8'))

    def test_quarantine(self):
        self.assertEqual(len(c.run(self.config)['quarantine']), 2)

    def test_unknown_review(self):
        self.assertEqual(c.run(self.config)['gate'], 'REVIEW')

    def test_psi_identity(self):
        self.assertEqual(c.psi([1, 2], [1, 2]), 0)

    def test_psi_shift(self):
        self.assertGreater(c.psi([50, 30, 20], [20, 30, 50]), 0.1)

    def test_future(self):
        row = {'id': 'X', 'amount': 1, 'at': 101}
        self.assertEqual(c.gate([row], self.config['contract'], 100)['gate'], 'BLOCK')

    def test_bool_not_int(self):
        self.assertEqual(c.gate([{'id': 'X', 'amount': True, 'at': 99}], self.config['contract'], 100)['gate'], 'BLOCK')

    def test_partition_conservation(self):
        r = c.run(self.config)
        self.assertEqual(len(r['accepted']) + len(r['quarantine']), len(self.config['rows']))

    def test_empty_histogram(self):
        with self.assertRaises(ValueError):
            c.psi([0, 0], [1, 1])
if __name__ == '__main__':
    unittest.main()
