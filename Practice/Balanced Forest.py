#!/bin/python3

import math
import os
import random
import re
import sys



class Node:
    visitOrder = 0

    def __init__(self, d):
        self.link = []
        self.sum = 0
        self.data = d
        self.visitOrderStart  = None
        self.visitOrderEnd = None


    def addLink(self, n):
        self.link.append( n )
        n.link.append( self )


    def traverse(self, freq, parent : 'Node' = None):
        self.sum += self.data
        __class__.visitOrder += 1

        self.visitOrderStart = __class__.visitOrder


        for c in self.link:
            if c != parent:
                self.sum += c.traverse( freq, self )

        self.visitOrderEnd = __class__.visitOrder
        freq.setdefault( self.sum, [] ).append( self )

        return self.sum


    def isSubtreeOf(self, tree: 'Node'):
        return tree.visitOrderStart <= self.visitOrderStart <= tree.visitOrderEnd


def balancedForest(c, edges):
    # build
    nodes = []
    for _c in c:
        nodes.append( Node( _c ) )

    for e0, e1 in edges:
        nodes[e0-1].addLink( nodes[e1-1] )

    freq = {}
    root = nodes[0]
    sum = root.traverse( freq, root )

    minValue = math.inf
    minAdd = minValue

    if sum%2 == 0 and freq.get( sum/2, None):
        minAdd = int( sum/2 )

    for node in nodes:
        if node.sum <= sum/3:
            if ( sum - node.sum )%2 == 0:
                searching = int( (sum-node.sum)/2 )
                for c in freq.get( searching, [] ):
                    if c != node and not node.isSubtreeOf( c ):
                        minAdd = min( minAdd, searching-node.sum )
                        break
                else:
                    for c in freq.get( node.sum + searching, [] ):
                        if c != node and node.isSubtreeOf( c ):
                            minAdd = min( minAdd, searching-node.sum )
                            break

        elif node.sum*2 < sum:
            add = node.sum*3-sum
            for c in freq.get( node.sum, []):
                if c != node:
                    minAdd = min(minAdd, add )
                    break
            else:
                for c in freq.get(node.sum - add, []):
                    if c != node and not c.isSubtreeOf( node ):
                        minAdd = min(minAdd, add )
                        break
                else:
                    for c in freq.get(node.sum*2 - add, []):
                        if c != node and node.isSubtreeOf( c ):
                            minAdd = min(minAdd, add )
                            break
                    else:
                        for c in freq.get(node.sum*2, []):
                            if c != node and node.isSubtreeOf( c ):
                                minAdd = min(minAdd, add )
                                break

    return minAdd if minAdd < minValue else -1

print( balancedForest( [ 2, 3, 3, 4], [(1,2), (2,3), (1, 4)]) )

print( balancedForest( [ 100, 100, 99, 99, 98, 98 ], [(1,3), (3, 5), (1, 2), (2, 4), (4, 6)]) )
#
print( balancedForest( [ 1, 2, 2, 1, 1], [(1,2), (1,3), (3, 5), (1, 4)]) )

print( balancedForest( [ 15, 12, 8, 14, 13], [(1,2), (1,3), (1, 4), (4, 5) ] ) )

print( balancedForest( [ 7, 7, 4, 1, 1, 1 ], [(1, 2), (3, 1), (2, 4), (2, 5), (2, 6) ] ) )


if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
