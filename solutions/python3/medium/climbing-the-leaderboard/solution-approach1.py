# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
# Problem     Climbing the Leaderboard
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 01:00 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    unique_ranked = sorted(list(set(ranked)), reverse=True)
    
    result = []
    # Start tracking from the bottom of the unique leaderboard
    leaderboard_index = len(unique_ranked) - 1
    
    for score in player:
        # Move up the leaderboard while the player's score is greater or equal
        while leaderboard_index >= 0 and score >= unique_ranked[leaderboard_index]:
            leaderboard_index -= 1
        
        # The rank is the index position plus 2
        result.append(leaderboard_index + 2)
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
