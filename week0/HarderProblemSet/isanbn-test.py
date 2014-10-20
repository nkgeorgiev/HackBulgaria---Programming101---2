import unittest
from isanbn import is_an_bn


class isanbnTest(unittest.TestCase):
    def test_isanbn(self):
        self.assertTrue(is_an_bn(""))
        self.assertTrue(is_an_bn("aaaabbbb"))
        self.assertFalse(is_an_bn("aabba"))
        self.assertFalse(is_an_bn("Rado"))

if __name__ == '__main__':
    unittest.main()
