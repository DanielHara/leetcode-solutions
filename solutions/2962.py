# Question 2962: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

"""
    Just sliding window, no secrets
"""

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        
        start = 0
        end = 0

        count = 1 if nums[0] == target else 0

        result = 0
        while start < len(nums):
            while end < len(nums) - 1 and count < k:
                end = end + 1
                if nums[end] == target:
                    count = count + 1
            
            if count >= k:
                result = result + len(nums) - end

            if nums[start] == target:
                count = count - 1
            start = start + 1
        
        return result
