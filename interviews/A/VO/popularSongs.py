from random import randint  

START = 1 
END = 3

class Song:
    
    def __init__(self, name, popularity):
        self.name = name 
        self.popularity = popularity
        self.order = 1 

class Solution:
    def sortPopluarSongs(self, songs):

        for song in songs:
            song.order = song.popularity * randint(START, END) 

        songs = sorted(songs, key = lambda song : (song.order, song.popularity, song.name), reverse = True)

        return songs 

song_name = ["Love the way you lie", "Just give me a resson", "Need you now",
             "Back to Decemember", "We are never ever getting back together"]

songs = [] 

for i in range(len(song_name)):

    songs.append(Song(song_name[i], i + 1))

solution = Solution()

for song in solution.sortPopluarSongs(songs):
    print(str(song.order) + " " + song.name + " " + str(song.popularity))