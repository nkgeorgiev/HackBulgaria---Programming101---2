from mutagen.mp3 import MP3
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
            mp3s.append(MP3(filename))
        return mp3s

    def generate_playlist(self):
        playlist = Playlist("New Playlist")
        for mp3 in self.mp3s:
            title = mp3.tags["TIT2"]
            artist = mp3.tags["TPE1"]
            album = mp3.tags["TALB"]
            bitrate = mp3.info.bitrate
            length = round(mp3.info.length)
            playlist.add_song(Song(title, artist, album, 0, length, bitrate))
        return playlist


def main():
    m = MusicCrawler("songs/")
    a = m.generate_playlist()
    print(a)

if __name__ == '__main__':
    main()

