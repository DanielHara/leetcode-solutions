# Question 1911: https://leetcode.com/problems/maximum-alternating-subsequence-sum/

"""
    Just use DP to do it
"""

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Let S[i] be the subsequence with the highest alternating sum which begins with nums[i]
        S = [None for i in range(len(nums))]
        # Let T[i] be the subsequence with the lowest alternating sum which begins with nums[i]
        T = [None for i in range(len(nums))]

        max_S = nums[-1]
        min_T = nums[-1]
        S[-1] = nums[-1]
        T[-1] = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            S[i] = max(nums[i] - min_T, nums[i])
            T[i] = min(nums[i] - max_S, nums[i])
            
            max_S = max(max_S, S[i])
            min_T = min(min_T, T[i])
        
        return max(S)
