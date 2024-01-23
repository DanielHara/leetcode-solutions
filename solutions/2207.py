# Question 2207: https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

"""
    Just do it greedily, not a difficult question
"""

class Solution:
    def getMaximumSubsequenceCount(self, text: str, pattern) -> int:        
        # S[i] is equal to the number of the characters pattern[1] from index >= i

        S = [0 for i in range(len(text))]
        S[-1] = 1 if text[-1] == pattern[1] else 0

        for i in range(len(text) - 2, -1, -1):
            S[i] = S[i + 1] + (1 if text[i] == pattern[1] else 0)
        
        result = 0
        for i in range(0, len(text) - 1, 1):
            if text[i] == pattern[0]:
                result = result + S[i + 1]

        return result

    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        # Do it in a greedy way:

        # First possibility, add pattern[0] to the very beginning of the text
        modified_text = pattern[0] + text

        return max(self.getMaximumSubsequenceCount(pattern[0] + text, pattern), self.getMaximumSubsequenceCount(text + pattern[1], pattern))
