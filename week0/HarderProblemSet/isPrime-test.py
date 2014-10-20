import unittest
from isPrime import is_prime

class isPrimeTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(128))

if __name__ == '__main__':
    unittest.main()
