#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def findAnagram(a, s):
    pass


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    lenOfS = len(s)
    for length in range(1, lenOfS - 1):
        for startPos in range(lenOfS - length):
            substring = s[startPos:startPos + length]

            findAnagram(substring, s[startPos + 1:])