# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-more-exceptions/problem?isFullScreen=true
# Problem     Day 17: More Exceptions
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:28 a.m.
# ──────────────────────────────────────────────────

class Calculator:
    def power(self, n: int, p: int) -> int:
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        return n ** p


