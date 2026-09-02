# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
# Problem     Polar Coordinates
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:52 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

# Read the complex number from standard input
z = complex(input().strip())

# Print the modulus (r) using abs()
print(abs(z))

# Print the phase angle (phi) using cmath.phase()
print(cmath.phase(z))
