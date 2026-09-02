# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-arrays/problem?isFullScreen=true
# Problem     Day 7: Arrays
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:24 a.m.
# ──────────────────────────────────────────────────

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return        
    N = int(input_data[0])
    arr = input_data[1:N+1]    
    reversed_arr = arr[::-1]    
    print(*(reversed_arr))

if __name__ == '__main__':
    main()
