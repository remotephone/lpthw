# Define the class Song. 

class Song(object):

# instantiate it, pass two items to it, itself and lyrics
# lyrics will be the strings. 
    def __init__(self, lyrics):
        self.lyrics = lyrics

# define the function sing_me_a_song. We're doing a for loop, it'll read each
# line in self.lyrics, which we defined above, and then print the lines. 
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

# We assign the class to Happy Birthday with different objects assigned to it.
# So we earlier passed self and Lyrics. You can see Self where we write Song
# and then lyrics are the words in parenthenses. Each string in the parentehses
# is one of the lines in self.lyrics. 
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop righty there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

wut_wut = Song(["Wut wut",
                "la la la"])

# Then we call the assignemnts we just made and run the function
# sing_me_a_song() which prints each line of the song.
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

wut_wut.sing_me_a_song()


## Now we pass a variable instead

# first set the value for words. The brackets let us split it up line by line
# without weird spaces.
words = ["Hello this is a song",
        "It is not very long"]

# now we assign words_song to the result of class(object)
words_song = Song(words)

# then we run the sing_me_a_song() functionc
words_song.sing_me_a_song()

