// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem?isFullScreen=true
// Problem     Day 25: Running Time and Complexity
// Difficulty  Medium
// Subdomain   30 Days of Code
// Platform    HackerRank
// Language    cpp
// Status      Accepted
// Submitted   2026-09-02, 09:31 a.m.
// ──────────────────────────────────────────────────

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// Function to check if a number is prime in O(sqrt(n)) time
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    
    // Eliminate multiples of 2 and 3 quickly
    if (n % 2 == 0 || n % 3 == 0) return false;
    
    // Check divisors up to sqrt(n) skipping multiples of 2 and 3
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int t;
    if (cin >> t) {
        while (t--) {
            int n;
            cin >> n;
            if (isPrime(n)) {
                cout << "Prime" << endl;
            } else {
                cout << "Not prime" << endl;
            }
        }
    }
    return 0;
}
