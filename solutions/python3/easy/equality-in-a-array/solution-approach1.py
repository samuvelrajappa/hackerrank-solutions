# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true
# Problem     Equalize the Array
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
from collections import Counter


#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    # Count the frequency of each element
    counts = Counter(arr)
    
    # Find the maximum frequency among all elements
    max_frequency = max(counts.values())
    
    # Minimum deletions = total elements minus the most frequent element count
    return len(arr) - max_frequency

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
