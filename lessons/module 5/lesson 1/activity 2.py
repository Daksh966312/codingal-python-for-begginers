class Song:
    def __init__(self, name, artist, instruments, genre):
        self.name = name
        self.artist = artist
        self.instruments = instruments
        self.genre = genre 
#name, lyrics, beats, rhythm, artist, instruments
    
    def info(self):
        print("name: ", self.name)
        print("artist: ", self.artist)
        print("instrument: ", self.instruments)
        print("genre: ", self.genre)

s1 = Song("outta my league", "stellar", ["keyboard", "electronic drums"],"indie pop" )

# print("name: ", s1.name)

s1.info()