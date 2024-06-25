import os
import random
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1

# List to keep track of played songs
played_songs = []

# Player class to keep track of player name and score
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

# Function to get a random song from the 'songs' directory
def getSong():
    songPath = f"songs/{random.choice(os.listdir('songs'))}"
    song = MP3(f"{songPath}", ID3=ID3)
    songLength = song.info.length
    title = song.get("TIT2")
    artist = song.get("TPE1")
    return songPath, songLength, title, artist

# Function to play a preview of a song
def playSong(previewLength):
    songPath, songLength, title, artist = getSong()
    input("\tHit Enter To Start The Preview!")  
    print("\tPlaying")
        
    # Calculate a random start and end point for the preview
    randomStart = random.randint(10, int(songLength) - 30)    
    randomEnd = randomStart + previewLength
    osCommand = f'mpv --start={randomStart} --end={randomEnd} --no-video --really-quiet "{songPath}"'
    os.system(osCommand)
    return title, artist

# Simualarity threshold for correct answer
similarityThreshold = 50

# Get number of players and preview length from user
numberOfPlayers = int(input("How many players? "))

# Create player objects and add to playerList
playerList = []
for player in range(numberOfPlayers):
    playerName = input(f"Player {player + 1} name: ")
    playerList.append(Player(playerName))

previewLength = int(input("How long should the preview be? (2-10)"))

# Get number of rounds from user
rounds = int(input("How many rounds? "))
    
# Main game loop
for round in range(rounds):
    for player in playerList:
        print(f"Round {round + 1}")
        print(f"\n\nPlayer: {player.name}")
        title, artist = playSong(previewLength)
        guess = input("What is the song title? ")
        
        # Calculate similarity between guess and actual title
        similarity = fuzz.ratio(guess, title.text)
 
        if similarity > similarityThreshold:
            player.score += 1
            print(f"\nCorrect!")
            print(f"{title} by {artist}")
        else:   
            print(f"\nIncorrect!") 
            print(f"Correct answer: {title}")
    
    # Print scores after each round
    print("\nPlayer Scores:")
    for player in playerList:
        print(f"\t{player.name}: {player.score}")   
