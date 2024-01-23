"""
Question 2091: https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

    A fairly trivial question, really, should actually be rated as easy.
"""

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # All the elements are distinct
        
        maximum_index = 0
        minimum_index = 0
        
        for i in range(1, len(nums)):
            if nums[maximum_index] < nums[i]:
                maximum_index = i
            
            if nums[minimum_index] > nums[i]:
                minimum_index = i
        
        lesser_index = min(minimum_index, maximum_index)
        greater_index = max(minimum_index, maximum_index)
        
        return min(greater_index + 1, len(nums) - lesser_index, lesser_index + 1 + len(nums) - greater_index)
