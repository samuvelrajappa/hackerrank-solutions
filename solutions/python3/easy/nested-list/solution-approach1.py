# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Problem     Nested Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:12 a.m.
# ──────────────────────────────────────────────────

N = int(input())

records = []

for _ in range(N):
    name = input()
    grade = float(input())
    records.append([name, grade])

grades = []

for student in records:
    grades.append(student[1])

grades = list(set(grades))
grades.sort()

second_lowest = grades[1]

names = []

for student in records:
    if student[1] == second_lowest:
        names.append(student[0])

names.sort()

for name in names:
    print(name)
