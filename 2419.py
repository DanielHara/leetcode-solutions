"""
Question 2419: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/
    Well, a & b <= a and a & b <= always hold.

    So, just take the longest subarray filled with the maximum value in nums.

    Another trivial question labelled as "Medium" :(
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)

        result = 0

        i = 0
        while i < len(nums):
            if nums[i] == maximum:
                j = i + 1
                while j < len(nums) and nums[j] == maximum:
                    j = j + 1
            
                result = max(result, j - i)
            
                i = j
            else:
                i = i + 1

        return result
