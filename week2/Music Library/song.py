class Song:
    MAX_RATING = 5
    MIN_RATING = 0

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, rating):
        if rating < self.MIN_RATING or rating > self.MAX_RATING:
            error_message = "Rating must be from {} to {}"
            raise ValueError(error_message.format(Song.MIN_RATING, Song.MAX_RATING))

        else:
            self.rating = rating
