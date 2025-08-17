# Question 188: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

"""
    Very interesting question! Do the same as the other questions about buying and selling stock and create
    2 dp matrices: one for the situation you have the stock, and another for the situation you don't have it.
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dps = []
        for _ in range(k + 1):
            # Having the stock:
            dp1 = [0 for price in prices]
            # Not having the stock:
            dp2 = [0 for price in prices]
            dps.append([dp1, dp2])

        # dps[k] is the dp for having completed at most k operations
        for completed_operations in range(1, k + 1):
            dps[completed_operations][0][0] = (-1) * prices[0]
            dps[completed_operations][1][0] = 0
        
        for prices_index in range(1, len(prices)):
            for completed_operations in range(1, k + 1):
                maximum_previous_not_having_the_stock = dps[completed_operations - 1][1][prices_index - 1]
                maximum_previous_having_the_stock = dps[completed_operations][0][prices_index - 1]

                dps[completed_operations][0][prices_index] = max(maximum_previous_not_having_the_stock - prices[prices_index], maximum_previous_having_the_stock)

                maximum_previous_not_having_the_stock = dps[completed_operations][1][prices_index - 1]
                maximum_previous_having_the_stock = dps[completed_operations][0][prices_index - 1]

                dps[completed_operations][1][prices_index] = max(maximum_previous_not_having_the_stock, maximum_previous_having_the_stock + prices[prices_index])


        return max(dps[k][0][-1], dps[k][1][-1])
