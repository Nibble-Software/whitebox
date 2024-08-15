import unittest


class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(operate('+', 2, 3), 5)
        self.assertEqual(operate('-', 1, 1), 0)
        self.assertEqual(operate('*', 0, 0), 0)
        self.assertEqual(operate('/', 4, 2), 2)

    def test_division_by_cero(self):
        self.assertEqual(operate('/', 4, 0), 0)
        self.assertEqual(operate('/', 0, 4), 0)
        self.assertEqual(operate('/', 0, 0), 0)
