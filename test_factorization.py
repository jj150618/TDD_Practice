import unittest
from factorization import Factorization


class FactorizationTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.factorization = Factorization()

    def test_get_factorization(self):
        self.assertEqual(self.factorization.get_factorization(1), [])
        self.assertEqual(self.factorization.get_factorization(2), [2])
        self.assertEqual(self.factorization.get_factorization(3), [3])
        self.assertEqual(self.factorization.get_factorization(4), [2, 2])
        self.assertEqual(self.factorization.get_factorization(5), [5])
        self.assertEqual(self.factorization.get_factorization(6), [2, 3])
        self.assertEqual(self.factorization.get_factorization(7), [7])
        self.assertEqual(self.factorization.get_factorization(8), [2, 2, 2])
        self.assertEqual(self.factorization.get_factorization(9), [3, 3])
        self.assertEqual(self.factorization.get_factorization(10), [2, 5])
        self.assertEqual(self.factorization.get_factorization(2*3*3*5*7), [2, 3, 3, 5, 7])


if __name__ == '__main__':
    unittest.main()
