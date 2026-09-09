# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true
# Problem     Modified Kaprekar Numbers
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-09, 09:32 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    results = []
    
    for n in range(p, q + 1):
        # Get the number of digits of the original number n
        d = len(str(n))
        
        # Calculate the square of n
        sq = n * n
        sq_str = str(sq)
        
        # Split into right (last d digits) and left (the rest)
        r_str = sq_str[-d:]
        l_str = sq_str[:-d]
        
        # Convert substrings to integers (handle empty left substring as 0)
        r = int(r_str) if r_str else 0
        l = int(l_str) if l_str else 0
        
        # Check if the sum of parts equals the original number
        if l + r == n:
            results.append(n)
            
    # Print the output according to the format requirements
    if results:
        print(*(results))
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
