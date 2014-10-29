from song import Song
import unittest


class TestSong(unittest.TestCase):
    def setUp(self):
        self.test_song = Song("Highway to Hell", "AC/DC", "Highway to Hell", 5, 208, 256, "asa")

    def test_song_init(self):
        self.assertEqual("Highway to Hell", self.test_song.title)
        self.assertEqual("AC/DC", self.test_song.artist)
        self.assertEqual("Highway to Hell", self.test_song.album)
        self.assertEqual(5, self.test_song.rating)
        self.assertEqual(208, self.test_song.length)
        self.assertEqual(256, self.test_song.bitrate)
        self.assertEqual("asa", self.test_song.path)

    def test_song_rate_raise_error(self):
        with self.assertRaises(ValueError):
            self.test_song.rate(10)

    def test_song_rate(self):
        self.test_song.rate(3)
        self.assertEqual(3, self.test_song.rating)

if __name__ == '__main__':
    unittest.main()
