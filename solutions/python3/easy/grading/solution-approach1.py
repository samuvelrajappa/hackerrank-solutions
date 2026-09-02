# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
# Problem     Grading Students
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 12:01 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    rounded_grades = []
    
    for grade in grades:
        # Failing grades under 38 are never rounded
        if grade < 38:
            rounded_grades.append(grade)
        else:
            # Find the distance to the next multiple of 5
            remainder = grade % 5
            
            # If the difference is less than 3, round up
            if remainder >= 3:
                rounded_grades.append(grade + (5 - remainder))
            else:
                rounded_grades.append(grade)
                
    return rounded_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
