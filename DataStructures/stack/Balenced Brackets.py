#!/bin/python3

import math
import os
import random
import re
import sys


def isBalanced(s):
    stack = []
    d = { '[' : ']', '{' : '}', '(':')'}
    for i in s:
        #If stack is empty then append
        if not stack:
            stack.append(i)
        elif i == d.get(stack[-1]) :  # if i matches the key-value from the dictionary for the first elemnt in stack then it must be the matching bracket then pop the first elemnt 
            stack.pop()
        else :
            stack.append(i) #else we are still in opening brackets so append the element
    if not stack: 
        return "YES"
    else : return "NO" 
        
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
