# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
# Problem     Bigger is Greater
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-08, 12:23 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    # Convert string to list since strings are immutable in Python
    arr = list(w)
    n = len(arr)
    
    # Step 1: Find the rightmost character that is smaller than its next character
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
        
    # If no such character is found, it is the highest possible permutation
    if i < 0:
        return "no answer"
        
    # Step 2: Find the rightmost character that is greater than arr[i]
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
        
    # Step 3: Swap the pivot and the successor
    arr[i], arr[j] = arr[j], arr[i]
    
    # Step 4: Reverse the suffix after index i
    arr[i + 1:] = reversed(arr[i + 1:])
    
    return "".join(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
