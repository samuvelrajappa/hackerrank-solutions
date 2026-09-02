# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
# Problem     Piling Up!
# Difficulty  Medium
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:57 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

def can_stack_cubes():
    # Read the number of test cases
    t = int(input())
    
    for _ in range(t):
        # Read the number of cubes and their side lengths
        n = int(input())
        cubes = deque(map(int, input().split()))
        
        current_top = float('inf')
        possible = True
        
        # Greedily pick the larger of the leftmost or rightmost cube
        while cubes:
            if cubes[0] >= cubes[-1]:
                picked = cubes.popleft()
            else:
                picked = cubes.pop()
                
            # If the picked cube is larger than the one below it, it's invalid
            if picked > current_top:
                possible = False
                break
                
            current_top = picked
            
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    can_stack_cubes()
