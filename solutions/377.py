# Question 377: https://leetcode.com/problems/combination-sum-iv/

"""
    Easy question, just DP 101
"""

class Solution:
    def recusiveCombinationSum4(self, target: int) -> int:
        if target < 0:
            return 0

        if target == 0:
            return 1

        if self.dp[target] is not None:
            return self.dp[target]

        result = 0
        for num in self.nums:
            result = result + self.recusiveCombinationSum4(target - num)

        self.dp[target] = result

        return result

    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.nums = nums

        self.dp = [None for _ in range(target + 1)]

        return self.recusiveCombinationSum4(target)

