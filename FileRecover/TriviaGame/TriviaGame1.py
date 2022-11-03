'''
Program: Trivia Game
Author: Liam Hatala
Date: 2022-02-16
'''

import os
import sys

#opening the document for reading the highscore
with open(os.path.join(sys.path[0],"highscore.txt"), 'r') as f:

#read info from the file
    highscore = f.read()

score = 0

#Asks a question and checks the answer.
#Returns 1 (for one point) if it's right and 0 if it's wrong
def askQuestion(question, answer):
    guess = input(question)
    if guess.lower() == answer.lower():
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

#Define Questions and Answers
qList = ["What city is the Eiffel Tower located in? ",
         "What is the largest country in the world, by area? ",
         "What city is hosting the 2022 Winter Olympics? ",
         "Where would you find the monolithic stone heads known as Mo'ai? ",
         "Uluru is a large rock formation sacred to the Pitjantjatjara people in the centre of what country? "]

aList = ["Paris",
         "Russia",
         "Beijing",
         "Easter Island",
         "Australia"]

#ask each question

for i in range(len(qList)):
    qstn = qList[i]
    ans = aList[i]
    #track score
    score = score + askQuestion(qstn, ans)

print(f'Your score is {score}')

if score > int(highscore):
    print("congradulations, new highscore!")
    #open file
    with open(os.path.join(sys.path[0],"highscore.txt"), 'r') as f:
        f.write ("{leader} with a score of {score}"+"\n")

elif score == int(highscore):
    print("awesome you tied the highscore!")

    #get the name of the highscore leader.
    leader = input("what is your name? ")

    with open(os.path.join(sys.path[0],"leader.txt"), 'a') as f:
        f.write(leader+"\n")

    #print name of leader
    with open(os.path.join(sys.path[0],"leader.txt"), 'r') as f:
        f.read()
        print(f"the most recent highscore holder is {leader}")