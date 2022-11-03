'''
Program: Trivia Game
Author: Mrs K
Date: 2022-02-16
'''

import os
import sys

#open the document for reading
with open(os.path.join(sys.path[0],"LeaderBoard.csv"), 'r') as f:
    leaderboard = f.read().splitlines()

    for i in range(len(leaderboard)):
        leaderboard[i] = leaderboard[i].split(',')

print(leaderboard)

score = 0

#Asks a question and checks the answer. Returns 1 if it's right and 0 if it's wrong.
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
         "Uluru is a large rock formation sacred to the Pitjantjatjara people in the centre of which country? "]

aList = ["Paris",
         "Russia",
         "Beijing",
         "Easter Island",
         "Australia"]

#Ask each question
for i in range(len(qList)):
    qstn= qList[i]
    ans = aList[i]
    #track score
    score = score + askQuestion(qstn, ans)
'''
print(f'Your score is {score}.')

newHiscores = []
newLeaders = []


if score > int(hiscores[-1]):
    print("Congratulations, you made the leaderboard!")
    player = input("What's your name? ")

    playerOnList = False

    for i in range(0, len(hiscores)):
        if score > int(hiscores[0]) and not playerOnList:
            newHiscores.append(str(score))
            newLeaders.append(player)
            playerOnList = True
        else:
            newHiscores.append(hiscores[0])
            hiscores = hiscores[1:]
            newLeaders.append(leaders[0])
            leaders = leaders[1:]
        
    with open(os.path.join(sys.path[0],"hiscores.txt"), 'w') as f:
        for score in newHiscores:
            f.write(score + "\n")

    with open(os.path.join(sys.path[0],"leaders.txt"), 'w') as f: 
        for name in newLeaders:
            f.write(name+"\n")

else:
    newHiscores = hiscores
    newLeaders = leaders

print("\nNAME:          SCORE:")
print("---------------------")
for i in range(0,len(newHiscores)):
    print(f'{newLeaders[i]:<15}{newHiscores[i]}')
'''