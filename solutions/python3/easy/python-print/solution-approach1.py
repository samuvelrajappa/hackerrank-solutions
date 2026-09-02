# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
# Problem     Print Function
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:11 a.m.
# ──────────────────────────────────────────────────

def print_numbers(i, n):
    if i > n:
        return
    print(i, end='')
    print_numbers(i + 1, n)
if __name__ == '__main__':
    n = int(input())
    print_numbers(1, n)
