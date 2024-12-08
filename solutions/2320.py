# Question 2320: https://leetcode.com/problems/count-number-of-ways-to-place-houses/

"""
    A hint to solve this question is that the streets are independent of each other. Therefore,
    solve the question for a street individually, and then just square the number of possibilities for
    an individual street to get the answer.
"""

class Solution:
    def singleStreetPlacement(self, start: int, n: int, dp: List[int]) -> int:
        if start > n:
            return 1

        if start == n:
            return 2
        
        if dp[start] is not None:
            return dp[start]

        mod = 10** 9 + 7
        result = (self.singleStreetPlacement(start + 1, n, dp) + self.singleStreetPlacement(start + 2, n, dp)) % mod
        dp[start] = result
        
        return result
    
    def countHousePlacements(self, n: int) -> int:
        dp = [None for i in range(n + 1)]

        single_street_possibilities = self.singleStreetPlacement(1, n, dp)

        mod = 10** 9 + 7
        return (single_street_possibilities ** 2) % mod
