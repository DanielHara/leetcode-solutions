# Question 1893: https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

"""
    Easy question, just do it. The contraints are very small, so no optimisation is needed.
"""

class Solution:
    def isNumberCoveredByRanges(self, ranges: List[List[int]], number: int):
        for [start, end] in ranges:
            if start <= number and number <= end:
                return True

        return False
    
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for number in range(left, right + 1):
            if not self.isNumberCoveredByRanges(ranges, number):
                return False
        
        return True
