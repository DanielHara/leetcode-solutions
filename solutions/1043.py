# Question 1043: https://leetcode.com/problems/partition-array-for-maximum-sum/

"""
    Fairly trivial DP question. By seeing that 1 <= k <= arr.length <= 500, you can already notice that a O(n**2) solution will do.
"""

class Solution:
    def recursiveMaxSumAfterPartitioning(self, start: int, arr: List[int], k, dp) -> int:
        if start >= len(arr):
            return 0
        
        if dp[start] is not None:
            return dp[start]
        
        maximum = 0
        result = 0
        for end in range(start, min(start + k, len(arr)), 1):
            maximum = max(maximum, arr[end])
            further = self.recursiveMaxSumAfterPartitioning(end + 1, arr, k, dp)
            
            result = max(result, maximum * (end - start + 1) + further)
            
        dp[start] = result
        return result

    
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [None for i in range(len(arr))]
        
        return self.recursiveMaxSumAfterPartitioning(0, arr, k, dp)
