"""
Question 674: https://leetcode.com/problems/longest-continuous-increasing-subsequence/
"""

"""
Just do it, 2 pointer approach, O(N)
"""

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i = 0
        
        result = 0
        while i < len(nums):
            j = i + 1
            
            while j < len(nums) and nums[j] > nums[j - 1]:
                j = j + 1
            
            result = max(result, j - i)
        
            i = j
        
        return result
