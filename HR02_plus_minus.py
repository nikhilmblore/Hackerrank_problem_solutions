#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    plus = minus = zero = 0
    for each in arr:
        if each > 0:
            plus += 1
        elif each <0:
            minus += 1
        elif each == 0:
            zero += 1
        
    print(round(plus/n, 6))
    print(round(minus/n,6))
    print(round(zero/n,6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
