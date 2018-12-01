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

        adjacentNodeMap.setdefault( _from, [] ).append( _to )
        adjacentNodeMap.setdefault( _to, [] ).append( _from )


    minDistance = None
    # traverse
    for index, color in enumerate( ids ):
        if color == val:
            startNode = index+1

            visited = set( (startNode,) )

            toBeVisited = list( (adjacent, 1) for adjacent in adjacentNodeMap[ startNode ] )
            while toBeVisited:
                curNode, distance = toBeVisited.pop(0)
                visited.add( curNode )

                if ids[curNode-1] == val:
                    if minDistance is None or minDistance > distance:
                        # for the min value
                        if distance == 1:
                            return distance

                        minDistance = distance

                if minDistance is None or distance < minDistance-1: # dont need to traverse further
                    for adjacent in adjacentNodeMap[curNode]:
                        if adjacent not in visited:
                            toBeVisited.append( (adjacent, distance + 1) )


    return minDistance if minDistance is not None else -1



print( findShortest( 5, (1, 1, 2, 3,), (2, 3, 4, 5), (1, 2, 3, 3, 2), 2))

