import unittest
from goldbach import goldbach


class goldbachTest(unittest.TestCase):
    def test_goldbach(self):
        ans1 = [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]
        ans2 = [(3, 7), (5, 5)]
        self.assertListEqual(ans1, goldbach(100))
        self.assertListEqual(ans2, goldbach(10))

if __name__ == '__main__':
    unittest.main()
