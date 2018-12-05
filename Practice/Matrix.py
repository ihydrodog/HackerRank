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
            newPath = list(path).append( adjacent )
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
            p = findPath( edges, a, b )
            for index in range( len( p )-1):
                path.setdefault( p[index], [] ).append( p[index+1])
                path.setdefault(p[index+1], []).append(p[index])


    # sort
    sortedByCost = sorted( cost.items(), key=lambda kv:kv[1] )
    # destroy
    cost = 0
    for count in range( machineCount-1):
        # find the cheapest
        cheapest = sortedByCost[0]
        road = cheapest[0]
        cost += cheapest[1]

        # remove unnecessary roads
        for

