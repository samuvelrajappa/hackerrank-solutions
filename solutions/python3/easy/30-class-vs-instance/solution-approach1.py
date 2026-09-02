# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-class-vs-instance/problem?isFullScreen=true
# Problem     Day 4: Class vs. Instance
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:23 a.m.
# ──────────────────────────────────────────────────

class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age += 1

