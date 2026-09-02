# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
# Problem     Bill Division
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
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    total_anna_ate = sum(bill) - bill[k]
    
    # Calculate Anna's actual fair share (split equally by 2)
    fair_share = total_anna_ate // 2
    
    # Check if Brian charged her correctly
    if b == fair_share:
        print("Bon Appetit")
    else:
        # Print the overcharged refund amount
        print(b - fair_share)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
