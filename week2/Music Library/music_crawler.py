from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from playlist import Playlist
from song import Song
import os
import glob


class MusicCrawler:
    def __init__(self, pathname):
        self.mp3s = self.load(pathname)

    def load(self, pathname):
        os.chdir(pathname)
        mp3s = []
        for filename in glob.glob("*.mp3"):
            mp3s.append(MP3(filename, ID3=EasyID3))
        return mp3s

    def generate_playlist(self):
        playlist = Playlist("New Playlist")
        for mp3 in self.mp3s:
            try:
                title = mp3.tags["title"][0]
            except:
                title = "Unknown"
            try:
                artist = mp3.tags["artist"][0]
            except:
                artist = "Unknown"
            try:
                album = mp3.tags["album"][0]
            except:
                album = "Unknown"
            bitrate = mp3.info.bitrate
            length = round(mp3.info.length)
            playlist.add_song(Song(title, artist, album, 0, length, bitrate))
        return playlist


def main():
    m = MusicCrawler("/mnt/76F83073F8303429/Music/Avenged Sevenfold")
    a = m.generate_playlist()
    print(a)

if __name__ == '__main__':
    main()

