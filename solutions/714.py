# Question 714: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

"""
    Very interesting DP problem! I could come out with O(N**2) solution similar to question 309 (https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/),
    but which didn't pass the judge, because 1 <= prices.length <= 5 * 10**4
    I had to look at the hints to come up with this solution.
"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp1 = [None for price in prices]
        dp2 = [None for price in prices]

        dp1[0] = (-1) * prices[0]
        dp2[0] = 0

        for price_index in range(1, len(prices)):
            dp1[price_index] = max(dp1[price_index - 1], dp2[price_index - 1] - prices[price_index])
            dp2[price_index] = max(dp2[price_index - 1], dp1[price_index - 1] + prices[price_index] - fee)
        
        return max(dp1[-1], dp2[-1])
