#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

'''
#This takes too much time 
def getMax(operations):
    stack = []
    final = []
    for i in operations:
        if i[0] == '1':
            x,y = i.split(' ')
            stack.append(int(y))
        elif i[0] == '2':
            stack.pop()
        elif i[0] == '3':
            final.append(max(stack))
    return final
    
 '''        
'''

We do not need to maintain two stacks. 
Instead, we can use a single stack of integers: For query (1), instead of pushing element X, we simply push max(x, stack.peek()). 
    For query (2), simply pop an element. For query (3), print stack.peek().
In a nutshell, we don't care that X is at the top of the stack if there is an element Y > X further down in the stack, so why not just push Y?
            '''

def getMax(operations):
    items = [0]
    final = []
    for i in operations:
        x= list(map(int,i.split(" ")))
        if x[0] == 1 : items.append(max(x[1],items[-1]))
        elif x[0] == 2 : items.pop()
        else: final.append(items[-1])
    return final
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
