# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?isFullScreen=true
# Problem     Day 8: Dictionaries and Maps
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:25 a.m.
# ──────────────────────────────────────────────────

import sys

def solve():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
    n = int(input_lines[0])
    phone_book = {}
    for i in range(1, n + 1):
        name, phone = input_lines[i].split()
        phone_book[name] = phone
    for query in input_lines[n + 1:]:
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")

if __name__ == "__main__":
    solve()
