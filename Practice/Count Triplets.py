#!/bin/python3

import math
import os
import random
import re
import sys

import collections


# Complete the countTriplets function below.
def countTriplets(arr, r):
    freq = collections.Counter(arr)
    count = 0
    for firstElement in freq.keys():
        if r != 1:
            count += freq.get(firstElement, 0) * freq.get(firstElement * r, 0) * freq.get(firstElement * r * r, 0)
        else:
            f = freq[firstElement]
            if f >= 3:
                count += int( f * (f - 1) * (f - 2) / 6 )

    return count



if __name__ == '__main__':

    with open( 'Input/Count Triplets.dat', 'rt') as inputFile:

        inputData = inputFile.readline()

        nr = inputData.rstrip().split()

        n = int(nr[0])

        r = int(nr[1])

        arr = list(map(int, inputFile.read().rstrip().split()))

        ans = countTriplets(arr, r)

        print( ans )