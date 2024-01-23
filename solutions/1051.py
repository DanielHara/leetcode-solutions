# Question 1051: https://leetcode.com/problems/height-checker/description/

"""
    Trivial question.
"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)

        result = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                result = result + 1
        
        return result
