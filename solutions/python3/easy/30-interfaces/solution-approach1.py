# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-interfaces/problem?isFullScreen=true
# Problem     Day 19: Interfaces
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:28 a.m.
# ──────────────────────────────────────────────────



class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        total_sum = 0
        
        for i in range(1, n + 1):
            if n % i == 0:
                total_sum += i
                
        return total_sum

