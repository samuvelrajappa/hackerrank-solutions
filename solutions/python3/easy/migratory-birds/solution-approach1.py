# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true
# Problem     Migratory Birds
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 12:06 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    count = [0] * 6
    
    # Count occurrences of each bird ID
    for bird in arr:
        count[bird] += 1
        
    max_count = 0
    best_bird = 1
    
    # Find the most frequent bird with the lowest ID
    for i in range(1, 6):
        if count[i] > max_count:
            max_count = count[i]
            best_bird = i
            
    return best_bird

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
