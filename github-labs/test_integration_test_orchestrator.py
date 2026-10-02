import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import integration_test_orchestrator as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'integration_test_orchestrator_scenario.json').read_text(encoding='utf-8'))

    def test_retry(self):
        self.assertEqual(c.run(self.config)['results']['create']['attempts'], 2)

    def test_skip(self):
        self.assertEqual(c.run(self.config)['results']['after-slow']['status'], 'skipped')

    def test_timeout(self):
        self.assertEqual(c.run(self.config)['results']['slow']['status'], 'timeout')

    def test_unsafe(self):
        with self.assertRaises(ValueError):
            c.orchestrate([{'id': 'a', 'duration': 1, 'retries': 1}])

    def test_cycle(self):
        with self.assertRaises(ValueError):
            c.orchestrate([{'id': 'a', 'duration': 1, 'depends': ['a']}])

    def test_workers(self):
        with self.assertRaises(ValueError):
            c.orchestrate([], 0)

    def test_nonfinite_duration(self):
        with self.assertRaises(ValueError):
            c.orchestrate([{'id': 'x', 'duration': float('nan')}])

    def test_serial_makespan(self):
        self.assertEqual(c.orchestrate([{'id': 'a', 'duration': 2}, {'id': 'b', 'duration': 3}], workers=1)['makespan'], 5)
if __name__ == '__main__':
    unittest.main()
