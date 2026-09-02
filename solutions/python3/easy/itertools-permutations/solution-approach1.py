# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Problem     itertools.permutations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:54 a.m.
# ──────────────────────────────────────────────────

from itertools import permutations

# Read the space-separated string and size k
s, k = input().split()

# Generate and print permutations using sorted(s) to guarantee lexicographic order
for p in permutations(sorted(s), int(k)):
    print("".join(p))
