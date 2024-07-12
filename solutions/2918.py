# Question 2918: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

"""
    Do it greedily
"""

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeros1 = 0
        for num in nums1:
            if num == 0:
                zeros1 = zeros1 + 1
        
        zeros2 = 0
        for num in nums2:
            if num == 0:
                zeros2 = zeros2 + 1
        
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        if zeros1 == 0 and zeros2 == 0:
            return sum1 if sum1 == sum2 else -1

        if sum1 >= sum2:
            if zeros1 == 0 and sum2 + zeros2 > sum1:
                return -1
            if zeros2 == 0:
                return -1

        if sum2 >= sum1:
            if zeros2 == 0 and sum1 + zeros1 > sum2:
                return -1
            if zeros1 == 0:
                return -1

        return max(sum1 + zeros1, sum2 + zeros2)
