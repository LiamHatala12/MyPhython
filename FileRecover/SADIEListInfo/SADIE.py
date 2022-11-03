'''
Program: SADIE the Chatbot
Author: Liam Hatala
Date: 2022-02-10
'''

#Welcome
print("Hello, I'm SADIE - Someone Artificial Discussing Interesting Events")

#Name and greeting
name = input("What is your name? ")

if name == "Liam":
    print("Oh, of course, my creator!")
elif name == "Sadie":
    print("That's my name too!")
else:
    print(f'Hello, {name}. Good to meet you!')

#SADIE only wants to talk about unicorns.
#Gets user input repeatedly until user suggests unicorns.
topic = input("What would you like to talk about? ")

while topic != "unicorns":
    print("No thanks, that's boring!")
    topic = input("What would you like to talk about? ")

print("Yes I LOOOVE unicorns.")

file = open("colours.txt", 'r')

colourList = file.read().splitlines()

file.close()

#creates text for different coloured unicorns
def ilove(col):
    return f"I love {col} unicorns and..."

#SADIE states her love for all types of unicorns
for colour in colourList:
    print(ilove(colour))
    
print("that's all")

NewColour = input("what colour of unicorns do you like? ")

colourList.append(NewColour)

file = open("colours.txt", 'w')

for colour in colourList:
    file.write(colour+"\n")

file.close()

print("Goodbye")