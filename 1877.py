# Question 1877: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

"""
    Quite easy question, just sort the array before hand, and your best chance of having a minimized maximum pair sum is
    pairing up a high (from the end of the sorted array) and a low number (from the beginning of the sorted array).
"""

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        start = 0
        end = len(nums) - 1

        result = 0
        while start < end:
            result = max(result, nums[start] + nums[end])
            
            start = start + 1
            end = end - 1

        return result
