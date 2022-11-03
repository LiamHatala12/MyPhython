'''
Program: password
Author: Liam Hatala
Date: 02/24/2022
'''

import os
import sys

#open password 
with open(os.path.join(sys.path[0],"password.txt"),"r") as f:
#read password
    FilePassword = f.read()
#check access
accessGranted = False

#open UserName
with open(os.path.join(sys.path[0],"UserName.txt"),"r") as f:
#read UserName
    FileUserName = f.read()
#Check if username is valid
userList = FileUserName
#get username and check if valid user
FileUserName = input("Username: ")

if FileUserName in userList:

    #get password & check if valid
    password = input("Password: ")
    
    if password == FilePassword: 
        accessGranted = True
    else:
        print("Access Denied")

else:
    print ("User not found")

if accessGranted:
    print("------------------")
    print("| Access Granted |")
    print("------------------")

    PasswordChange = input("Would you Like to Change your Password? ")

    if PasswordChange == "yes":
        NewPassword = input("What would you like to change it to? ")
        #open file for new password
        with open(os.path.join(sys.path[0],"password.txt"),"a") as f:
        #write to file new password
            f.write(str(NewPassword)+"\n") 
    else:
        print("Ok I Guess not.")

    UsernameChange = input("Would you like use a different acount. ")
    
    if UsernameChange == "yes":
        NewUsername = input("whats your username? ")
        
        #open file for new name
        with open(os.path.join(sys.path[0],"UserName.txt"),"a") as f:
        #write to file
            f.write(NewUsername+"\n")
    else:
        print("Ok thats alright.")