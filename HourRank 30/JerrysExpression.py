#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING expression as parameter.
#

def _getOperand( queue, res, shouldBe = None ):
    v = queue[0]
    if v == '?':
        value = 1 if shouldBe is None else shouldBe
        res.append( value )
        queue.pop(0)
        return value
    else:
        return _calculate( queue, res, shouldBe )

def _calculate( queue, res, shouldBe ):
    op = queue.pop(0)


    l = _getOperand( queue, res )
    r = _getOperand( queue, res, l if op =='-' else -l )
    return __calc( op, l, r )

def __calc( op, l, r):
    if op == '+':
        return l+r
    elif op == '-':
        return l-r

def solve(expression):
    queue = list( expression )

    res = []
    _calculate( queue, res, 0 )

    return res


print( solve( '-?-??'))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    expression = input()

    res = solve(expression)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
