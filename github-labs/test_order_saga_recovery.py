import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import order_saga_recovery as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'order_saga_recovery_scenario.json').read_text(encoding='utf-8'))
        with c.sqlite_session(self.path) as connection:
            connection.execute('SELECT 1')
        with self.assertRaises(sqlite3.ProgrammingError):
            connection.execute('SELECT 1')

    def test_complete(self):
        self.assertEqual(c.Saga(self.path).execute('A'), 'COMPLETED')

    def test_resume(self):
        s = c.Saga(self.path)
        with self.assertRaises(RuntimeError):
            s.execute('A', crash_after='payment')
        self.assertEqual(c.Saga(self.path).execute('A'), 'COMPLETED')
        self.assertEqual(len(s.effects('A')), 3)

    def test_compensate(self):
        s = c.Saga(self.path)
        self.assertEqual(s.execute('A', fail_step='shipping'), 'COMPENSATED')
        self.assertFalse(any(s.effects('A').values()))

    def test_idempotency(self):
        s = c.Saga(self.path)
        s.execute('A')
        s.execute('A')
        self.assertEqual(len(s.effects('A')), 3)

    def test_irreversible(self):
        s = c.Saga(self.path)
        s.execute('A')
        s.compensate('A')
        self.assertEqual(s.state('A'), 'MANUAL')

    def test_empty_id(self):
        with self.assertRaises(ValueError):
            c.Saga(self.path).execute('')

    def test_compensation_idempotent(self):
        s = c.Saga(self.path)
        s.execute('A', fail_step='payment')
        s.compensate('A')
        self.assertEqual(s.state('A'), 'COMPENSATED')

    def test_shipping_crash_recovery(self):
        s = c.Saga(self.path)
        with self.assertRaises(RuntimeError):
            s.execute('A', crash_after='shipping')
        self.assertEqual(c.Saga(self.path).execute('A'), 'COMPLETED')
if __name__ == '__main__':
    unittest.main()
