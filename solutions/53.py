"""
Question 53: https://leetcode.com/problems/maximum-subarray/

Although LeetCode rates this as an easy question, the O(n) is not so trivial to find.
Basically, we go through the array and replace nums[i] with the sum of the maximum subarray that starts in the index i.
It's a dynamic programming approach to get a O(n) solution, instead of the naive solution that would take (On**2), as
it'd try to test all the subarrays to get the maximum sum.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            nums[i] = max(nums[i], nums[i + 1] + nums[i])
            result = max(result, nums[i])
        
        return result
