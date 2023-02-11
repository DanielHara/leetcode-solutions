"""
Question 462: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii

Do it greedily: sort the array and split it into two halves. For example, if you're array is [1,10,2,9]:
Sort it:
It becomes [1,2,9,10]

Then calculate how many steps you need for all elements in the first half to become the max of the first half,
and how many steps you need for all elements in the second half to become the min of the second half. This is a greedy approach.

Then you get just 2 values, and see which one is best for you to transform into an array with just 1 value.
"""

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) <= 1:
            return 0
        
        if len(nums) == 2:
            return nums[1] - nums[0]

        half = len(nums) // 2

        a = nums[half]
        b = nums[half + 1]

        result = a * half - sum(nums[0: half])
        
        result = result + sum(nums[half + 2: len(nums)]) - b * (len(nums) - (half + 2))
        
        result = result + (b - a) * min(half + 1, len(nums) - (half + 1))
        return result
