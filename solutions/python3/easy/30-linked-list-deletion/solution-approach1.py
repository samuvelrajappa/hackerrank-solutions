# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-linked-list-deletion/problem?isFullScreen=true
# Problem     Day 24: More Linked Lists
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:29 a.m.
# ──────────────────────────────────────────────────



    def removeDuplicates(self,head):
        if head is None:
            return None
        
        current = head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
                
        return head

