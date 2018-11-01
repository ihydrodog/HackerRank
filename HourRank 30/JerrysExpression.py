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

def _getOperand( queue ):
    v = queue[0]
    if v == '?':
        queue.pop(0)
        return v
    else:
        return _calculate( v )

def _calculate( queue ):
    op = queue.pop(0)
    l = _getOperand( queue )
    r = _getOperand( queue )
    return __cal( op, l, r )

def __cal( op, l, r):
    if op == '+':
        return l+r
    elif op == '-':
        return l-r

def solve(expression):
    queue = list( expression )

    ret = _calculate( queue )


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    expression = input()

    res = solve(expression)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
