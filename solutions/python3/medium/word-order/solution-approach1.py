# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# Problem     Word Order
# Difficulty  Medium
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:55 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

# Read the number of words
n = int(input())

# Initialize an OrderedDict to keep track of count and insertion order
words = OrderedDict()

for _ in range(n):
    word = input().strip()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

# Output the number of distinct words
print(len(words))

# Output the occurrences separated by a space
print(*(words.values()))

