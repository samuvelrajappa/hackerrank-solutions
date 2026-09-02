# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
# Problem     Birthday Cake Candles
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 12:01 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    return candles.count(max(candles))   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
