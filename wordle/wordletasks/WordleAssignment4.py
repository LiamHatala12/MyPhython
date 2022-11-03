'''
Program: Wordle Wednesday
Author: Liam Hatala
Date: 2022-02-11

'''

#import random library for choosing a random secret word.
import random

#allow game to run first time
#Note booleans in python are capitalised
play = True

#prints reason for guessing again (only one) and returns number of guesses so far.
def checkError(currGuess, guessesSoFar):
    #check if guess is 5 letters
    if len(currGuess) != 5 and currGuess != "":
        print("Your guess must be 5 letters")
    #check if guess is only letters
    elif currGuess != "" and not currGuess.isalpha():
        print("Your guess must contain only letters")
    #if this isn't the first time, tell user guess is wrong.
    elif currGuess != "":
        print("That's wrong, try again")
        #increase number of guesses (This should only happen if guess was valid)
        guessesSoFar += 1
    return(guessesSoFar)

def playGame():
    #initialise guess so while loop will run
    guess = ""

    #counter for number of guesses
    numGuesses = 0

    #wordbank & this game's secret word
    wordList = ["brave", "smart", "pride", "among","charm","elbow", "loves", "drive","abide", "plant"]
    secretWord = random.choice(wordList)
    
    # while loop allows user to guess repeatedly until they are correct.
    while guess != secretWord:

        numGuesses = checkError(guess, numGuesses)

        #get guess from user
        guess = input("Guess a 5 letter word: ")

        #this converts guess to lowercase (so APPLE matches apple). If statement prevents error.
        if guess.isalpha():
            guess = guess.lower()

    

    #once loop has terminated, they must have guessed correctly.
    #Increase count by 1 for correct guess
    numGuesses += 1
    print("That's right!")
    print(f"That took {numGuesses} guesses.")


#allows whole game to be re-played.
#Note that since play is a boolean (True or False), we don't need to put play == True since that just evaluates to True

while play:
    playGame()

    #check if user wants to play again
    again = input("Do you want to play again? ")
    if again.isalpha() and again.lower() != "y" and again.lower() != "yes":
        play = False

print ("Thanks for playing!")