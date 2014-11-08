import unittest
from music_crawer import Music_crawler


class CrawerTest(unittest.TestCase):

    def test_give_me_files(self):
        new_crawler = Music_crawler("/home/mihail/Music/")
        files = new_crawler._give_me_files("/home/mihail/Music/")
        self.assertEqual(len(files), 6)

    def test_generate_list(self):
        new_crawler = Music_crawler("/home/mihail/Music/")
        playlist = new_crawler.generate_playlist()
        self.assertEqual(len(playlist.songs), 6)


if __name__ == '__main__':
    unittest.main()
