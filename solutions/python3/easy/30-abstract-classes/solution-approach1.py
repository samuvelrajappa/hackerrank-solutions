# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-abstract-classes/problem?isFullScreen=true
# Problem     Day 13: Abstract Classes
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:27 a.m.
# ──────────────────────────────────────────────────



#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        # Call the parent Book class constructor to initialize title and author
        super().__init__(title, author)
        # Initialize the price attribute
        self.price = price

    def display(self):
        # Print the required three lines with a space after the colon
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")


