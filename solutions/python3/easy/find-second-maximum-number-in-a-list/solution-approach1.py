# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:12 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    arr.sort()
    print(arr[-2])
