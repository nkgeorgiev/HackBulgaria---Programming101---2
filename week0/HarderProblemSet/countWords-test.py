import unittest
from countWords import count_words


class countWordstest(unittest.TestCase):
    def test_count_words(self):
        d = {"apple": 2, "banana": 1, "pie": 1}
        self.assertDictEqual(d,
                             count_words(["apple", "banana", "apple", "pie"]))

if __name__ == '__main__':
    unittest.main()
