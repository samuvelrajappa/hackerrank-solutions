# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true
# Problem     Electronics Shop
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 12:10 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    max_spent = -1
    
    # Iterate through all combinations of keyboards and drives
    for k in keyboards:
        for d in drives:
            total = k + d
            # Check if the combination is affordable and more expensive than the current max
            if total <= b and total > max_spent:
                max_spent = total
                
    return max_spent
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
