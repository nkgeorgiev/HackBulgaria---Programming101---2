from playlist import Playlist
from song import Song
import unittest


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist("test_playlist")
        self.test_song = Song("Highway to Hell", "AC/DC", "Highway to Hell", 5, 208, 128, "sda")
        self.test_song2 = Song("Back in Black", "ACDC", "Back in Black", 4, 200, 256, "sdb")

        self.playlist.add_song(self.test_song)
        self.playlist.add_song(self.test_song2)
        self.playlist.save("sdadada.json")
        #self.playlist.load("sdadada.json")
    def test_init(self):
        self.assertEqual("test_playlist", self.playlist.name)

    def test_playlist_add_song(self):
        self.assertListEqual(self.playlist.songs, [self.test_song, self.test_song2])
        self.assertEqual(self.playlist.totalLength, 408)

    def test_playlist_remove_song(self):
        self.playlist.remove_song(self.test_song.title)
        self.assertListEqual(self.playlist.songs, [self.test_song2])
        self.assertEqual(self.playlist.totalLength, 200)

    def test_playlist_total_length(self):
        self.playlist.remove_song(self.test_song.title)
        self.assertEqual(self.playlist.total_length(), 200)

    def test_playlist_remove_disrated(self):
        self.playlist.remove_disrated(5)
        self.assertListEqual(self.playlist.songs, [self.test_song])
        self.assertEqual(self.playlist.total_length(), 208)

    def test_playlist_remove_bad_quality(self):
        self.playlist.remove_bad_quality()
        self.assertListEqual(self.playlist.songs, [self.test_song2])
        self.assertEqual(self.playlist.total_length(), 200)

    def test_playlist_list_artists(self):
        self.playlist.add_song(self.test_song2)
        artists = self.playlist.list_artists()
        self.assertListEqual(["AC/DC", "ACDC"], artists)


if __name__ == '__main__':
    unittest.main()
