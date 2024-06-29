"""
    Question 2592: https://leetcode.com/problems/maximize-greatness-of-an-array/

    Very interesting question! Just sort the array and use a 2-pointer approach. Do it greedily.
    For example, if you find the number 5 in the array, try to find for the lowest number larger than 5 to get the optimal result.
"""

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()

        # 2-pointer approach:
        i = 0
        j = 0
        
        result = 0
        while i < len(nums):
            while j <= i:
                j = j + 1
            
            while j < len(nums) and nums[j] <= nums[i]:
                j = j + 1
            
            if j < len(nums):
                j = j + 1
                result = result + 1
            
            i = i + 1
        
        return result
