# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true
# Problem     Cut the sticks
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
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    result = []
    while arr:
        # Record the number of sticks before the current cut operation
        result.append(len(arr))
        # Find the shortest stick length in the current iteration
        min_val = min(arr)
        # Cut the minimum length from all sticks and discard zero-length pieces
        arr = [x - min_val for x in arr if x - min_val > 0]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
