# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true
# Problem     Sequence Equation
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 01:01 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    location = {val: i + 1 for i, val in enumerate(p)}
    
    result = []
    # Iterate through all x from 1 to n
    for x in range(1, len(p) + 1):
        # Find where x is located
        pos1 = location[x]
        # Find where that position itself is located
        y = location[pos1]
        result.append(y)
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
