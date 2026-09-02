# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
# Problem     Diagonal Difference
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:58 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    primary_sum = 0
    secondary_sum = 0
    n = len(arr)
    
    for i in range(n):
        primary_sum += arr[i][i]          # Elements like (0,0), (1,1), (2,2)
        secondary_sum += arr[i][n - 1 - i] # Elements like (0,2), (1,1), (2,0)
        
    return abs(primary_sum - secondary_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
