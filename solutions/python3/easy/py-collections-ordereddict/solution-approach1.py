# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
# Problem     Collections.OrderedDict()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 11:55 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

# Initialize the OrderedDict to maintain insertion order
item_dict = OrderedDict()

# Read the total number of item entries
n = int(input())

# Process each entry line by line
for _ in range(n):
    # Separate the item name from the net price by splitting from the right
    item_name, net_price = input().rsplit(' ', 1)
    net_price = int(net_price)
    
    # Calculate and accumulate the cumulative net price
    if item_name in item_dict:
        item_dict[item_name] += net_price
    else:
        item_dict[item_name] = net_price

# Print each unique item name and its final combined net price
for item_name, net_price in item_dict.items():
    print(item_name, net_price)
