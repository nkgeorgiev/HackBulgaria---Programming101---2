import unittest
from simplifyFraction import simplify_fraction, gcd


class SimplifyFractionTest(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(1, gcd(5, 2))
        self.assertEqual(4, gcd(16, 20))

    def test_simplify_fraction(self):
        self.assertTupleEqual((3, 22), simplify_fraction((63, 462)))
        self.assertTupleEqual((2, 5), simplify_fraction((4, 10)))


if __name__ == '__main__':
    unittest.main()
