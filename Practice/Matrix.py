#!/bin/python3

import math
import os
import random
import re
import sys

def dfs( edges, machines, costTable, root, parent ):
    cost = 0
    for node, c in edges[root]:
        if node != parent:
            dfs( edges, machines, costTable, node, root )
            cost += min( costTable[node][1] + c, costTable[node][0] )

    if root in machines:
        f1 = cost
        f0 = math.inf
    else:
        f0 = cost
        f1 = math.inf
        for node, c in edges[root]:
            if node != parent:
                f1 = min( f1, cost+costTable[node][1]-min( costTable[node][1]+c, costTable[node][0] ) )

    costTable[root] = (f0, f1 )


# Complete the minTime function below.
def minTime(roads, machines):

    edges = {}
    for (f,t, c) in roads:
        edges.setdefault( f, list() ).append( (t, c) )
        edges.setdefault( t, list() ).append( (f, c) )

    costTable = {}

    root = machines[-1]

    dfs( edges, machines, costTable, root, -1 )

    return min( *costTable[root])


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



