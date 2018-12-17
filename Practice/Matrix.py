#!/bin/python3

import math
import os
import random
import re
import sys


def findPath( edges, a, b):

    queue = [(a, [a])]
    visited = set()

    while queue:
        cur, path = queue.pop(0)

        visited.add( cur )

        for adjacent in (edges[cur]-visited):
            newPath = list(path)
            newPath.append( adjacent )
            if adjacent == b:
                return newPath
            else:
                queue.append( (adjacent, newPath) )

    return None




# Complete the minTime function below.
def minTime(roads, machines):
    edges = {}

    cost = {}
    for r in roads:
        a, b = r[0], r[1]
        edges.setdefault( a, set() ).add( b )
        edges.setdefault( b, set() ).add( a )

        cost[ ( a, b ) if a<b else (b, a) ] = r[2]

    costSum = 0
    # find paths
    path = {}
    machineCount = len( machines )
    for a in range( machineCount ):
        for b in range( a ):
            p = findPath( edges, machines[a], machines[b] )
            if p:
                cheapestNode = None
                cheapestCost = None
                for index in range( len( p )-1):
                    n0 = p[index]
                    n1 = p[index+1]
                    edgeCost = cost[ ( n0, n1 ) if n0<n1 else (n1, n0) ]
                    if cheapestCost is None or cheapestCost > edgeCost:
                        cheapestCost = edgeCost
                        cheapestNode = ( n0, n1)

                # cut the cheapest
                n0, n1 = cheapestNode
                edges[ n0 ].remove( n1 )
                edges[ n1 ].remove( n0 )
                costSum += cheapestCost




    return costSum

print( minTime( ( (0, 3, 3), (1, 4, 4), (1, 3, 4), (0, 2, 5) ), (1, 3, 4) ))

print( minTime( ((2, 1, 8), (1, 0, 5), (2, 4, 5), (1, 3, 4)), (2, 4, 0) ))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    with open( 'Input/matrix.dat' , 'rt') as inputFile:

        nk = inputFile.readline().split()

        n = int(nk[0])

        k = int(nk[1])

        roads = []

        for _ in range(n - 1):
            roads.append(list(map(int, inputFile.readline().rstrip().split())))

        machines = []

        for _ in range(k):
            machines_item = int(inputFile.readline())
            machines.append(machines_item)

        result = minTime(roads, machines)

        print( result )

    # fptr.write(str(result) + '\n')

    # fptr.close()



