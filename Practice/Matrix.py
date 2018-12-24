#!/bin/python3

import math
import os
import random
import re
import sys


def findPathAndCut( edges, costTable, machines, start ):
    queue = list( )
    queue.append( ( start, list( (start,) ) ) )
    visited = set()

    while queue:
        curNode, path = queue.pop( 0 )
        visited.add( curNode )

        if curNode in machines and curNode != start :

            # find the chepeast and cut
            cheapestNode = None
            cheapestCost = None
            for index in range(len(path) - 1):
                n0 = path[index]
                n1 = path[index + 1]
                edgeCost = costTable[(n0, n1) if n0 < n1 else (n1, n0)]
                if cheapestCost is None or cheapestCost > edgeCost:
                    cheapestCost = edgeCost
                    cheapestNode = (n0, n1)


            n0, n1 = cheapestNode
            edges[ n0 ].remove( n1 )
            edges[ n1 ].remove( n0 )

            return cheapestCost, ( start, curNode )
        else:
            for n in edges[curNode]-visited:
                newPath = list( path )
                newPath.append( n )
                queue.append( ( n, newPath ) )

    return None, (None, None)

# Complete the minTime function below.
def minTime(roads, machines):
    edges = {}

    costTable = {}
    for r in roads:
        a, b = r[0], r[1]
        edges.setdefault( a, set() ).add( b )
        edges.setdefault( b, set() ).add( a )

        costTable[ ( a, b ) if a<b else (b, a) ] = r[2]

    costSum = 0
    # find paths

    queue = list( (machines[0], ))
    while queue:
        start = queue.pop()
        cost, (n0, n1) = findPathAndCut( edges, costTable, machines, start )
        if cost is not None:
            queue.append( n0 )
            queue.append( n1 )
            costSum += cost


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



