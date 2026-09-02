# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Problem     itertools.product()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:53 a.m.
# ──────────────────────────────────────────────────

from itertools import product

# Read space-separated integers for list A and list B
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute the Cartesian product and unpack to print space-separated tuples
print(*product(A, B))
