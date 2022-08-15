# Question 945: https://leetcode.com/problems/minimum-increment-to-make-array-unique/

"""
    I asked myself if you'd help if the array came sorted.
"""

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        stack = []
        result = 0
        for num in nums:
            if not stack or stack[-1] < num:
                stack.append(num)
            else:
                result = result + stack[-1] - num + 1
                stack.append(stack[-1] + 1)
        
        return result
