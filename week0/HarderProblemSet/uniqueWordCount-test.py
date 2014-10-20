import unittest
from uniqueWordCount import unique_words_count


class uniqueWordCountTest(unittest.TestCase):
    def test_unique_word_count(self):
        self.assertEqual(3, unique_words_count(["apple", "banana", "apple", "pie"]))
        self.assertEqual(2, unique_words_count(["python", "python", "python", "ruby"]))
        self.assertEqual(1, unique_words_count(["HELLO!"] * 10))

if __name__ == '__main__':
    unittest.main()
