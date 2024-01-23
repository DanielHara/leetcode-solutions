# Question 2012: https://leetcode.com/problems/sum-of-beauty-in-the-array/

"""
    Just use a bit of DP to get the answer
"""

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        # A[i] is the maximum of nums[0:i + 1]

        A = []
        for num in nums:
            A.append(max(num, (A[-1] if A else 0)))
        
        # B[i] is the minimum of nums[i:]

        B = [None for i in range(len(nums))]
        B[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            B[i] = min(nums[i], B[i + 1])
        
        result = 0
        for i in range(1, len(nums) - 1, 1):
            if A[i - 1] < nums[i] < B[i + 1]:
                result = result + 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                result = result + 1

        return result
