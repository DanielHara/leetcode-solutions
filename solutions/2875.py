# Question 2875: https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

"""
    This is an amazingly interesting question!
    Take the sum of nums, and use multiple chunks of the array as much as you need to come as close as possible to target. This will have length
    len(nums) * (target // sum_nums)
    Take the remainder, and find the shortest subarray of nums concatenated with itself (nums + nums), which sums to target.
    You can use a sliding window to do it.
"""

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)

        result = len(nums) * (target // sum_nums)
        remainder = target % sum_nums

        nums = nums + nums

        start = 0
        end = 0
        s = 0
        partial = None
        while start < len(nums):
            while end < len(nums) and s < remainder:
                s = s + nums[end]
                end = end + 1

            if s == remainder:
                partial = min(partial, end - start) if partial is not None else end - start

            s = s - nums[start]
            start = start + 1

        result = result + partial if partial is not None else -1

        return result 
