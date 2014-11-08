class Song:
    max_rating = 5
    min_rating = 1

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, number):
        if number < Song.min_rating or number > Song.max_rating:
            error_message = "rating must be from {} to {}".format(Song.min_rating, Song.max_rating)
            raise ValueError(error_message)
        else:
            self.rating = self.rate
