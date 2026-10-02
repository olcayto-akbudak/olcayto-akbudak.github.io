import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import requirements_traceability_graph as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'requirements_traceability_graph_scenario.json').read_text(encoding='utf-8'))

    def test_stale_gate(self):
        self.assertEqual(c.run(self.config)['gate'], 'BLOCK')

    def test_weight(self):
        self.assertAlmostEqual(c.run(self.config)['weighted_coverage'], 5 / 7)

    def test_impact(self):
        self.assertEqual(c.run(self.config)['impact'], ['B1', 'T1'])

    def test_cycle(self):
        cfg = copy.deepcopy(self.config)
        cfg['edges'].append(['T1', 'R1'])
        with self.assertRaises(ValueError):
            c.run(cfg)

    def test_dangling(self):
        with self.assertRaises(ValueError):
            c.analyze(self.config['nodes'], [['R1', 'missing']])

    def test_duplicate(self):
        with self.assertRaises(ValueError):
            c.analyze(self.config['nodes'] * 2, [])

    def test_current_evidence_pass(self):
        cfg = copy.deepcopy(self.config)
        cfg['nodes'][-1]['tested_revision'] = 1
        self.assertEqual(c.run(cfg)['gate'], 'PASS')

    def test_unknown_change(self):
        with self.assertRaises(ValueError):
            c.analyze(self.config['nodes'], self.config['edges'], ['missing'])
if __name__ == '__main__':
    unittest.main()
