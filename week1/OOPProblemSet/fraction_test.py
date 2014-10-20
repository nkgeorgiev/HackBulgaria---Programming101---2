import unittest
from Fraction import Fraction


class FractionTest(unittest.TestCase):
    def test_fraction_init_(self):
        fraction = Fraction(3, 4)
        self.assertEqual(3, fraction.num)
        self.assertEqual(4, fraction.denum)

    def test_fraction_eq(self):
        a = Fraction(3, 4)
        b = Fraction(6, 8)
        c = Fraction(4, 1)
        self.assertTrue(a == b)
        self.assertFalse(a == c)

    def test_fraction_add(self):
        a = Fraction(3, 4)
        b = Fraction(6, 8)
        d = Fraction(12, 8)
        self.assertEqual(d, a + b)

    def test_fraction_sub(self):
        a = Fraction(3, 4)
        b = Fraction(6, 8)
        d = Fraction (0, 0)
        self.assertEqual(d, a - b)

    def test_fraction_lt(self):
        a = Fraction(3, 4)
        b = Fraction(4, 5)
        self.assertTrue(a < b)
        self.assertFalse(a == b)

    def test_fraction_gt(self):
        a = Fraction(3, 4)
        b = Fraction(4, 5)
        self.assertTrue(a > b)
        self.assertFalse(a == b)

if __name__ == '__main__':
    unittest.main()
