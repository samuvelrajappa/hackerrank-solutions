# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true
# Problem     Picking Numbers
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 01:00 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    counts = Counter(a)
    max_length = 0
    
    # Iterate through unique numbers present in the counter
    for num in counts:
        # Check the combination of current number and the next consecutive number
        max_length = max(max_length, counts[num] + counts[num + 1])
        
    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
