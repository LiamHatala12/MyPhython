'''
Name: Liam H
Program: interpolation Search
Date: Saturday, April 2
'''
#this the the same type of function that we used before just a def with four seperate varibles this time
#pos is the position of key being searched
#list[] os where the elements need to be searched
#x is the element needing to be searched
#lo is the starting of the index in the arr[]
#hi is the ending of the index in the arr[]
def interpolationSearch(list, lo, hi, x):
 
    #This is the interpolation equation with the varibles subbed in
    if (lo <= hi and x >= list[lo] and x <= list[hi]):
 
        # this is the equation simplified because 0 + ((99-0) // (969-9)) * 795 - 9 
        pos = lo + ((hi - lo) // (list[hi] - list[lo]) * (x - list[lo]))
 
        # if the value calculated is the x value return pos
        if list[pos] == x:
            return pos
 
        # If x is larger than the calculated value, x is in then right subarray
        if list[pos] < x:
            #returning this is basiclly saying that return the function with the vars as the same array, the position plus 1
            #the high value and the value being looked for, pos + 1 is basiclly saying that take the calculated position and add one because u need to search the next subarray
            return interpolationSearch(list, pos + 1, hi, x)
 
        # If x is smaller the the calculated value, x is in the left subarray
        if list[pos] > x:
            #returning this is basiclly saying that return the function with the vars as the same array, the position minus 1
            #the low value and the value being looked for, pos - 1 is basiclly saying that take the calculated position and add one because u need to search the next subarray
            return interpolationSearch(list, lo, pos - 1, x)

    return -1
 
#this is the array being searched
list = [9, 56, 69, 73, 82, 92, 133, 145, 146, 150,
163, 180, 181, 190, 192, 199, 201, 218, 225, 242,
245, 251, 265, 271, 274, 282, 299, 307, 313, 322,
324, 340, 349, 356, 360, 366, 367, 376, 381, 395,
406, 411, 413, 432, 442, 456, 477, 484, 491, 495,
508, 516, 517, 529, 534, 538, 552, 561, 567, 576,
603, 604, 605, 632, 646, 648, 670, 691, 705, 706,
721, 725, 735, 738, 756, 772, 774, 795, 805, 810,
811, 825, 829, 864, 874, 876, 891, 897, 906, 916,
923, 924, 925, 940, 946, 954, 964, 965, 967, 969]

# n is finding the length of the array
n = len(list)
 
# Element to be searched for
x = 795

# this is a var that is calling the made function which is calling the array and setting the hight and low values wich is 0 for low and n-1 for hight 
# because arrays start at 0 and calling the x because thats the value being found
index = interpolationSearch(list, 0, n - 1, x)
 

if index != -1:
    #if the number being searched for is not found in the array print element not found
    print("Element found at index", index)
else:
    #if the element is found in the array print element found
    print("Element not found")