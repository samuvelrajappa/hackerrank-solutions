# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
# Problem     Collections.namedtuple()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:55 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N, Student = int(input()), namedtuple('Student', input())
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(N)) / N:.2f}")
