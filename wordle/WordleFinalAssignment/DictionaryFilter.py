'''
Program: Dictionary sorter
Name: Liam
Date: 03/04/2022
'''

import os
import sys

with open (os.path.join(sys.path[0],"dictionary.txt"), 'r') as f:
    words = f.read().splitlines()
    print(words)

with open(os.path.join(sys.path[0],"fiveletterdict.txt",),'w') as u:
    for word in words:
        if len(word) == 5 and word.isalpha() and word.islower():
            u.write(word+'\n')