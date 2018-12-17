#!/bin/python3

import math
import os
import random
import re
import sys

import collections

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



    # find paths
    path = {}
    machineCount = len( machines )
    for a in range( machineCount ):
        for b in range( a ):
            p = findPath( edges, machines[a], machines[b] )
            assert( p )
            for index in range( len( p )-1):
                path.setdefault( p[index], set() ).add( p[index+1])
                path.setdefault(p[index+1], set() ).add(p[index])


    # sort
    sortedByCost = collections.OrderedDict( sorted( filter( lambda kv: kv[0][0] in path and kv[0][1] in path, cost.items()), key=lambda kv:kv[1] ) )
    # destroy
    costSum = 0
    for count in range( machineCount-1):
        # find the cheapest
        cheapest = sortedByCost.popitem( last=False )
        road = cheapest[0]
        costSum += cheapest[1]


        queue = list()
        queue.append( road )

        while queue:
            e = queue.pop( 0 )
            e0, e1 = e
            try:
                del sortedByCost[ (e0, e1) if e0 < e1 else (e1, e0)]
            except:
                pass
            path[e[0]].remove( e[1] )
            path[e[1]].remove( e[0] )

            for n in e:
                if len( path[n] ) == 1 and n not in machines:
                    queue.append( ( n, list(path[n])[0] ) )


    return costSum
#
# print( minTime( ( (0, 3, 3), (1, 4, 4), (1, 3, 4), (0, 2, 5) ), (1, 3, 4) ))
#
# print( minTime( ((2, 1, 8), (1, 0, 5), (2, 4, 5), (1, 3, 4)), (2, 4, 0) ))

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



