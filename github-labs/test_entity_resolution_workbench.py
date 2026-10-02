import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import entity_resolution_workbench as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'entity_resolution_workbench_scenario.json').read_text(encoding='utf-8'))

    def test_tax_conflict(self):
        self.assertTrue(any((not e['accepted'] for e in c.run(self.config)['evidence'])))

    def test_cluster_invariant(self):
        byid = {r['id']: r for r in self.config['records']}
        for group in c.run(self.config)['clusters']:
            self.assertLessEqual(len({byid[k]['tax_id'] for k in group if byid[k].get('tax_id')}), 1)

    def test_normalize(self):
        self.assertEqual(c.normalize('İSTANBUL Şirket'), 'istanbul sirket')

    def test_country_block(self):
        r = [{'id': '1', 'name': 'Acme', 'country': 'TR'}, {'id': '2', 'name': 'Acme', 'country': 'DE'}]
        self.assertEqual(c.resolve(r)['candidate_count'], 0)

    def test_duplicate(self):
        with self.assertRaises(ValueError):
            c.resolve(self.config['records'] * 2)

    def test_threshold(self):
        with self.assertRaises(ValueError):
            c.resolve([], 0)

    def test_email_punctuation_preserved(self):
        records = [{'id': '1', 'name': 'Aaa', 'country': 'TR', 'email': 'a.b@x.com'}, {'id': '2', 'name': 'Azz', 'country': 'TR', 'email': 'ab@x.com'}]
        self.assertEqual(c.resolve(records)['candidate_count'], 0)

    def test_compatible_merge(self):
        self.assertEqual(len(c.resolve([{'id': '1', 'name': 'Acme', 'country': 'TR'}, {'id': '2', 'name': 'Acme', 'country': 'TR'}])['clusters']), 1)
if __name__ == '__main__':
    unittest.main()
