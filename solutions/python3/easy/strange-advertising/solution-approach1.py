# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true
# Problem     Viral Advertising
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
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    shared = 5
    cumulative_likes = 0
    
    for _ in range(n):
        liked = shared // 2
        cumulative_likes += liked
        shared = liked * 3
        
    return cumulative_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
