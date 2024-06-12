"""
    Question 2830: https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

    A very interesting question! Just sort the array of [start, end, gold] by start, and use some DP.
"""

class Solution:
    # Returns the index of the first offer for which offers[index] > target.
    # If there's none, returns None
    def binarySearch(self, start, end, offers, target):
        if start > end:
            return None
        
        half = (start + end) // 2

        if offers[half][0] > target and (half == start or offers[half - 1][0] <= target):
            return half
        
        if offers[half][0] > target:
            return self.binarySearch(start, half - 1, offers, target)
        
        return self.binarySearch(half + 1, end, offers, target)
        

    def recursiveMaximizeTheProfit(self, i: int, offers: List[List[int]]):
        n = len(offers)
        
        if i == n - 1:
            return offers[n - 1][2]
        
        if self.dp[i] is not None:
            return self.dp[i]
        
        result = self.recursiveMaximizeTheProfit(i + 1, offers)

        [start, end, gold] = offers[i]

        possibility = offers[i][2]
        j = self.binarySearch(i + 1, n - 1, offers, end)
        if j is not None:
            possibility = possibility + self.recursiveMaximizeTheProfit(j, offers)

        result = max(result, possibility)
        self.dp[i] = result

        return result

    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda offer: offer[0])

        self.dp = [None for i in range(len(offers))]

        return self.recursiveMaximizeTheProfit(0, offers)
