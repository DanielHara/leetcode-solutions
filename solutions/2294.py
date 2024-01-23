# Question 2294: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

"""
    Actually an easy question, as the order of the nums array actually doesn't matter.
    After sorting it, the solution comes easily, just right away.
"""

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        result = 0

        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] - nums[i] <= k:
                j = j + 1

            i = j
            result = result + 1

        return result
