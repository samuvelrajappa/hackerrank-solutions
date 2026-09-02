# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-queues-stacks/problem?isFullScreen=true
# Problem     Day 18: Queues and Stacks
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:28 a.m.
# ──────────────────────────────────────────────────



class Solution:
    def __init__(self):
        # Initialize internal collection instances for stack and queue
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch: str) -> None:
        # Pushes a character onto the stack
        self.stack.append(ch)

    def enqueueCharacter(self, ch: str) -> None:
        # Enqueues a character in the queue
        self.queue.append(ch)

    def popCharacter(self) -> str:
        # Pops and returns the top character from the stack
        return self.stack.pop()

    def dequeueCharacter(self) -> str:
        # Dequeues and returns the first character from the queue
        return self.queue.pop(0)


