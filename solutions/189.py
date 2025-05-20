# Question 189: https://leetcode.com/problems/rotate-array/

"""
    This is the trivial solution: O(N) time, O(N) space
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        answer = [nums[(index - k) % len(nums)] for index in range(len(nums))]
        
        for index in range(len(answer)):
            nums[index] = answer[index]
