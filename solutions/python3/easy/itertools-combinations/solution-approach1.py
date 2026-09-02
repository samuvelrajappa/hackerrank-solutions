# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
# Problem     itertools.combinations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:56 a.m.
# ──────────────────────────────────────────────────

from itertools import combinations

# Read the string S and integer value k from STDIN
S, k = input().split()

# Loop through all combination sizes from 1 up to k (inclusive)
for length in range(1, int(k) + 1):
    # Sort the string characters to output in lexicographic order
    for comb in combinations(sorted(S), length):
        print(''.join(comb))
