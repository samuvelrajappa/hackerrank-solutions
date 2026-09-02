# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
# Problem     Breaking the Records
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 12:05 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here\
    max_score = scores[0]
    min_score = scores[0]
    
    # Initialize the counters for record updates
    max_count = 0
    min_count = 0
    
    # Iterate through the scores starting from the second game
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1
            
    # Return an array containing the counts [most_points_broken, least_points_broken]
    return [max_count, min_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
