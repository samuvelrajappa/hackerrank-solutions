# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
# Problem     Capitalize!
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:51 a.m.
# ──────────────────────────────────────────────────



# Complete the solve function below.
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))


