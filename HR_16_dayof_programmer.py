#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    y = year
    if y < 1918:
        if y%4 == 0:
            print("sep 12 ")
            return ("12.09."+str(y))
        else:
            return ("13.09."+str(y))
    elif y>1918:
        if (y%400 == 0  )or( y%4 == 0  and y%100 != 0):
            return ("12.09."+str(y))
        else:
            return ("13.09."+str(y))
            
    else:
        return ("26.09.1918")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
    
