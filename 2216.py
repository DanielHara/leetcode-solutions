# Question 2216: https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

"""
    Do it greedily.
"""

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        result = 0
        i = 0
        while i < len(nums):
            j = i + 1
            
            while j < len(nums) and nums[j] == nums[i]:
                j = j + 1
            
            if j >= len(nums):
                result = result + j - i
                return result
        
            result = result + j - i - 1
            i = j + 1
        
        return result
