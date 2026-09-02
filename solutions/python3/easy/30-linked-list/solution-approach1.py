# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-linked-list/problem?isFullScreen=true
# Problem     Day 15: Linked List
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:27 a.m.
# ──────────────────────────────────────────────────



    def insert(self, head, data):
        new_node = Node(data)
        if head is None:
            return new_node
        
        current = head
        while current.next is not None:
            current = current.next
            
        current.next = new_node
        return head


