# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true
# Problem     Append and Delete
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
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    common_length = 0
    for char_s, char_t in zip(s, t):
        if char_s == char_t:
            common_length += 1
        else:
            break
            
    # Calculate the minimum operations required
    min_ops = (len(s) - common_length) + (len(t) - common_length)
    
    # Case 1: Enough operations to delete the whole string and rebuild it from scratch
    if k >= len(s) + len(t):
        return "Yes"
    
    # Case 2: Operations match or exceed the minimum requirement with an even difference
    elif k >= min_ops and (k - min_ops) % 2 == 0:
        return "Yes"
        
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
