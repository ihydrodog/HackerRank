#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY names as parameter.
#

def _solve_wrong(names):
    abbrMap = {}
    occupiedNames = set()
    for name in names:
        for i in range( 0, len( name ) ):
            _abbr = name[:i+1]
            duplicatedCount = abbrMap.get( _abbr, 0 )
            if duplicatedCount is 0:
                # check starts with
                if not _abbr in occupiedNames:
                    abbrMap[ _abbr ] = 1
                    # fill nameMap for all length
                    for j in range( len( name ) ):
                        occupiedNames.add( name[:j+1] )
                    break
        else:
            abbrMap[ '{} {}'.format( name, duplicatedCount )] = 1

    return abbrMap.keys()

import collections

def solve(names):
    res = []
    occupiedNames = dict()
    nameCount = {}
    for name in names:
        for i in range( 0, len( name ) ):
            _abbr = name[:i+1]
            duplicatedCount = occupiedNames.get( _abbr, None )
            if duplicatedCount is None:
                # check starts with
                if not _abbr in occupiedNames:

                    occupiedNames[ _abbr ] = 1
                    res.append( _abbr )
                    # pre-occupy for longer
                    for j in range( i+1, len( name ) ):
                        occupiedNames[ name[:j+1] ] = 0

                    nameCount[name] = 1
                    break
        else:
            nameCount[name] = nameCount.get( name, 0)+1
            if nameCount[name] == 1:
                res.append( _abbr )
            else:
                res.append( '{} {}'.format( name, nameCount[name] ) )


    return res


# ret = solve( ('alvin', 'alice', 'alvin'))
# print( ret )


if __name__ == '__main__':

    inputFile = open( 'input/testcase2.txt', 'rt')

    line = inputFile.readline()
    n = int(line.strip())

    names = []

    for _ in range(n):
        line = inputFile.readline()
        names_item = line.strip()
        names.append(names_item)

    res = solve(names)

    print( res )
