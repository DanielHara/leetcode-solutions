# Question 1480: https://leetcode.com/problems/running-sum-of-1d-array/

"""
    Too easy even for a question labelled as easy
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        S = [nums[0]]

        for i in range(1, len(nums)):
            S.append(S[-1] + nums[i])
        
        return S
