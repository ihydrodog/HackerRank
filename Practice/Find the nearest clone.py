#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):

    # build map
    adjacentNodeMap = {}
    for i in range( len( graph_from) ):
        _from = graph_from[i]
        _to = graph_to[i]

        adjacentNodeMap.get( _from, [] ).append( _to )
        adjacentNodeMap.get( _to, [] ).append( _from )

    # traverse

    startNode = adjacentNodeMap.keys()[0]

    visited = set()

    toBeVisited = list()
    toBeVisited.add( startNode )
    distance = -1
    minDistance = -1
    while toBeVisited:
        curNode = toBeVisited.pop(0)
        visited.add( curNode )

        if ids[curNode] == val:
            if distance < 0:
                # init
                distance = 0
            else:
                if minDistance > distance:
                    minDistance = distance

                distance = 0 # reset to continue searching
        else:
            if distance >= 0:
                distance += 1   # or weight

        for adjacent in adjacentNodeMap[curNode]:
            if adjacent not in visited:
                toBeVisited.add( adjacent )


    return minDistance




