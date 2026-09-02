# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# Problem     Merge the Tools!
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:52 a.m.
# ──────────────────────────────────────────────────

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i : i + k]
        
        unique_chars = "".join(dict.fromkeys(substring))
        
        print(unique_chars)

