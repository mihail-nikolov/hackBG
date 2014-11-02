import os
from mutagen.mp3 import MP3
from song import Song
from playlist import Playlist


class Music_crawler:

    audio_title = 'TIT2'
    audio_artist = 'TPE1'
    audio_album = 'TALB'
    def_title = 'unkwnow title'
    def_artist = 'unkwnow artist'
    def_album = 'unkwnow album'
    def_rate = 0

    def __init__(self, path):
        self.path = path

    def _give_me_files(self, path):
        files = os.listdir(self.path)
        song_files = []
        for file in files:
            if file.endswith(".mp3"):
                song_files.append(file)
        return song_files

    def _give_me_tags(self, audio):
        tags_dict = {}
        tags_dict['title'] = audio.get(self.audio_title, self.def_title)
        tags_dict['artist'] = audio.get(self.audio_artist, self.def_artist)
        tags_dict['album'] = audio.get(self.audio_album, self.def_album)
        return tags_dict

    def _get_bitrate(self, audio):
        return audio.info.bitrate

    def _get_length(self, audio):
        return int(audio.info.length)

    def _get_rating(self, audio):
        return audio.get(self.def_rate)

    def _make_the_song(self, song_file):
        song_tags = self._give_me_tags(song_file)
        song_length = self._get_length(song_file)
        song_bitrate = self._get_bitrate(song_file)
        song = Song(str(song_tags['title']), str(song_tags['artist']), str(song_tags['album']), str(self.def_rate), str(song_length), str(song_bitrate))
        return song

    def generate_playlist(self):
        the_playlist = Playlist("new_playlist")
        files = self._give_me_files(self.path)
        for file_name in files:
            file_name = self.path + file_name
            song_file = MP3(file_name)
            song = self._make_the_song(song_file)
            the_playlist.add_song(song)
        return the_playlist


new_crawler = Music_crawler("/home/mihail/Music/")
playlist = new_crawler.generate_playlist()
print(playlist.str_func())
