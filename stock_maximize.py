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
    maximas = []
    n = len(prices)
    for i in xrange(n-1, -1, -1):
        if not maximas:
            maximas.append(i)
            continue
        if prices[i] > prices[maximas[-1]]:
            maximas.append(i)
    profits = 0
    prev_maxima = 0
    while maximas:
        maxima = maximas.pop()
        for i in xrange(prev_maxima, maxima):
            profits += (prices[maxima] - prices[i])
        prev_maxima = maxima + 1
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
