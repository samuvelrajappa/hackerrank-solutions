# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-nested-logic/problem?isFullScreen=true
# Problem     Day 26: Nested Logic
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:32 a.m.
# ──────────────────────────────────────────────────

# Read the actual return date (d1, m1, y1)
d1, m1, y1 = map(int, input().split())

# Read the expected return date / due date (d2, m2, y2)
d2, m2, y2 = map(int, input().split())

# Calculate the fine using nested logic conditions
if y1 > y2:
    fine = 10000
elif y1 == y2:
    if m1 > m2:
        fine = 500 * (m1 - m2)
    elif m1 == m2:
        if d1 > d2:
            fine = 15 * (d1 - d2)
        else:
            fine = 0
    else:
        fine = 0
else:
    fine = 0

# Print the final calculated fine
print(fine)
