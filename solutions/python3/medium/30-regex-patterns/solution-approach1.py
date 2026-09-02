# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-regex-patterns/problem?isFullScreen=true
# Problem     Day 28: RegEx, Patterns, and Intro to Databases
# Difficulty  Medium
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:32 a.m.
# ──────────────────────────────────────────────────

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    
    # List to store names of users with a Gmail account
    gmail_users = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        
        # Use regex to find if the email ends with @gmail.com
        if re.search(r"@gmail\.com$", emailID):
            gmail_users.append(firstName)

    # Sort the names alphabetically
    gmail_users.sort()
    
    # Print each name on a new line
    for name in gmail_users:
        print(name)
