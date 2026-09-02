# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true
# Problem     Non-Divisible Subset
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 01:03 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    remainder_counts = [0] * k
    for num in s:
        remainder_counts[num % k] += 1
        
    # For numbers evenly divisible by k (remainder 0), we can include at most 1 element
    count = min(remainder_counts[0], 1)
    
    # Pair up complementary remainders (i and k - i)
    for i in range(1, (k // 2) + 1):
        if i == k - i:
            # If k is even and i equals k/2, we can only pick at most 1 element
            count += min(remainder_counts[i], 1)
        else:
            # Otherwise, pick the larger group between the two complementary remainders
            count += max(remainder_counts[i], remainder_counts[k - i])
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
