# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true
# Problem     ACM ICPC Team
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-07, 10:09 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    # Convert each binary string to an integer for efficient bitwise operations
    topic_ints = [int(t, 2) for t in topic]
    n = len(topic)
    
    max_topics = 0
    team_count = 0
    
    # Check every unique pair of attendees
    for i in range(n):
        for j in range(i + 1, n):
            # Bitwise OR combines the topics known by both attendees
            combined_topics = topic_ints[i] | topic_ints[j]
            
            # Count the number of '1's (topics known)
            known_count = bin(combined_topics).count('1')
            
            # Track the maximum topics and the number of teams that achieve it
            if known_count > max_topics:
                max_topics = known_count
                team_count = 1
            elif known_count == max_topics:
                team_count += 1
                
    return [max_topics, team_count]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
