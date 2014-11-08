import unittest
from playlist import Playlist
from song import Song


class PlaylistTest(unittest.TestCase):

    def test_playlist_init(self):
        new_playlist = Playlist("my_playlist")
        self.assertEqual(new_playlist.name, "my_playlist")

    def test_add_song(self):
        new_playlist = Playlist("my_playlist")
        harvester_song = Song("Harvester of sorrow", "Metallica", "...And justice for all",3 , 342, 192)
        new_playlist.add_song(harvester_song)
        self.assertIn(harvester_song, new_playlist.songs)

    def test_remove_song(self):
        new_playlist = Playlist("my_playlist")
        harvester_song = Song("Harvester of sorrow", "Metallica", "...And justice for all",3 , 342, 192)
        enter_song = Song("Enter sandman", "Metallica", "Balck album", 300, 2, 192)
        new_playlist.songs.append(harvester_song)
        new_playlist.songs.append(enter_song)
        new_playlist.remove_song("Harvester of sorrow")
        self.assertEqual(len(new_playlist.songs), 1)

    def test_total_length(self):
        new_playlist = Playlist("my_playlist")
        harvester_song = Song("Harvester of sorrow", "Metallica", "...And justice for all", 3, 300, 192)
        enter_song = Song("Enter sandman", "Metallica", "Balck album", 2, 300, 192)
        new_playlist.songs.append(harvester_song)
        new_playlist.songs.append(enter_song)
        self.assertEqual(new_playlist.total_length(), 600)

    def test_remove_bad_quality(self):
        new_playlist = Playlist("my_playlist")
        enter_song = Song("Enter sandman", "Metallica", "Balck album", 2, 300, 192000)
        harvester_song = Song("Harvester of sorrow", "Metallica", "...And justice for all", 3, 300, 150000)
        new_playlist.songs.append(harvester_song)
        new_playlist.songs.append(enter_song)
        new_playlist.remove_bad_quality()
        self.assertEqual(len(new_playlist.songs), 1)

    def test_remove_disrated(self):
        new_playlist = Playlist("my_playlist")
        enter_song = Song("Enter sandman", "Metallica", "Balck album", 2, 300, 192)
        enter_song1 = Song("Enter sandman", "Metallica", "Balck album", 2.5, 300, 192)
        harvester_song = Song("Harvester of sorrow", "Metallica", "...And justice for all",4 , 300, 150)
        new_playlist.songs.append(harvester_song)
        new_playlist.songs.append(enter_song1)
        new_playlist.songs.append(enter_song)
        new_playlist.remove_disrated(3)
        self.assertEqual(len(new_playlist.songs), 1)
        self.assertEqual(new_playlist.songs[0], harvester_song)

    def test_show_artists(self):
        new_playlist = Playlist("my_playlist")
        enter_song = Song("Enter sandman", "Metallica", "Balck album", 2, 300, 192)
        harvester_song = Song("Harvester of sorrow", "Metallica", "...And justice for all",3 , 300, 150)
        hells_song = Song("Hells Bells", "Ac/DC", "Back in Black",2 , 240, 256)
        new_playlist = Playlist("my_playlist")
        new_playlist.songs.append(harvester_song)
        new_playlist.songs.append(enter_song)
        new_playlist.songs.append(hells_song)
        self.assertEqual(len(new_playlist.show_artists()), 2)

    def test_str(self):
        new_playlist = Playlist("my_playlist")
        enter_song = Song("Enter sandman", "Metallica", "Balck album", 2, 300, 192)
        harvester_song = Song("Harvester of sorrow", "Metallica", "...And justice for all",3 , 300, 150)
        new_playlist = Playlist("my_playlist")
        new_playlist.songs.append(harvester_song)
        new_playlist.songs.append(enter_song)
        expected_string = "Metallica - Harvester of sorrow 300\nMetallica - Enter sandman 300\n"
        self.assertEqual(expected_string, new_playlist.str_func())

    def test_empty_str(self):
        new_playlist = Playlist("my_playlist")
        expected_string = ""
        self.assertEqual(expected_string, new_playlist.str_func())


if __name__ == '__main__':
    unittest.main()
