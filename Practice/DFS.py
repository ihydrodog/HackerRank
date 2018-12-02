import math
import os
import random
import re
import sys

def getRegionSize( r, c, grid, visited, size ):
    n = len(grid)
    m = len(grid[0])
    for nr in range( r-1, r+2 ):
        for nc in range( c-1, c+2 ):
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] and (nr, nc) not in visited:
                    size += 1
                    visited.add( (nr, nc ))
                    if not (nr == r and nc == c):
                        size = getRegionSize( nr, nc, grid, visited, size)

    return size


# Complete the maxRegion function below.
def maxRegion(grid):

    maxRegionSize = 0

    n = len(grid)
    m = len(grid[0])

    visited = set()

    for r in range( n ):
        for c in range( m ):
            if grid[r][c] and ( r, c ) not in visited:
                size = getRegionSize( r, c, grid, visited, 0 )
                maxRegionSize = max( maxRegionSize, size )

    return maxRegionSize



print( maxRegion( ((0, 0, 1, 1), (0, 0,1, 0), (0, 1, 1, 0), (0, 1, 0, 0),(1, 1, 0, 0)) ) )