# Question 2370: https://leetcode.com/problems/longest-ideal-subsequence/

"""
    A nice question. Explore the fact that 0 <= k <= 25, which is quite low.
"""

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        result = 0

        best_possibilities = [0 for i in range(ord('z') - ord('a') + 1)]
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            
            best_possibility = 0

            range_minimum = max(0, ord(char) - k - ord('a'))
            range_maximum = min(ord('z') - ord('a'), ord(char) + k - ord('a'))
            
            for i in range(range_minimum, range_maximum + 1, 1):
                best_possibility = max(best_possibilities[i], best_possibility)
            
            best_possibility = best_possibility + 1
            
            best_possibilities[ord(char) - ord('a')] = best_possibility

            result = max(result, best_possibility)

        return result
