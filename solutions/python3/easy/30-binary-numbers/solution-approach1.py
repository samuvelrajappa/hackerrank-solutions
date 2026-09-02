# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-binary-numbers/problem?isFullScreen=true
# Problem     Day 10: Binary Numbers
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



if __name__ == '__main__':
    n = int(input().strip())
    binary_str = bin(n)[2:]
    ones_groups = binary_str.split('0')
    max_consecutive_ones = max(len(group) for group in ones_groups)
    print(max_consecutive_ones)
