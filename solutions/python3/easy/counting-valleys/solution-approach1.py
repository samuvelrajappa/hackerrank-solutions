# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
# Problem     Counting Valleys
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 12:09 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    valleys = 0
    
    for step in path:
        if step == 'U':
            altitude += 1
            # If we reach sea level from below, it's a valley
            if altitude == 0:
                valleys += 1
        else:
            altitude -= 1
            
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
