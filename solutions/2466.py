"""
Question 2466: https://leetcode.com/problems/count-ways-to-build-good-strings/

This O(N**2) solution using DP, where N = high - low, surprisingly passes the judge. I thought it wouldn't, because 1 <= low <= high <= 10**5,
which are already high numbers.
"""

class Solution:
    def recursiveSountGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        if low <= 0 and high == 0:
            return 1
        
        if low > high:
            return 0
        
        if high <= 0:
            return 0
        
        key = str(low) + '_' + str(high)

        if key in self.dp:
            return self.dp[key]

        if low <= 0:
            result = 1
            if zero <= high:
                result = (result + self.recursiveSountGoodStrings(0, high - zero, zero, one) % mod) % mod
            if one <= high:
                result = (result + self.recursiveSountGoodStrings(0, high - one, zero, one) % mod) % mod
            self.dp[key] = result
            return result

        result = 0
        result = (result + self.recursiveSountGoodStrings(low - zero, high - zero, zero, one) % mod) % mod
        result = (result + self.recursiveSountGoodStrings(low - one, high - one, zero, one) % mod) % mod
        self.dp[key] = result

        return result


    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.dp = {}


        return self.recursiveSountGoodStrings(low, high, zero, one)
