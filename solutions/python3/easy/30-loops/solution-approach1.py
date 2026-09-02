# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-loops/problem?isFullScreen=true
# Problem     Day 5: Loops
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:23 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
