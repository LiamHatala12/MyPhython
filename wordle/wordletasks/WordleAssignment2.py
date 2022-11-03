#Ask for a 5 letter word
print ("hello there this is Wordle, can you guess me a 5 letter word?")

#make word an input so someone can answer
word = input("Whats your guess? ")

#see if the user guessed a 5 letter word

guess = "water"

if len(word) != len(guess) :
    print("you need to guess a 5 letter word")

while word != "water" :
    if word == 6:
        print("there are to many letters in this word")
    if word == 4:
        print("to few letters in this word")
    word = input("guess another 5 letter word: ")

#see if guess is correct
if word == "water":
    print("you are correct")
else:
    print("That's not correct")
    