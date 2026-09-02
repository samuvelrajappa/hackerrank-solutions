# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true
# Problem     Repeated String
# Difficulty  Easy
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
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    # Count 'a' in the single original string
    count_in_s = s.count('a')
    
    # Calculate full repetitions and the remaining characters
    full_repeats = n // len(s)
    remainder_len = n % len(s)
    
    # Count 'a' in the partial remaining string
    count_in_remainder = s[:remainder_len].count('a')
    
    # Return the total frequency
    return (full_repeats * count_in_s) + count_in_remainder
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
