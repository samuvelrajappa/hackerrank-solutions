# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Problem     The Minion Game
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:52 a.m.
# ──────────────────────────────────────────────────

def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    
    for i in range(length):
        if string[i] in vowels:
            # Kevin gets points for words starting with vowels
            kevin_score += length - i
        else:
            # Stuart gets points for words starting with consonants
            stuart_score += length - i
            
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

