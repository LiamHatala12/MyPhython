'''
Program: password
Author: Liam H
Date:
'''

import os
import sys

accessGranted = False

#list of valid and corresponding passwords
with open(os.path.join(sys.path[0],"UserName.txt"),"r") as f:
    userList = f.read().splitlines()

with open(os.path.join(sys.path[0],"password.txt"),"r") as f:
    passwords = f.read().splitlines()

#log in or sign up

action = input("Would you like to 1. login or 2. sign up? ")

if action == "1":

    #get username and check if valid user
    username = input("Username: ")

    if username in userList:

        usernum = userList.index(username)

        #get password & check if valid
        password = input("Password: ")
        
        if password == passwords[usernum]:
            accessGranted = True
        else:
            print("Access Denied")

    else:
        print ("User not found")


    if accessGranted:
        print("------------------")
        print("| Access Granted |")
        print("------------------")


        #update password option
        update = input("Update password?")

        if update.lower()[0] == "y":
            newPass = input("Enter new password: ")
            passwords[usernum] = newPass
            with open(os.path.join(sys.path[0],"passwords.txt"),"w") as f:
                for pw in passwords:
                    f.write(pw+"\n")

            print("Password registered!")
            
else:
    print("-----------")
    print("| Sign Up |")
    print("-----------")
    username = input("Choose a username: ")
    while username in userList:
        print ("Username is taken, try again")
        username = input("Choose a username: ")

    password = input("Choose a password: ")

    with open(os.path.join(sys.path[0],"password.txt"),"a") as f:
        f.write(password+"\n")

    with open(os.path.join(sys.path[0],"UserName.txt"),"a") as f:
        f.write(username+"\n")

    print("Registered!")

print("Goodbye!")