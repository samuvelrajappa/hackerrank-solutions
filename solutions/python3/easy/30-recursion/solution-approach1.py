# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-recursion/problem?isFullScreen=true
# Problem     Day 9: Recursion 3  
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:25 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
