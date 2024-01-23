# Question 2274: https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors

"""
    Actually, quite a trivial question.
"""

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort(reverse=True)

        result = 0
        while bottom < top:
            floor = special.pop() if special else (top + 1)
            result = max(result, floor - bottom)

            bottom = floor + 1
        
        return result
