# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-binary-search-trees/problem?isFullScreen=true
# Problem     Day 22: Binary Search Trees
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:29 a.m.
# ──────────────────────────────────────────────────


    def getHeight(self,root):
        #Write your code here
        if root is None:
            return -1
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        
        return 1 + max(left_height, right_height)


