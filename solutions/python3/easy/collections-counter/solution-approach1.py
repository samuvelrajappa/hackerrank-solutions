# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# Problem     collections.Counter()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:52 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# Read total number of shoes
num_shoes = int(input())

# Read all available shoe sizes and convert to a frequency map using Counter
shoe_sizes = Counter(map(int, input().split()))

# Read the number of customers
num_customers = int(input())

# Initialize the total revenue earned
total_revenue = 0

# Process each customer transaction
for _ in range(num_customers):
    size, price = map(int, input().split())
    
    # Check if the requested shoe size is available in inventory
    if shoe_sizes[size] > 0:
        total_revenue += price
        shoe_sizes[size] -= 1  # Reduce stock by 1

# Print the total money earned
print(total_revenue)
