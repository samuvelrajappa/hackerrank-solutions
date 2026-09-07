# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true
# Problem     Organizing Containers of Balls
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-07, 10:11 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    # Calculate the total capacity of each container (sum of each row)
    container_capacities = sorted([sum(row) for row in container])
    
    # Calculate the total number of balls for each type (sum of each column)
    ball_type_counts = sorted([sum(container[i][j] for i in range(len(container))) for j in range(len(container[0]))])
    
    # If the distribution matches, organization is possible
    if container_capacities == ball_type_counts:
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
