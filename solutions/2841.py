"""
    Question 2841: https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

    Just take the sliding window in the substring, with length k, and save the frequency of characters,
    and their sum
"""

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        result = 0
        S = 0
        frequency_dict = {}
        for index in range(0, k):
            S = S + nums[index]
            frequency_dict[nums[index]] = frequency_dict.get(nums[index], 0) + 1
        
        if len(frequency_dict) >= m:
            result = S
        
        for index in range(k, len(nums)):
            S = S + nums[index]
            frequency_dict[nums[index]] = frequency_dict.get(nums[index], 0) + 1
            
            frequency_dict[nums[index - k]] =  frequency_dict[nums[index - k]] - 1
            if frequency_dict[nums[index - k]] == 0:
                del frequency_dict[nums[index - k]]
            
            S = S - nums[index - k]

            if len(frequency_dict) >= m:
                result = max(S, result)
        
        return result
