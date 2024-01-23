# Question 1913: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

"""
  All the numbers are positive.
  Simply pick the 2 largest and 2 smallest and calculate the product difference
"""

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        return nums[len(nums) - 1] * nums[len(nums) - 2] - nums[0] * nums[1]
