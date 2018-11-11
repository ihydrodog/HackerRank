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


def calculate( expression, debt = None, debtForPositiveOperand = None, debtForNegativeOperand = None ):
    operators = ['-','+']

    index = 0
    stack = [ ( expression[index], index) ]
    index+=1

    res = [None]*len(expression)

    curSign = 1 # 1 means positive sign

    positiveCount, negativeCount = 0, 0

    signQueue = [curSign]

    while len(stack) > 1 or index < len(expression):
        info = stack[-1]
        c = info[0]

        if c in operators:
            if c == '-':
                curSign = -curSign
            signQueue.append( curSign )

            # need left operand
            stack.append( [expression[index], index] )
            index += 1
        else:
            if stack[-2][0] not in operators:
                right, left = stack.pop(), stack.pop()
                leftIndex = left[1]
                rightIndex = right[1]
                operator = stack.pop()[0]

                if right[0] == '?':
                    if curSign > 0:
                        positiveCount+=1
                    else:
                        negativeCount+=1

                    res[rightIndex] = curSign
                    right[0] = 1

                signQueue.pop()
                curSign = signQueue[-1]

                if left[0] == '?':
                    if curSign > 0:
                        positiveCount+=1
                    else:
                        negativeCount+=1

                    res[leftIndex] = curSign
                    left[0] = 1

                result = left[0] + right[0] if operator=='+' else left[0] - right[0]

                stack.append( (result, None) )
            else:
                # need right operand
                stack.append( [ expression[index], index] )
                index += 1

    return stack[0][0], (positiveCount, negativeCount), res

def solve(expression):
    traversed = list(expression)
    sumIfQuestionMarkIsOne, (positiveCount, negativeCount), signs = calculate( traversed, None )

    debtForPositiveOperand, debtForNegativeOperand = 0, 0
    if sumIfQuestionMarkIsOne > 0:
        debt = sumIfQuestionMarkIsOne
        debtForNegativeOperand = math.ceil( debt/negativeCount )
    elif sumIfQuestionMarkIsOne < 0:
        debt = -sumIfQuestionMarkIsOne
        debtForPositiveOperand = math.ceil( debt/positiveCount )

    result = []
    for sign in signs:
        if sign is not None:
            if sign > 0:
                if debtForPositiveOperand > 0:
                    v = min( debtForPositiveOperand, debt )
                    debt -= v
                    result.append( 1+v )
                else:
                    result.append( 1 )
            else:
                if debtForNegativeOperand > 0:
                    v = min( debtForNegativeOperand, debt )
                    debt -= v
                    result.append( 1+v )
                else:
                    result.append( 1 )

    return result

print( solve( '+--???--???'))

