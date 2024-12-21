# Question 2787: https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

"""
    Just a modified version of the knapsack problem of question 2915
"""

import math

class Solution:
    # Use an approach similar to the backpack problem
    def numberOfWays(self, n: int, x: int) -> int:
        nums = []
        for num in range(1, math.ceil(math.pow(n, 1/x)) + 1):
            nums.append(num ** x)
        
        target = n
        dp = [[0 for i in range(target + 1)] for num in nums]

        N = len(nums)
        for s in range(1, target + 1):
            if s == nums[0]:
                dp[0][s] = 1

        for index in range(1, N, 1):
            for s in range(1, target + 1):
                dp[index][s] = dp[index - 1][s]

                if nums[index] == s:
                    dp[index][s] = dp[index][s] + 1

                if s - nums[index] >= 1:
                    dp[index][s] = dp[index][s] + dp[index - 1][s - nums[index]]

        return dp[-1][target] % (10**9 + 7)
