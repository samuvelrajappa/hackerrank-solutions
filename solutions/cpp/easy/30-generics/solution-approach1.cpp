// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/30-generics/problem?isFullScreen=true
// Problem     Day 21: Generics
// Difficulty  Easy
// Subdomain   30 Days of Code
// Platform    HackerRank
// Language    cpp
// Status      Accepted
// Submitted   2026-09-02, 09:30 a.m.
// ──────────────────────────────────────────────────



/**
*    Name: printArray170
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template <typename T>
void printArray(const vector<T>& arr) {
    for (const auto& element : arr) {
        cout << element << "\n";
    }
}

