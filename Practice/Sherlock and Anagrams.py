#!/bin/python3

import math
import os
import random
import re
import sys




# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    lenOfS = len(s)
    count = 0
    for length in range(1, lenOfS ):
        for startPos in range(lenOfS - length):
            substring = s[startPos:startPos + length]
            sortedAnagram = tuple(sorted(substring))


            for startPos2 in range( startPos+1, lenOfS-length+1 ):
                if tuple(sorted( s[startPos2:startPos2+length])) == sortedAnagram:
                    count+=1
    return count



print( sherlockAndAnagrams( 'cdcd'))