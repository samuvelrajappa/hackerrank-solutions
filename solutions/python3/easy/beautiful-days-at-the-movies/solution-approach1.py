# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true
# Problem     Beautiful Days at the Movies
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 01:00 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    beautiful_count = 0
    
    # Iterate through each day in the given inclusive range
    for day in range(i, j + 1):
        # Reverse the integer by converting it to a string and slicing
        reversed_day = int(str(day)[::-1])
        
        # Check if the absolute difference is evenly divisible by k
        if abs(day - reversed_day) % k == 0:
            beautiful_count += 1
            
    return beautiful_count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
