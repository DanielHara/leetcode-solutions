# Question 2845: https://leetcode.com/problems/count-of-interesting-subarrays/

"""
    This is a very interesting question!
    Just keep in mind that (a + b) % mod = ((a % mod) + (b % mod)) % mod, and use some DP.
"""

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        N = len(nums)

        S = [0]
        for num in nums:
            element = S[-1] + (1 if num % modulo == k else 0)
            S.append(element % modulo)

        result = 0
        dp = {0 : 1}
        for index in range(len(nums)):
            key = (S[index + 1] - k) % modulo
            result = result + dp.get(key, 0)

            dp[S[index + 1]] = dp.get(S[index + 1], 0) + 1

        return result
