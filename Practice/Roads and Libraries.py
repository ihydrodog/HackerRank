#!/bin/python3

import math
import os
import random
import re
import sys

def findContainingGraph( graphs, vertex ):

    for g in graphs:
        if vertex in g:
            return g

    return None

def getGraphGroups( n, edges ):

    graphs = [ { c } for c in range(1, n+1) ]

    for e in edges:
        ( g0, g1 ) = tuple( findContainingGraph( graphs, v ) for v in e )

        if g0 != g1:
            g0 |= g1
            graphs.remove( g1 )

    return graphs


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    graphs = getGraphGroups( n, cities )
    if c_lib <= c_road:
        return n * c_lib
    else:
        cost = len( graphs )*c_lib
        for g in graphs:
            cost += (len( g )-1)*c_road

        return cost


print( roadsAndLibraries( 6, 10, 2, ((1,3),(3,4),(2,4),(1,2),(2,3),(5,6) ) ) )