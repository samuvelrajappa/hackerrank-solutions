# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true
# Problem     Sherlock and Squares
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 01:02 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    # Find the smallest integer whose square is >= a
    lower_bound = math.ceil(math.sqrt(a))
    
    # Find the largest integer whose square is <= b
    upper_bound = math.floor(math.sqrt(b))
    
    # If the range is valid, return the count of integers between bounds
    if lower_bound <= upper_bound:
        return upper_bound - lower_bound + 1
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
