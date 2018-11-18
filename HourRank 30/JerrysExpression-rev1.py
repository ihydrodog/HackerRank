import math

def solve(expression):
    elementsStack = []
    operators = ('-',    '+')
    index = 0
    while index < len(expression):
        if index < len(expression):
            ch = expression[index]
            index+=1
            if ch in operators:
                elementsStack.append( ch )
            else:
                elementsStack.append( ch )

        while len( elementsStack ) >= 2 and \
            elementsStack[-1] not in operators and elementsStack[-2] not in operators:
            right, left = elementsStack.pop(), elementsStack.pop()
            elementsStack.append( ( left, elementsStack.pop(), right ) )


    curSign = 1
    queue = [ (elementsStack.pop( ), curSign ) ]
    positiveCount, negativeCount = 0, 0

    index = 0
    while index < len(queue):
        e, curSign = queue.pop( index )

        if isinstance( e, tuple ):
            added = 0
            for i in e:
                if i == '-':
                    curSign = -curSign
                elif i == '+':
                    pass
                else:
                    queue.insert( index+added, (i, curSign) )
                    added+=1
        else:
            if e in operators:
                pass
            else:
                queue.insert( index, (e, curSign) )
                if curSign > 0:
                    positiveCount += 1
                else:
                    negativeCount += 1
            index += 1


    sumIfQuestionMarkIsOne = positiveCount-negativeCount

    debtForPositiveOperand, debtForNegativeOperand = 0, 0
    if sumIfQuestionMarkIsOne > 0:
        debt = sumIfQuestionMarkIsOne
        debtForNegativeOperand = math.ceil( debt/negativeCount )
    elif sumIfQuestionMarkIsOne < 0:
        debt = -sumIfQuestionMarkIsOne
        debtForPositiveOperand = math.ceil( debt/positiveCount )

    values = []
    for (_,sign) in queue:
        if sign > 0:
            if debtForPositiveOperand > 0:
                v = min(debtForPositiveOperand, debt)
                debt -= v
                values.append(1 + v)
            else:
                values.append(1)
        else:
            if debtForNegativeOperand > 0:
                v = min(debtForNegativeOperand, debt)
                debt -= v
                values.append(1 + v)
            else:
                values.append(1)

    return values


def solve( expression ):
    ki = 0
    stack = []
    posi = []
    nega = []
    sign = 1
    for char in expression:
        if char == '+':
            stack.append( ( 1, sign ) )
        elif char == '-':
            stack.append( ( 3, sign ) )
        elif char == '?':
            if sign > 0:
                posi.append( ki )
            else:
                nega.append( ki )
            ki += 1

            while stack:
                last, sign = stack.pop()
                if last == 1 or last == 3:
                    sign = sign if last == 1 else -sign
                    stack.append( ( last + 1, sign ) )
                    break

    posiSize = len( posi )
    negaSize = len( nega )
    result = [ 1, ] * ki
    diff = posiSize - negaSize
    if diff > 0:
        remainder = diff % negaSize
        quotient = diff // negaSize
        for i in range( negaSize ):
            index = nega[ i ]
            if i < remainder:
                result[ index ] += quotient + 1
            else:
                result[ index ] += quotient
    else:
        remainder = -diff % posiSize
        quotient = -diff // posiSize
        for i in range( posiSize ):
            index = posi[ i ]
            if i < remainder:
                result[ index ] += quotient + 1
            else:
                result[ index ] += quotient

    return result

print( solve( '+--???+??'))

print( solve( '-----???+?+???+?+??'))