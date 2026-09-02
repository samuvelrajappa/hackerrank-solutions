# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
# Problem     Any or All
# Difficulty  Easy
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:57 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()

numbers = input().split()

result = all(int(x) > 0 for x in numbers) and any(x == x[::-1] for x in numbers)

print(result)
