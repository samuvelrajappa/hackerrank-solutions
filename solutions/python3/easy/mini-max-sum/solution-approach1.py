# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
# Problem     Mini-Max Sum
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
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total = sum(arr)
    print(total - max(arr),total - min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
