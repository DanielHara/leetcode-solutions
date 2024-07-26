# Question 2865: https://leetcode.com/problems/beautiful-towers-i/

"""
    Very interesting question. From the constraints: len(heights) <= 10**3, which hints that a quadratic solution
    would pass the judge. So, for every index in heights, just calculate the possible sum for the case in which that one index
    is the peak.
"""

class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        maximum_height = max(heights)

        result = 0
        for index in range(len(heights)):
            s = heights[index]
            
            left = heights[index]
            for left_index in range(index - 1, -1, -1):
                left = min(left, heights[left_index])
                s = s + left
            
            right = heights[index]
            for right_index in range(index + 1, len(heights)):
                right = min(right, heights[right_index])
                s = s + right

            result = max(result, s)

        return result
