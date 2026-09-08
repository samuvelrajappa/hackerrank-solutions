# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
# Problem     Encryption
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-08, 12:21 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    # Remove all spaces from the text
    s = s.replace(" ", "")
    import math
    
    # Calculate the number of columns required using the ceiling of the square root
    cols = math.ceil(math.sqrt(len(s)))
    
    # Collect characters for each column using string slicing with a stride equal to 'cols'
    result = []
    for i in range(cols):
        result.append(s[i::cols])
        
    # Join the columns with a single space between them
    return " ".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
