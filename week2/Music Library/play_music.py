import multiprocessing
import sys
import os
from music_crawler import MusicCrawler
from playlist import load
import time


def playSong(mp3s, index):

    while(index < len(mp3s)):
        try:
            os.system("gnome-terminal -e 'play {}'".format(mp3s[index].path))
            time.sleep(mp3s[index].length + 1)
        except:
            print("Error!!")
        index += 1


def menu():
    print("welcome to the best music player ever")
    t = True
    playlist = None
    p = None
    while t:

        print("1. Create new Playlist")
        print("2. Load existing Playlist")
        print("3. Save current playlist")
        print("4. View Playlist")
        print("5. PLay song")
        print("6. Exit")

        choice = input("> ")
        if choice == "1":
            print("Enter name for new Playlist > "),
            name = input()
            print("Enter the filepath to your music > ")
            filepath = input()
            m = MusicCrawler(filepath)
            playlist = m.generate_playlist()
            playlist.name = name
            print("Playlist {}  created".format(playlist.name))

        elif choice == "2":
            print("Enter the filepath to your playlist > ")
            filepath = input()
            playlist = load(filepath)
            if playlist is not None:
                print("Playlist {} loaded".format(playlist.name))

        elif choice == "3":
            if playlist is None:
                print("No playlist loaded")
            else:
                print("Enter filepath to save > ")
                filepath = input()
                playlist.save(filepath)

        elif choice == "4":
            for i, song in enumerate(playlist.songs):
                print("[{}] {}".format(i, song))

        elif choice == "5":
            print("Enter song number > ")
            number = int(input())
            if number < 0 or number >= len(playlist.songs):
                print("song number doesnt exist!")
            else:
                if p is not None:
                    p.terminate()
                    os.system("pkill -9 play")
                p = multiprocessing.Process(target=playSong,
                    args=(playlist.songs, number))
                p.start()
                print()
        elif choice == "6":
            if p is not None:
                p.terminate()
                os.system("pkill -9 play")
            print("Thank you! Come again!")
            sys.exit(0)

        else:
            print("Wrong input! try again")


def main():
    menu()


if __name__ == '__main__':
    main()
