# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
# Problem     Day of the Programmer
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 12:07 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year <= 1917:
        if year % 4 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
            
    # Case 2: Transition year (1918)
    elif year == 1918:
        return "26.09.1918"
        
    # Case 3: Gregorian calendar period (1919 onwards)
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
