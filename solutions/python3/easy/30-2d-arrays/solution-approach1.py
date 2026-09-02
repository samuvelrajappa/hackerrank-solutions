# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-2d-arrays/problem?isFullScreen=true
# Problem     Day 11: 2D Arrays
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:27 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

def solve():
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().split())))
    max_sum = -63 
    
    for r in range(4):
        for c in range(4):
            top = arr[r][c] + arr[r][c+1] + arr[r][c+2]
            mid = arr[r+1][c+1]
            bot = arr[r+2][c+1] + arr[r+2][c+2] + arr[r+2][c]
            current_sum = (arr[r][c]   + arr[r][c+1]   + arr[r][c+2] + arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2])
            if current_sum > max_sum:
                max_sum = current_sum         
    print(max_sum)

if __name__ == '__main__':
    solve()
