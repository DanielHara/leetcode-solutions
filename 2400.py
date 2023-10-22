"""
Question 2400: https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

    Just use some DP to do it
"""

class Solution:
    # Returns, recursively, and with use of DP, the number of different ways to
    # reach position diff from position 0, in exactly k steps
    def recursiveNumberOfWays(self, diff: int, k: int) -> int:
        mod = 10**9 + 7
        if k <= 0:
            return 1 if diff == 0 else 0
        
        key = str(diff) + '_' + str(k)

        if key in self.dp:
            return self.dp[key]
        
        result = ((self.recursiveNumberOfWays(diff - 1, k - 1) % mod) + (self.recursiveNumberOfWays(diff + 1, k - 1) % mod)) % mod
        self.dp[key] = result

        return result

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        self.dp = {}
        
        diff = endPos - startPos

        return self.recursiveNumberOfWays(diff, k)
