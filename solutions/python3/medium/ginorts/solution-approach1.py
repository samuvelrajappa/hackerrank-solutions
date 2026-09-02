# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
# Problem     ginortS
# Difficulty  Medium
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:57 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
def custom_sort(s):
    lowercase = []
    uppercase = []
    odd_digits = []
    even_digits = []
    for char in s:
        if char.islower():
            lowercase.append(char)
        elif char.isupper():
            uppercase.append(char)
        elif char.isdigit():
            if int(char) % 2 != 0:
                odd_digits.append(char)
            else:
                even_digits.append(char)  
    lowercase.sort()
    uppercase.sort()
    odd_digits.sort()
    even_digits.sort()
    return "".join(lowercase + uppercase + odd_digits + even_digits)
if __name__ == '__main__':
    s = input().strip()
    print(custom_sort(s))
