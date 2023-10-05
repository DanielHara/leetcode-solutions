"""
Question 1664: https://leetcode.com/problems/ways-to-make-a-fair-array/

Using a bit of DP cracks it.
"""


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        S_odd = 0
        S_even = 0

        for i in range(0, len(nums) - 1, 1):
            if i % 2 == 0:
                S_even = S_even + nums[i]
            else:
                S_odd = S_odd + nums[i]
        
        right_even = 0
        right_odd = 0
        result = 0
        for i in range(len(nums) - 1, -1, -1):
            if S_odd + right_odd == S_even + right_even:
                result = result + 1
            
            if i % 2 == 0:
                S_odd = S_odd - (nums[i - 1] if i - 1 >= 0 else 0)
                right_odd = nums[i] + right_odd
            else:
                S_even = S_even - (nums[i - 1] if i - 1 >= 0 else 0)
                right_even = nums[i] + right_even
        
        return result

