import json
from song import Song


class Playlist:

    min_quality = 192000

    def __init__(self, name):
        self.name = name
        self.songs = []

    def _read_file(self, file_name):
        file = open(file_name, 'r')
        file_content = file.read()
        file_content = json.loads(file_content)
        file.close()
        return file_content
#have to be made some corrrections in add and remove song!
#maybe the info could be get from existing arr of song objects!

    def add_song(self, song_name):
        self.songs.append(song_name)

    def remove_song(self, song_title):
        new_list = []
        for song in self.songs:
            if song.title != song_title:
                new_list.append(song)
        self.songs = new_list

    def total_length(self):
        tot_len = 0
        for song in self.songs:
            tot_len += song.length
        return tot_len

    def remove_disrated(self, rating):
        rated_songs = []
        for song in self.songs:
            if int(song.rating) >= rating:
                rated_songs.append(song)
        self.songs = rated_songs

    def remove_bad_quality(self):
        new_list = []
        for song in self.songs:
            if int(song.bitrate) >= Playlist.min_quality:
                new_list.append(song)
        self.songs = new_list

    def show_artists(self):
        artists_arr = []
        for song in self.songs:
            if song.artist not in artists_arr:
                artists_arr.append(song.artist)
        return artists_arr

    def str_func(self):
        playlist_string = ""
        for song in self.songs:
            playlist_string += song.artist + " - " + song.title +" " + str(song.length) + "\n"
        return playlist_string

    def make_json_string(self):
        songs_array = []
        json_dic = {}
        for song in self.songs:
            songs_array.append(song.__dict__)
        json_dic["name"] = self.name
        json_dic["songs"] = songs_array
        return json_dic

    def save(self, the_file):
        json_dic = self.make_json_string()
        file = open(the_file, "w")
        file.write(json.dumps(json_dic))
        file.close()

    def load(self, file_name):
        file_content = self._read_file(file_name)
        #file_data = json.load(file_content)
        for song in file_content['songs']:
            self.add_song(
                Song(song['title'], song['artist'], song['album'], song['rating'], song['length'], song['bitrate']))


"""
   @staticmethod
    def load(file_name):
        #file_content = self._read_file(file_name)
        with open(file_name, 'r') as file_content:
            file_data = json.load(file_content)
        playlist = Playlist(file_data['name'])
        for song in file_data['songs']:
            playlist.add_song(
                Song(song['title'], song['artist'], song['album'], song['rating'], song['length'], song['bitrate']))
        return playlist
"""
#защо тук не работи read_file?????????????????!!!!!

    #def _make_seconds_to_hours_minutes_seconds(self, number):
     #   m, s = divmod(seconds, 60)
      #  h, m = divmod(m, 60)
       # time_str = "%d:%02d:%02d" % (h, m, s)
        #return time_str
