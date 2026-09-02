# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
# Problem     Time Conversion
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 12:03 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    period = s[-2:]
    hour = int(s[:2])
    time_remainder = s[2:8]
    
    # Apply conversion logic based on AM/PM
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
            
    # Format hour to always be 2 digits and combine with minutes/seconds
    return f"{hour:02d}{time_remainder}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
