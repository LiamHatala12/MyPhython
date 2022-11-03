'''
Author: Liam Hatala
Purpose: generates random stock values
Date: Tuesday, May 17
'''

#importing nessisary libraries 
import random
import os
import sys
import csv

def random_stock(iterations):

    #making an open arry called stock_list
    stock_list = []
    #seting the initial value to 0
    value = 0
    #making sure the maximum stock that the warehouse can hold is 10000 units
    MaxStock = 10000
    #the minimum stock that we want at anytime in the warehouse is 100
    MinStock = 100

    for _ in range(iterations):

        #to start off the value is increased by a random number from 0 to 1000
        value += random.randint(0, 1000)

        #if the value is less than 2000
        if value < 2000:
            #increase it from a random number in the range of 1000 to 1500
            value += random.randint(1000, 1500)

        #but if the number is already greater than 10000 guarantee that there will be a subtraction of a random number in the range of 1000 to 2500
        elif(value > 10000):
            value -= random.randint(1000, 2500)

        #if the value is greater than 2000 and less than 10000 than randomly add or subtract a number in the range of 1500 to 2500
        else:
            value += random.choice([-1,1]) * random.randint(1500, 2500)

        #if the value is less than 0 than set the number to the minstock value that was set
        if value < 0:
            value = MinStock
        
        #if the number is greater than 10000 after adding, set it equal to the maxstock value
        if value > 10000:
            value = MaxStock
        
        #from stock_list append the values
        stock_list.append(value)
    return stock_list

def Data_Record():

        #print 24 instances of the generation
    n = 25

    for i in range(5):

        #stock_list is being set to the generation function n amount of times
        stock_list = random_stock(n)

        #this is sending the data to a txt file
        with open(os.path.join(sys.path[0], "randomData.csv"), 'w', newline = "") as f:
            writer = csv.writer(f)
            for i in range(5):
                stock_list = random_stock(n)
                writer.writerow((stock_list))

        #printing the numbers in the terminal so people can see them
        #print(stock_list)

Data_Record()