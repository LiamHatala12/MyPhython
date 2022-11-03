'''
Program: Wordle With Dicitonary
Author: Liam H
Date: 2022-03-11

Instructions:
0. Please use this file as a base. Don't modify the hint() or checkerror() functions.
1. Create a csv file with user records in it.(When you hand it in, have sample data in there)
2. Determine an appropriate place in your program to ask the user for their name.
3. After each game, show the user their record.
    The record should include:
    a. How many games they've played
    b. How many they've won in a row (win streak)
    c. Their longest win streak
    d. Their win %
    e. Their score distribution (how many times did they get the right answer in 1, 2, 3, 4, 5, 6 guesses)
4. You should also be able to read a user record in from the file, so that you can determine if the user has played before.

The following must be different to your previous solution:
You must choose how to organise/format this information to present to the user
You must choose what information to store in the CSV and in what order.
Note: you don't necessarily need to store every number related to the statistics.
'''

# import random library for choosing a random secret word.

import csv
import json
import os
import random
import sys


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
def checkError(currGuess, guessesSoFar, secretWord, FiveLetterList):
    # check if guess is 5 letters
    if len(currGuess) != 5 and currGuess != "":
        print("Your guess must be 5 letters")
    # check if guess is only letters
    elif currGuess != "" and not currGuess.isalpha():
        print("Your guess must contain only letters")
    # check if guess is a valid word
    elif currGuess not in FiveLetterList:
        print("Your guess must be a supported word")
    # if this isn't the first time, tell user guess is wrong.
    elif currGuess != "":
        print(" " * 23 + hint(currGuess, secretWord))
        # increase number of guesses (This should only happen if guess was valid)
        guessesSoFar += 1
    return guessesSoFar

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
        #add 1 to wins in the csv
        record["wins"] += 1
        #if 
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

#prints users record
#The .items(): method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.
def displayRecord(record):
    print("--------- Current record ---------")
    #k stands for key and v stands for value, in order to loop through keys and values you need records.items and k and v
    for k, v in record.items():
        #if the key is == to guessdistro the values are 
        if k == "guessDistribution":
            # value is = a comprehension that builds a dictionary based on the guess history
            dictDistribution = {i + 1: v[i] for i in range(0, len(v))}
            v = dictDistribution
        # if the key is not equal to the number of wins and the keys are also not equal to the the gamesplayedonlastwin
        if k != "wins" and k != "gamesPlayedOnLastWin":
            print(f"{k} : {v}")
    print("--------- End of record ---------")

# saves players data to csv 
#The csv.DictWriter class operates like a regular writer but maps Python dictionaries into CSV rows. 
#The fieldnames parameter is a sequence of keys that identify the order in which values in the dictionary passed to the writerow method are written to the CSV file.
def saveHistoryRecord(historyRecord):
    with open(os.path.join(sys.path[0], f"history_record.csv"), "w+") as csvFile:
        fieldnames = [ "name","guessDistribution","gamesPlayed","gamesPlayedOnLastWin","wins","winRate","winStreak","longestStreak",]
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)

        #The writeheader method writes the headers to the CSV file.
        writer.writeheader()
        
        #The writerow method writes a row of data into the specified file. It is possible to write all data in one shot. 
        #The writerows method writes all given rows to the CSV file.
        writer.writerows(historyRecord)


def loadHistoryRecord():
    if os.path.isfile(os.path.join(sys.path[0], "history_record.csv")):
        with open(os.path.join(sys.path[0], "history_record.csv"), "r") as f:

            #The csv.DictReader class operates like a regular reader but maps the information read into a dictionary. 
            #The keys for the dictionary can be passed in with the fieldnames parameter or inferred from the first row of the CSV file.
            #converting the list of lines read in from the csv into a list of dictionaries using a comprehension
            history_record = [{k: v for k, v in row.items()}for row in csv.DictReader(f, skipinitialspace=True)]
        return history_record
    return None


if __name__ == "__main__":

    #start game
    play = True

    #ask player there name
    userName = input("Input your name: ")

    #when this var is calling the function loadhistoryrecord
    historyRecord = loadHistoryRecord()

    # seting user record to none/null or 0
    userRecord = None
    # if the historyrecord is = to what is in the for loop 
    if historyRecord:
        for currRecord in historyRecord:
            #if the current records name is the same an already existing name
            if currRecord["name"] == userName:
                #
                userRecord = currRecord
                #json. loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary, in this case guessdistro
                userRecord["guessDistribution"] = json.loads(userRecord["guessDistribution"])
                #recording all data into intgers and the winrate into a float value because its a percent 
                userRecord["gamesPlayed"] = int(userRecord["gamesPlayed"])
                userRecord["gamesPlayedOnLastWin"] = int(userRecord["gamesPlayedOnLastWin"])
                userRecord["wins"] = int(userRecord["wins"])
                userRecord["winRate"] = float(userRecord["winRate"])
                userRecord["winStreak"] = int(userRecord["winStreak"])
                userRecord["longestStreak"] = int(userRecord["longestStreak"])

    #if the user record is not = 
    if not userRecord:
        #this is setting the player initial record to all the bellow values for everything
        initialUserRecord = True
        userRecord = {
            "name": userName,
            "guessDistribution": [0] * 6,
            "gamesPlayed": 0,
            "gamesPlayedOnLastWin": 0,
            "wins": 0,
            "winRate": 0,
            "winStreak": 0,
            "longestStreak": 0,
        }

    else:
        initialUserRecord = False
    # allows whole game to be re-played.
    # Note that since play is a boolean (True or False), we don't need to put play == True since that just evaluates to True
    while play:
        userRecord = playGame(userRecord)
        if historyRecord:
            if initialUserRecord:
                historyRecord.append(userRecord)
            else:
                #enmerate is a that function gives you back two loop variables, and is turning the list of records into a numbered list
                for idx, currRecord in enumerate(historyRecord):
                    #these are the vars for enumerate
                    if currRecord.get(userName, None):
                        historyRecord[idx] = userRecord
        else:
            historyRecord = [userRecord]


        # check if user wants to play again
        again = input("Do you want to play again? ")
        if again.isalpha() and again.lower() != "y" and again.lower() != "yes":
            play = False


    saveHistoryRecord(historyRecord)
    print("Thanks for playing!")