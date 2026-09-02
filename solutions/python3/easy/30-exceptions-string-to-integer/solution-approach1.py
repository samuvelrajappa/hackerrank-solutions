# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?isFullScreen=true
# Problem     Day 16: Exceptions - String to Integer
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:28 a.m.
# ──────────────────────────────────────────────────

S = input()
try:
    print(int(S))
except ValueError:
    print('Bad String')
