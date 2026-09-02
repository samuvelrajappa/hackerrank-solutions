# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/30-testing/problem?isFullScreen=true
# Problem     Day 27: Testing
# Difficulty  Easy
# Subdomain   30 Days of Code
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:32 a.m.
# ──────────────────────────────────────────────────


class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        return []
        # complete this function

class TestDataUniqueValues(object):
    data = []
    for i in range(5):
        data.append(i)
    data[::-1]  
    @staticmethod
    def get_array():
        return TestDataUniqueValues.data
    @staticmethod
    def get_expected_result():
        data = TestDataUniqueValues.get_array()
        return data.index(min(data))
        # complete this function

class TestDataExactlyTwoDifferentMinimums(object):
    data = []
    for i in range(5):
        data.append(i)
    data[::-1] 
    data.insert(0,0)
    
    @staticmethod
    def get_array():
        return TestDataExactlyTwoDifferentMinimums.data
    @staticmethod
    def get_expected_result():
        data = TestDataExactlyTwoDifferentMinimums.get_array()
        return data.index(min(data))
