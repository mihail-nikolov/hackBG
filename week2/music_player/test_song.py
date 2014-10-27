import unittest
from song import Song



class SongTest(unittest.TestCase):

    def test_song_init(self):
        harvester_song = Song("Harvester of sorrow", "Metallica", "...And justice for all", 3, 342, 192)
        self.assertEqual(harvester_song.title, "Harvester of sorrow")
        self.assertEqual(harvester_song.artist, "Metallica")
        self.assertEqual(harvester_song.album, "...And justice for all")
        self.assertEqual(harvester_song.rating, 3)
        self.assertEqual(harvester_song.length, 342)
        self.assertEqual(harvester_song.bitrate, 192)

    def test_rate(self):
        harvester_song = Song("Harvester of sorrow", "Metallica", "...And justice for all", 342, 3, 192)
        with self.assertRaises(ValueError):
            harvester_song.rate(200)







if __name__ == '__main__':
    unittest.main()
