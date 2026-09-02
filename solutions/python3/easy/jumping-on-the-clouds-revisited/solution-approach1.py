# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true
# Problem     Jumping on the Clouds: Revisited
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

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    i = 0
    
    while True:
        # Move to the next cloud using circular modulo arithmetic
        i = (i + k) % n
        
        # Deduct 1 energy point for the jump
        energy -= 1
        
        # Deduct 2 additional energy points if landing on a thundercloud
        if c[i] == 1:
            energy -= 2
            
        # Stop once we cycle back to the starting cloud
        if i == 0:
            break
            
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
