# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
# Problem     String Formatting
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:51 a.m.
# ──────────────────────────────────────────────────

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        dec = str(i)
        octal = oct(i)[2:]
        hex_cap = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{dec.rjust(width)} {octal.rjust(width)} {hex_cap.rjust(width)} {binary.rjust(width)}")


