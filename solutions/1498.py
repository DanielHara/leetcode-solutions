"""
    Question 1498: https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

    Very interesting question! I just looked at the first hint, which says "Sort the array", and this helps a lot to solve the question.
    For each subsequence, it's important than the sum of its minimum and maximum is <= target, so the order of its elements
    actually doesn't matter, so sorting it is fine.

    After that, I thought about using a sliding window. This approach is rigorously not a sliding window, but has the same inspiration.
"""

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10** 9 + 7

        nums.sort()

        start = 0
        end = len(nums) - 1

        result = 0
        while start < len(nums):
            while end >= start and nums[end] + nums[start] > target:
                end = end - 1

            if start <= end and nums[end] + nums[start] <= target:
                result = (result + (2 ** (end - start)) % mod) % mod

            start = start + 1

        return result
