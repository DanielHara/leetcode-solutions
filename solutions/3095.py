# Question 3095: https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

"""
    Just brute-force, O(N**2) solution, because 1 <= nums.length <= 50
"""

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        result = None
        for start in range(len(nums)):
            end = start
            accumulated_or = 0
            while end < len(nums) and accumulated_or < k:
                accumulated_or = accumulated_or | nums[end]
                end = end + 1

            if accumulated_or >= k:
                length = end - start
                result = min(result, length) if result is not None else length

        if result is None:
            return -1

        if result == 0:
            return 1

        return result
