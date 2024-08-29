# Question 1838: https://leetcode.com/problems/frequency-of-the-most-frequent-element/

"""
    Use sliding window!
"""

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)

        # Use a sliding window:
        start = 0
        end = 0
        soma = 0

        result = 0

        while start < len(nums):
            while end < len(nums) - 1 and soma + abs(nums[end + 1] - nums[start]) <= k:
                soma = soma + abs(nums[end + 1] - nums[start])
                end = end + 1
            
            if soma <= k:
                result = max(result, end - start + 1)
            
            if start < len(nums) - 1:
                soma = soma - (end - start) * (nums[start] - nums[start + 1])

            start = start + 1
        
        return result
