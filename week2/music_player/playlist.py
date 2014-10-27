import json
from song import Song


class Playlist:

    min_quality = 192

    @staticmethod
    def load(file_name):
        file = open("test_file.txt", "r")
        content = file.read()
        file.close()
        json_cont = json.loads(content)
        return Playlist(file_name)

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song_name):
        self.songs.append(song_name)

    def remove_song(self, song_name):
        self.songs.remove(song_name)

    def total_length(self):
        tot_len = 0
        for song in self.songs:
            tot_len += song.length
        return tot_len

    def remove_bad_quality(self):
        tmp_list = []
        for song in self.songs:
            if song.bitrate >= Playlist.min_quality:
                tmp_list.append(song)
        self.songs = tmp_list

    def show_artists(self):
        artists_arr = []
        for song in self.songs:
            if song.artist not in artists_arr:
                artists_arr.append(song.artist)
        return artists_arr

    #def _make_seconds_to_hours_minutes_seconds(self, number):
     #   m, s = divmod(seconds, 60)
      #  h, m = divmod(m, 60)
       # time_str = "%d:%02d:%02d" % (h, m, s)
        #return time_str

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


new_playlist = Playlist("my_playlist")
enter_song = Song("Enter sandman", "Metallica", "Balck album", 2, 300, 192)
harvester_song = Song("Harvester of sorrow", "Metallica", "...And justice for all", 3, 300, 150)
hells_song = Song("Hells Bells", "Ac/DC", "Back in Black", 2, 240, 256)
new_playlist.add_song(hells_song)
new_playlist.add_song(harvester_song)
new_playlist.add_song(enter_song)
#new_playlist.save("json_file.txt")

loading_playlist = Playlist.load("test_file.txt")
print(loading_playlist.songs)
