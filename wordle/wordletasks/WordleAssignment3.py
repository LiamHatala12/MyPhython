'''
Program: Wordle Tuesday
Author: Liam Hatala
Date: 2022-02-16
'''

#initialise guess so while loop will run
guess = ""

#counter for number of guesses
numGuesses = 0

# while loop allows user to guess repeatedly until they are correct.
while guess != "apple":

    #The following ensures only one error message will appear to the user
    #check if guess is 5 letters
    if len(guess) != 5 and guess != "":
        print("Your guess must be 5 letters")
    #check if guess is only letters
    elif guess != "" and not guess.isalpha():
        print("Your guess must contain only letters")
    #if this isn't the first time, tell user guess is wrong.
    elif guess != "":
        print("That's wrong, try again")
        #increase number of guesses (This should only happen if guess was valid)
        numGuesses += 1

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