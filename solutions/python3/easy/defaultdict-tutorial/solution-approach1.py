# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
# Problem     DefaultDict Tutorial
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:54 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# Read the sizes of group A (n) and group B (m)
n, m = map(int, input().split())

# Initialize a defaultdict with lists as values
group_A = defaultdict(list)

# Read words for group A and store their 1-indexed positions
for i in range(1, n + 1):
    word = input().strip()
    group_A[word].append(i)

# Read words for group B and print their positions or -1
for _ in range(m):
    word = input().strip()
    if word in group_A:
        print(*group_A[word])
    else:
        print(-1)
