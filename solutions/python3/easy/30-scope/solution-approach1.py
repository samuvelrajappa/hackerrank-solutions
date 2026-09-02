# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-scope/problem?isFullScreen=true
# Problem     Day 14: Scope
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:27 a.m.
# ──────────────────────────────────────────────────


        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        min_element = min(self.__elements)
        max_element = max(self.__elements)
        self.maximumDifference = max_element - min_element

