#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    sum,i,j = 0,0,0
    while i<n and (sum + a[i]) <= maxSum :   #first we find the count only in stack a
        sum += a[i]
        i += 1 
    count = i
    while j<len(b) and i >= 0 : #Here we add one elemnt of stack b to sum 
        sum += b[j]
        j += 1
        while (sum > maxSum and i>0): #If the sum exceeds maxsum then we pop a elemnt from stack a and subtract from sum. The logic here is that no. of elements added from stack b should be > no. of elemnts popped from stack a 
            i -= 1
            sum -= a[i]
            
        while (sum <= maxSum and i+j >count):
            count = i+j
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
