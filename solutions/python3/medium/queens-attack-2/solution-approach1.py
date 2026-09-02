# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true
# Problem     Queen's Attack II
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 01:05 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    # Maximum moves possible in each direction without obstacles
    up = n - r_q
    down = r_q - 1
    right = n - c_q
    left = c_q - 1
    
    up_right = min(up, right)
    down_right = min(down, right)
    down_left = min(down, left)
    up_left = min(up, left)
    
    # Process each obstacle to bound the distances
    for r_o, c_o in obstacles:
        # Vertical alignment (same column)
        if c_o == c_q:
            if r_o > r_q:
                up = min(up, r_o - r_q - 1)
            else:
                down = min(down, r_q - r_o - 1)
                
        # Horizontal alignment (same row)
        elif r_o == r_q:
            if c_o > c_q:
                right = min(right, c_o - c_q - 1)
            else:
                left = min(left, c_q - c_o - 1)
                
        # Diagonal alignment
        elif abs(r_o - r_q) == abs(c_o - c_q):
            if r_o > r_q and c_o > c_q:    # Up-Right
                up_right = min(up_right, r_o - r_q - 1)
            elif r_o < r_q and c_o > c_q:  # Down-Right
                down_right = min(down_right, r_q - r_o - 1)
            elif r_o < r_q and c_o < c_q:  # Down-Left
                down_left = min(down_left, r_q - r_o - 1)
            elif r_o > r_q and c_o < c_q:  # Up-Left
                up_left = min(up_left, r_o - r_q - 1)
                
    # Total attackable squares is the sum of valid spaces in all directions
    return up + down + right + left + up_right + down_right + down_left + up_left

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
