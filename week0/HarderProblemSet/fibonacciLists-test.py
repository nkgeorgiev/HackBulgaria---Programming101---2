import unittest
from fibonacciLists import nth_fib_lists


class fibonacciListsTest(unittest.TestCase):
    def test_fibonacciLists(self):
        l = nth_fib_lists([], [1, 2, 3], 4)
        self.assertListEqual([1, 2, 3, 1, 2, 3],l)
        self.assertListEqual([], nth_fib_lists([], [], 100))


if __name__ == '__main__':
    unittest.main()
