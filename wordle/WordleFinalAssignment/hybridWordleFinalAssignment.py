'''
Program: Final Wordle Assignment
Author: Liam H
Date: 07/03/2022
'''




# importing libraries
import os
import sys
import random
import csv

# allow game to run first time
# Note booleans in python are capitalised
play = True

# generates and returns a 5 character hint based on the user's guess
def hint(guess, secretWord):
    # create a list of hints, one for each letter
    hintList = []
    # convert both words to lists
    guess = list(guess)
    secretWord = list(secretWord)

    # will track letters we've given clues about
    cluesSoFar = []

    # loop thru 0-4 (indices of letters in a 5 letter word)
    for i in range(0, 5):
        # checks if each letter matches the corresponding one in the secret word and adds the hint to the list
        if guess[i] == secretWord[i]:
            hintList.append("#")
            # add this to clue list
            cluesSoFar.append(guess[i])
        else:
            hintList.append("-")



    # loop thru 0-4 (indices of letters in a 5 letter word) again
    for i in range(0, 5):
        # check for possible stars - ie it's in the word but not in the right place.
        if guess[i] in secretWord and guess[i] != secretWord[i]:
            # count number of occurances of letter in guess and in secret word
            timesInGuess = guess.count(guess[i])
            timesInAns = secretWord.count(guess[i])
            # if there's fewer or equal number of occurances in the guess than the answer
            # or if we haven't given enough clues yet, we'll give a star.
            if timesInGuess <= timesInAns or cluesSoFar.count(guess[i]) < timesInAns:
                hintList[i] = "*"
            # since we'e given a hint about this letter now, add it to the list of clues so far
            cluesSoFar.append(guess[i])

    # combine hint list into one 5-character string.
    return "".join(hintList)


# prints reason for guessing again (only one) and returns number of guesses so far.
def checkError(currGuess, guessesSoFar, secretWord):

    #open fiveletterDict and set it as a vaiable
    with open(os.path.join(sys.path[0], "fiveletterdict.txt", ), 'r') as f:
        FiveLetter = f.read().splitlines()

    # check if guess is 5 letters
    if len(currGuess) != 5 and currGuess != "":
        print("Your guess must be 5 letters")
    # check if guess is only letters
    elif currGuess != "" and not currGuess.isalpha():
        print("Your guess must contain only letters")
    # if this isn't the first time, tell user guess is wrong or not a word.
    elif currGuess != "" and not FiveLetter:
        print("That's not a word in the bank")
    elif currGuess != "":
        print(" " * 23 + hint(currGuess, secretWord))
        # increase number of guesses (This should only happen if guess was valid)
        guessesSoFar += 1
    return (guessesSoFar)


def playGame(record):
    record["gamesPlayed"] += 1
    # initialise guess so while loop will run
    guess = ""
    # prevents user from guessing more than 6 times.
    tooManyGuesses = False
    # counter for number of guesses
    numGuesses = 0
    # wordbank & this game's secret word

    # read the secretWordsList and choose a random one from there
    with open(os.path.join(sys.path[0],"secretwordslist.txt",),"r",) as f:
        secretWordsList = f.read().splitlines()
    # read the FiveLetterDict to cross-reference when user inputs word
    with open(os.path.join(sys.path[0],"fiveletterdict.txt",), "r",) as f:
        FiveletterList = f.read().splitlines()
    secretWord = random.choice(secretWordsList)
    # get first guess from user
    guess = input("Guess a 5 letter word: ")
    # while loop allows user to guess repeatedly until they are correct.
    while guess.lower() != secretWord:
        numGuesses = checkError(guess, numGuesses, secretWord, FiveletterList)
        if numGuesses == 6:
            tooManyGuesses = True
            break

        # get guess from user
        guess = input("Guess a 5 letter word: ")
    # once loop has terminated, they either guessed correctly or guessed too many times.
    if tooManyGuesses:
        print("Sorry, you've run out of guesses.")
        print(f"The correct answer was {secretWord}")
    else:
        # Increase count by 1 for correct guess
        numGuesses += 1
        record["wins"] += 1
        if record["gamesPlayedOnLastWin"] + 1 == record["gamesPlayed"]:
            record["winStreak"] += 1
        else:
            record["winStreak"] = 1
        record["gamesPlayedOnLastWin"] = record["gamesPlayed"]
        print("That's right!")
        print(f"That took {numGuesses} guesses.")
        
    # Update rest of the records
    record["guessDistribution"][numGuesses - 1] += 1
    record["winRate"] = record["wins"] / record["gamesPlayed"]
    if record["winStreak"] > record["longestStreak"]:
        record["longestStreak"] = record["winStreak"]


    displayRecord(record)
    return record


def displayRecord(record):
    print("--------- Current record ---------")
    for k, v in record.items():
        if k == "guessDistribution":
            dictDistribution = {i + 1: v[i] for i in range(0, len(v))}
            v = dictDistribution
        if k != "wins" and k != "gamesPlayedOnLastWin":
            print(f"{k} : {v}")
    print("--------- End of record ---------")

# allows whole game to be re-played.
# Note that since play is a boolean (True or False), we don't need to put play == True since that just evaluates to True
while play:

    #opens records.csv so that it can pull the players records up
    with open(os.path.join(sys.path[0], "records.csv"), 'r') as f:
        reader = csv.reader(f)
        UserRecords = list(reader)
    
    #Ask player for there username
    username = input("What is yor username? ")
    
    #checkss if the user exists 
    userCheck = False
    userPlace = 0
    for a in range(len(UserRecords)):
        if username == UserRecords[a][0]:
            userCheck = True
            UserPosition = a 
    #if user not exist 
    if not userCheck:
        b = [username]
        for i in range(13):
            b.append("0")
        UserRecords.append(b)
        for a in range(len(UserRecords)):
            if b != UserRecords[a][0]:
                UserPosition = a 

    #defining variables will be used later for stats 
    print(userCheck)
    print(UserPosition)
    print(UserRecords)

    GamesPlayed = int(UserRecords[UserPosition][1])
    Percwin = (UserRecords[UserPosition][2])
    GameWinStreak = int(UserRecords[UserPosition][3])
    HighScoreStreak = int(UserRecords[UserPosition][4])
    WinNumber = int(UserRecords[UserPosition][5])
   
    guessDistribution = []

    for i in range (0,6):
        guessDistribution.append(int(UserRecords[UserPosition][i+6]))
  
    #check if user wants to play again
    again = input("Do you want to play again? ")
    if again.isalpha() and again.lower() != "y" and again.lower() != "yes":
        play = False

print ("Thanks for playing!")