# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-binary-trees/problem?isFullScreen=true
# Problem     Day 23: BST Level-Order Traversal
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:29 a.m.
# ──────────────────────────────────────────────────



    def levelOrder(self,root):
        if root is None:
            return
        
        queue = [root]
        
        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

