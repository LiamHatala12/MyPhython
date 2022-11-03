'''
Program: password
Author: Liam Hatala
Date: 02/24/2022
'''
#open password 
f = open( "password.txt", 'r')

#read password
FilePassword = f.read()

#close file
f.close()

accessGranted = False

#list of valid users
userList = ["admin"]

#get username and check if valid user
username = input("Username: ")

if username in userList:

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
        f = open( "password.txt", 'w')
        #write to file new password
        f.write(str(NewPassword)) 
        #close file
        f.close()
    else:
        print("Ok I Guess not.")