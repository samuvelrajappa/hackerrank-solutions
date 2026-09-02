# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true
# Problem     Extra Long Factorials
# Difficulty  Medium
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
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    print(math.factorial(n))
    
if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
