# Question 2915: https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

"""
    Another version of the knapsack problem
"""

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        # dp[index][n] is the length of the longest subsequenc, including nums[index], which sums to n
        # If there's no subsequence after includnig nums[index] which sums to n, then dp[index][n] == None

        dp = [[None for i in range(target + 1)] for num in nums]

        N = len(nums)
        for s in range(1, target + 1):
            if s == nums[0]:
                dp[0][s] = 1

        for index in range(1, N, 1):
            for s in range(1, target + 1):
                # Check dp[index - 1][s], and dp[index - 1][s - nums[index]], and take the best one
                possibilities = []
                if dp[index - 1][s] is not None:
                    possibilities.append(dp[index - 1][s])
                
                if nums[index] == s:
                    possibilities.append(1)

                if s - nums[index] >= 1 and dp[index - 1][s - nums[index]] is not None:
                    possibilities.append(dp[index - 1][s - nums[index]] + 1)

                if possibilities:
                    dp[index][s] = max(possibilities)
        
        if dp[-1][target] is not None:
            return dp[-1][target]
        
        return -1
