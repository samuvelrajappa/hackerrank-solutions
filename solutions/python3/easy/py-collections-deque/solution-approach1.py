# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
# Problem     Collections.deque()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:55 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

# Read number of operations
n = int(input())
d = deque()

# Process each operation dynamically
for _ in range(n):
    inputs = input().split()
    method_name = inputs[0]
    
    if len(inputs) > 1:
        # For methods requiring an argument (append, appendleft)
        getattr(d, method_name)(inputs[1])
    else:
        # For methods requiring no arguments (pop, popleft)
        getattr(d, method_name)()

# Print space-separated elements
print(*d)
