# Question 2779: https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

"""
    Very interesting question! Thinking a bit, it's easy to come to the conclusion that we order of nums actually
    doesn't matter. Then, sorting the array and using a sliding window cracks the problem.
"""

class Solution:    
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        result = 1

        i = 0
        j = 1
        while j < len(nums):
            while j < len(nums) and nums[j] - nums[i] <= 2*k:
                j = j + 1
            
            result = max(result, j - i)

            if j == len(nums):
                return result

            while i < len(nums) and nums[j] - nums[i] > 2*k:
                i = i + 1

        return result
