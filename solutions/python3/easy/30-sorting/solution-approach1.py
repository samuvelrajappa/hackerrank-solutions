# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true
# Problem     Day 20: Sorting
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:28 a.m.
# ──────────────────────────────────────────────────

n = int(input())
a = list(map(int, input().split()))

total_swaps = 0

for i in range(n):
    numberOfSwaps = 0
    
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1
            total_swaps += 1
            
    if numberOfSwaps == 0:
        break

print(f"Array is sorted in {total_swaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
