"""
Question 309: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

    Very interesting question! Make dp[start] the best profit you can get from any number of operations in the array prices[start:]
"""

class Solution:
    def recursiveMaxProfitStartingFrom(self, prices: List[int], start):
        if start < 0 or start >= len(prices):
            return 0
        
        if self.dp[start] is not None:
            return self.dp[start]

        result = 0
        for index in range(start + 1, len(prices)):
            if prices[index] > prices[start]:
                profit = prices[index] - prices[start]
                result = max(result, profit + self.recursiveMaxProfitStartingFrom(prices, index + 2))

            result = max(result, self.recursiveMaxProfitStartingFrom(prices, index))
        
        self.dp[start] = result
        return result

    def maxProfit(self, prices: List[int]) -> int:
        self.dp = [None for price in prices]

        result = 0
        self.recursiveMaxProfitStartingFrom(prices, 0)
        
        return self.dp[0]
