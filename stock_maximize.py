#!/bin/python
# https://www.hackerrank.com/challenges/stockmax/problem

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    if not prices:
        return 0
    current_max = prices[-1]
    profits = 0
    for price in prices[::-1]:
        current_max = max(current_max, price)
        profits += (current_max - price)
    return profits

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        n = int(raw_input().strip())

        prices = map(int, raw_input().rstrip().split())

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
