# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-operators/problem?isFullScreen=true
# Problem     Day 2: Operators
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

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip_percent = (meal_cost/100) * tip_percent
    tax_percent = (tax_percent/100) * meal_cost
    total = meal_cost + tip_percent + tax_percent
    print(round(total))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
