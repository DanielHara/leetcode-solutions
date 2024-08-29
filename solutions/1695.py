# Question 1695: https://leetcode.com/problems/maximum-erasure-value/

"""
   Just use a sliding window to always finds the longest subarrays with all unique characters, and get ther sum.
   Then, you can just pick the largest sum.
"""

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = 0
        end = 0

        element_set = set()
        element_set.add(nums[0])
        s = nums[0]
        result = s

        while start < len(nums):
            while end < len(nums):
                result = max(result, s)
                end = end + 1
                if end < len(nums):
                    if nums[end] not in element_set:
                        element_set.add(nums[end])
                        s = s + nums[end]
                    else:
                        while start < len(nums) and nums[end] in element_set:
                            s = s - nums[start]
                            element_set.remove(nums[start])
                            start = start + 1

                        element_set.add(nums[end])
                        s = s + nums[end]
        
            if start < len(nums):
                s = s - nums[start]
                element_set.remove(nums[start])
                start = start + 1
        
        return result   
