# Question 2740: https://leetcode.com/problems/find-the-value-of-the-partition/

"""
    Very interesting question, just sort the array for the solution to come naturally.
"""

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()

        result = abs(nums[0] - nums[1])
        for i in range(len(nums) - 1):
            result = min(result, abs(nums[i] - nums[i+1]))

        return result
