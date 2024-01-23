# Question 1005: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/

"""
Just do it greedily
"""


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        # Just flip all the negatives:
        for i in range(len(nums)):
            if k <= 0:
                break

            if nums[i] < 0:
                nums[i] = (-1)* nums[i]
                k = k - 1

        if k <= 0:
            return sum(nums)

        if k % 2 == 0:
            return sum(nums)
        
        minimum = min(nums)

        return sum(nums) - 2 * minimum
