# Question 2348: https://leetcode.com/problems/number-of-zero-filled-subarrays/

"""
    Actually a fairly simple question.
"""

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i = 0

        result = 0
        while i < len(nums):
            if nums[i] == 0:
                j = i
                while j < len(nums) and nums[j] == 0:
                    j = j + 1

                N = j - i

                result = result + N * (N + 1) // 2
                i = j
            else:
                i = i + 1
        
        return result
