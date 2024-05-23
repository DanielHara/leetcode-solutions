# Question 2762: https://leetcode.com/problems/continuous-subarrays/

"""
    Very interesting, typical sliding window question.
"""

class Solution:
    def is_valid(self, frequency_dict):
        keys = list(frequency_dict.keys())
        if not keys:
            return True

        return max(keys) - min(keys) <= 2

    def continuousSubarrays(self, nums: List[int]) -> int:
        start = 0
        end = 0

        result = 0
        frequency_dict = {}
        frequency_dict[nums[0]] = 1

        while start < len(nums):
            while end < len(nums) - 1 and self.is_valid(frequency_dict):
                frequency_dict[nums[end + 1]] = frequency_dict.get(nums[end + 1], 0) + 1
                end = end + 1
            
            if self.is_valid(frequency_dict):
                result = result + end - start + 1
            else:
                result = result + end - start

            frequency_dict[nums[start]] = frequency_dict[nums[start]] - 1
            if frequency_dict[nums[start]] == 0:
                del frequency_dict[nums[start]]
            
            start = start + 1

        return result
