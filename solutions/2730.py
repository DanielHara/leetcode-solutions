# Question 2730: https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

"""
    Just use a sliding window
"""

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        start = 0
        end = 0

        result = 0
        repetitions = 0
        while start < len(s):
            while end < len(s) - 1:
                if s[end] == s[end + 1]:
                    if repetitions == 0:
                        repetitions = repetitions + 1
                        end = end + 1
                    else:
                        break
                else:
                    end = end + 1

            if repetitions <= 1:
                result = max(result, end - start + 1)

            if start + 1 < len(s) and s[start] == s[start + 1]:
                repetitions = repetitions - 1

            start = start + 1
        
        return result
