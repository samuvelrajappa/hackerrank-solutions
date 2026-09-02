# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
# Problem     Company Logo
# Difficulty  Medium
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:55 a.m.
# ──────────────────────────────────────────────────

from collections import Counter

if __name__ == '__main__':
    s = input()
    
    # Count the occurrence of each character
    counts = Counter(s)
    
    # Sort by frequency (descending) primarily, then by character (alphabetical/ascending) secondarily
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Print the top 3 characters along with their counts
    for char, count in sorted_chars[:3]:
        print(char, count)
