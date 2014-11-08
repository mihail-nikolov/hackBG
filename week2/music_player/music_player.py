import os
from mutagen.mp3 import MP3
from song import Song
from music_crawer import Music_crawler
from playlist import Playlist

    #adding some songs

seven_words = Song("7_words", "Deftones", "Unknown alb", 342, 3, 192)
butterfly_song = Song("butterfly", "Parvo stealer", "Unknown alb", 342, 3, 192)
alive_song = Song("alive", "P.O.D", "Unknown alb", 342, 3, 192)
songs_arr = [seven_words, butterfly_song, alive_song]


def split_command_str(command):
    arr = command.split(" ")
    return arr


def the_command(command_tuple, command):
    return command_tuple[0] == command


def unknown_command():
    message = "Unknown command, you can use one the the following commands:\
                    \n generate <path> - generate a new playlist from folder.\
                    \n clear_bitrate <number> - delete songs by rate < <number>\
                    \n clear_rating <number> -  delete songs by rating < <number>\
                    \n remove_song <title> - delete song\
                    \n add_song <title> - add song>\
                    \n load <file> - load an existing playlist\
                    \n save <file> - save the current playlist\
                    \n finish - to finish the program"
    return message


def start_message():
    start_message = "Hello, Welcome to the Music Player\
                    \n Here are the commands you can use:\
                    \n generate <path> - generate a new playlist from folder.\
                    \n clear_bitrate <number> - delete songs by rate < <number>\
                    \n clear_rating <number> -  delete songs by rating < <number>\
                    \n remove_song <title> - delete song\
                    \n add_song <title> - add song>\
                    \n load <file> - load an existing playlist\
                    \n save <file> - save the current playlist\
                    \n finish - to finish the program "
    return start_message


def songs_to_add():
    song_names_arr = []
    for song in songs_arr:
        song_names_arr.append(song.title)
    return song_names_arr


def main():

    #new_songs_arr = []
    print(start_message())
    print(songs_to_add())
    new_playlist = Playlist("my_playlist")
    while True:
        command = split_command_str(input("Enter command>"))

        if the_command(command, "generate"):
            new_crawler = Music_crawler(command[1])
            new_playlist = new_crawler.generate_playlist()
            print(new_playlist.str_func())

        elif the_command(command, "remove_disrated"):
            new_playlist.remove_disrated(int(command[1]))
            print(new_playlist.str_func())

        elif the_command(command, "remove_bad_quality"):
            new_playlist.remove_bad_quality()
            print(new_playlist.str_func())

        elif the_command(command, "remove"):
            new_playlist.remove_song(command[1])
            print(new_playlist.str_func())

        elif the_command(command, "add"):
            for song in songs_arr:
                if command[1] == song.title:
                    new_playlist.add_song(song)
                    break
            print(new_playlist.str_func())

        elif the_command(command, "load"):
            new_playlist.load(command[1])
            print(new_playlist.str_func())

        elif the_command(command, "save"):
            new_playlist.save(command[1])

        elif the_command(command, "finish"):
            print("GoodBye. Thank you for using the player")
            break

        else:
            print(unknown_command())


if __name__ == '__main__':
    main()

"""
        elif the_command(command, "remove_song"):
            for song in new_playlist.songs:
                if command[1] != song.title:
                    new_songs_arr.append(song)
            new_playlist.songs = new_songs_arr
            new_songs_arr = []
            print(new_playlist.str_func())

        elif the_command(command, "add_song"):
            songs_arr = songs_to_add()
            for song in songs_arr:
                if command[1] == song.title:
                    new_playlist.add_song(song)
                    break
"""
