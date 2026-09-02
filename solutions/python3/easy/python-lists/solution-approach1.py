# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:12 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        parts = input().split()
        command = parts[0]
        if command == "insert":
            i = int(parts[1])
            e = int(parts[2])
            my_list.insert(i, e)
        elif command == "print":
            print(my_list)
        elif command == "remove":
            e = int(parts[1])
            my_list.remove(e)
        elif command == "append":
            e = int(parts[1])
            my_list.append(e)
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()
