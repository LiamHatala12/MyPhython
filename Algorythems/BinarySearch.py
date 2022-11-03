'''
Name: Liam H
Program: Binary Search
Date: Saturday. April 2
'''

def binarySearch(sortedlist, searchkey):
    #we are begining at the start of the list
    starti = 0
    #we are ending with the last index and we minusing 1 because the first index is always 0
    endi = len(sortedlist) - 1

    #so as long as starti is smaller than endi we will contiue to midpoint
    while starti <= endi:
        #are midpoint is the middle position between are begining index and the rest of then items in the sortedlist
        #(endi -starti) = rest of items needing to be searched and // is devision without remander 
        listmidpoint = starti + (endi - starti) // 2
        #this is compairing the value of the midpoint to the value being seached for
        listmidpointvalue = sortedlist[listmidpoint]
        #checking if the midpoint is == to the value we looking for
        if listmidpointvalue == searchkey:
            return listmidpoint

        #the item would be to left of the midpoint value if this was in the list
        elif searchkey < listmidpointvalue:
            #the ending position would be the element directly left of the mid point
            endi = listmidpoint - 1

        
        else:
            # we only need to check if the item is to the right of the midpoint by changing the beging index
            starti = listmidpoint + 1 
    #if the item is not found in the index then we need to return none, this happens when the while loop breaks
    return None

MyList = [9, 56, 69, 73, 82, 92, 133, 145, 146, 150,
163, 180, 181, 190, 192, 199, 201, 218, 225, 242,
245, 251, 265, 271, 274, 282, 299, 307, 313, 322,
324, 340, 349, 356, 360, 366, 367, 376, 381, 395,
406, 411, 413, 432, 442, 456, 477, 484, 491, 495,
508, 516, 517, 529, 534, 538, 552, 561, 567, 576,
603, 604, 605, 632, 646, 648, 670, 691, 705, 706,
721, 725, 735, 738, 756, 772, 774, 795, 805, 810,
811, 825, 829, 864, 874, 876, 891, 897, 906, 916,
923, 924, 925, 940, 946, 954, 964, 965, 967, 969
]
searchkeyanswer = 795

searchkeyanswer2 = 120

#printing the function with the list being searched and giving them the number im looking for
print(binarySearch(MyList, searchkeyanswer))

#if we search for a number not in list we will get none
print(binarySearch(MyList, searchkeyanswer2))

