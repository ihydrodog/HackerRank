#!/bin/python3

import math
import os
import random
import re
import sys

def getGraphGroups( n, edges ):

    nodeMap = {}
    graphCount = 0

    for e in edges:

        g0 = nodeMap.get( e[0], None )
        g1 = nodeMap.get( e[1], None )

        if g0 is None and g1 is None:
            newSet = { e[0], e[1] }
            nodeMap[e[0]] = nodeMap[e[1]] = newSet
            graphCount += 1
        elif g0 is not None and g1 is not None:
            # merge
            if g0 != g1:
                g0 |= g1
                graphCount -= 1
                for node in g1:
                    nodeMap[node] = g0
        else:
            g = g0 if g0 else g1
            g.add( e[0] )
            g.add( e[1] )
            nodeMap[ e[0] ] = g
            nodeMap[ e[1] ] = g

    return nodeMap, graphCount


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):

    if c_lib <= c_road:
        return n * c_lib
    else:
        nodeMap, graphCount = getGraphGroups( n, cities )

        libCount = graphCount
        for n in range( 1, n+1):
            if n not in nodeMap:
                libCount+=1

        cost = libCount*c_lib
        cost += (n-libCount)*c_road

        return cost

print( roadsAndLibraries( 3, 2, 1, ((1,2),(3,1),(2,3) ) ) )
print( roadsAndLibraries( 6, 2, 5, ((1,3),(3,4),(2,4),(1,2),(2,3),(5,6) ) ) )