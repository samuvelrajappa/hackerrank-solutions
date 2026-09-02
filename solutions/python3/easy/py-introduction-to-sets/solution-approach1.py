# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
# Problem     Introduction to Sets
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:52 a.m.
# ──────────────────────────────────────────────────

def average(array):
    # your code goes here
    distinct_heights = set(array)
    
    # Calculate and return the average
    return sum(distinct_heights) / len(distinct_heights)

