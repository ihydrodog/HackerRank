#!/bin/python3

import math
import os
import random
import re
import sys

import collections
import itertools


# Complete the countTriplets function below.
def countTriplets(arr, r):
    freq = {}
    for index, item in enumerate( arr ):
        freq.setdefault( item, [] ).append( index )

    count = 0
    for firstElement in freq.keys():
        if r != 1:
            g = ( freq[firstElement], freq.get(firstElement * r, None), freq.get(firstElement * r * r, None) )
            if all( g ):
                i1ForMin = 0
                i2ForMin = 0
                for i0, arrIndex0 in enumerate( g[0] ):

                    for i1 in range(i1ForMin, len(g[1])):
                        arrIndex1 = g[1][i1]
                        if arrIndex0 < arrIndex1:
                            i1ForMin = i1
                            break

                    # find greater index in g[2]
                    for i2 in range(i2ForMin, len(g[2])):
                        arrIndex2 = g[2][i2]
                        if arrIndex2 > arrIndex0:
                            i2ForMin = i2
                            break


                    # find greater index in g[2]
                    for i2 in range(i2ForMin, len(g[2])):
                        arrIndex2 = g[2][i2]

                        # get count between arrIndex0, arrIndex2 in g[1]
                        # countInG1 = len( tuple( _g1 for _g1 in g[1] if arrIndex0 < _g1 < arrIndex2 ) )
                        countInG1 = 0
                        for i1 in range( i1ForMin, len(g[1])):
                            arrIndex1 = g[1][i1]
                            if arrIndex1 >= arrIndex2:
                                count += (len(g[2]) - i2) * (i1 - i1ForMin)
                                break











            # count += freq.get(firstElement, 0) * freq.get(firstElement * r, 0) * freq.get(firstElement * r * r, 0)
        else:
            f = len( freq[firstElement] )
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