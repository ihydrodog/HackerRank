import math
import os
import random
import re
import sys

def updateFreqListDic( dic, prevFreq, curFreq ):
    if prevFreq != 0:
        dic[prevFreq] -= 1

    if curFreq != 0:
        c = dic.get( curFreq, 0 )
        dic[curFreq] = c+1



# Complete the freqQuery function below.
def freqQuery(queries):

    result = []
    freq = {}
    reversedFreq = {}

    for q in queries:

        operation = q[0]
        target = q[1]
        if operation == 1:
            count = freq.get( target, 0)+1
            freq[target] = count
            updateFreqListDic( reversedFreq, count-1, count )
        elif operation == 2:
            count = freq.get( target, 0)-1
            if count >= 0:
                freq[target] = count
            updateFreqListDic(reversedFreq, count + 1, count)

        else: # operation == 3:
            result.append( 1 if reversedFreq.get( target, 0 ) > 0 else 0 )

    return result


print( freqQuery( [ (1, 1), (2, 2), (3, 2), (1, 1), (1,1), (2,1), (3,2) ] ))