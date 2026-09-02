# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
# Problem     String Split and Join
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:14 a.m.
# ──────────────────────────────────────────────────

def split_and_join(line):
    # write your code here
    l = line.split()
    l = "-".join(l)
    return l

