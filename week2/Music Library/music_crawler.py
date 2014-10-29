from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from playlist import Playlist, load
from song import Song
import os
import glob
import multiprocessing
import sys


class MusicCrawler:
    def __init__(self, pathname):
        self.pathname = pathname
        self.mp3s = self.load(pathname)

    def load(self, pathname):
        os.chdir(pathname)
        mp3s = []
        for filename in glob.glob("*.mp3"):
            path = (pathname+"/"+filename).replace(" ", "\ ")
            mp3s.append((MP3(filename, ID3=EasyID3), path))
        return mp3s

    def generate_playlist(self):
        playlist = Playlist("New Playlist")
        for mp3 in self.mp3s:
            try:
                title = mp3[0].tags["title"][0]
            except:
                title = "Unknown Title"
            try:
                artist = mp3[0].tags["artist"][0]
            except:
                artist = "Unknown Artist"
            try:
                album = mp3[0].tags["album"][0]
            except:
                album = "Unknown Album"
            bitrate = mp3[0].info.bitrate
            length = round(mp3[0].info.length)
            playlist.add_song(Song(title, artist, album, 0, length, bitrate, mp3[1]))
        return playlist


