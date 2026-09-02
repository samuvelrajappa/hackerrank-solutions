# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
# Problem     Alphabet Rangoli
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:51 a.m.
# ──────────────────────────────────────────────────

def print_rangoli(size):
    import string
    # Get all lowercase letters
    alpha = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        # Extract the letters needed for the current row
        s = "-".join(alpha[size - 1 : size - 1 - i : -1] + alpha[size - 1 - i : size])
        # Center the row with hyphens
        lines.append(s.center(4 * size - 3, "-"))
        
    # Join the top half with the bottom half (reversed top half excluding center)
    print("\n".join(lines + lines[:-1][::-1]))

