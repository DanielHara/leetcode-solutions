# Question 2270: https://leetcode.com/problems/number-of-ways-to-split-array/

"""
    A tiny little bit of DP already does the trick.
"""

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        S = [nums[0]]

        for i in range(1, len(nums)):
            S.append(S[-1] + nums[i])

        result = 0
        for i in range(0, len(nums) - 1):
            if S[i] >= S[-1] - S[i]:
                result = result + 1

        return result
