# Question 2221: https://leetcode.com/problems/find-triangular-sum-of-an-array/

"""
    Just a trivial solution already passes the judge.
"""

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_nums = []
            for i in range(0, len(nums) - 1):
                new_nums.append((nums[i] + nums[i + 1]) % 10)
            
            nums = new_nums

        return nums[0]

