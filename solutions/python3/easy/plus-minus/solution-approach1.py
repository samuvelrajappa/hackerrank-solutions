# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
# Problem     Plus Minus
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 12:01 p.m.
# ──────────────────────────────────────────────────

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
    
    # Initialize counters for positive, negative, and zero values
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    # Count occurrences of each type
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
            
    # Print fractions formatted to exactly 6 decimal places
    print(f"{positive_count / n:.6f}")
    print(f"{negative_count / n:.6f}")
    print(f"{zero_count / n:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
