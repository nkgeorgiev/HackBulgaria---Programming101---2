from song import Song
import json


class Playlist:
    BAD_QUALITY = 128

    def __init__(self, name):
        self.name = name
        self.songs = []
        self.totalLength = 0

    def add_song(self, song):
        self.songs.append(song)
        self.totalLength += song.length

    def remove_song(self, title):
        l = []
        for song in self.songs:
            if song.title is not title:
                l.append(song)
            else:
                self.totalLength -= song.length
        self.songs = l

    def total_length(self):
        return self.totalLength

    def remove_disrated(self, rating):
        l = []
        for song in self.songs:
            if song.rating >= rating:
                l.append(song)
            else:
                self.totalLength -= song.length
        self.songs = l

    def remove_bad_quality(self):
        l = []
        for song in self.songs:
            if song.bitrate > self.BAD_QUALITY:
                l.append(song)
            else:
                self.totalLength -= song.length
        self.songs = l

    def list_artists(self):
        artists = set()
        for song in self.songs:
            artists.add(song.artist)
        return sorted(artists)

    def __str__(self):
        string = "Name: %s\n" % self.name
        for song in self.songs:
            song_string = "{} {} - {}:{:02}\n"
            mins = song.length // 60
            secs = song.length % 60
            string += song_string.format(song.artist, song.title, mins, secs)
        return string

    def save(self, filename):
        d = {}
        lsongs = []
        d["name"] = self.name

        for song in self.songs:
            lsongs.append(song.__dict__)

        d["songs"] = lsongs
        with open(filename, "w") as file:
            file.write(json.dumps(d))


def load(filename):
    p = Playlist("")
    p.songs = []
    p.totalLength = 0
    try:
        with open(filename) as file:
            string = file.read()

        d = json.loads(string)

        for key in d.keys():
            if key == "name":
                p.name = d[key]
            elif key == "songs":
                lsongs = d[key]

        for s in lsongs:
            p.songs.append(Song(s["title"], s["artist"], s["album"],
                                s["rating"], s["length"], s["bitrate"], s["path"]))
        return p
    except:
        print("File does not exist!")
