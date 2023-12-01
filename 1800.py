# Question 1800: https://leetcode.com/problems/maximum-ascending-subarray-sum/

"""
    Trivial question
"""

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        
        i = 0
        while i < len(nums):
            j = i + 1

            S = nums[i]
            while j < len(nums) and nums[j] > nums[j - 1]:
                S = S + nums[j]
                j = j + 1
        
            result = max(result, S)
            
            i = j
        
        return result
