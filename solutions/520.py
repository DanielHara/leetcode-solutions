# Question 520: https://leetcode.com/problems/detect-capital/

"""
    Easy warm-up question
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(map(lambda char: char.upper() == char, word)):
            return True

        if word[0].upper() == word[0]:
            return not any(map(lambda char: char.upper() == char, word[1:]))

        return not any(map(lambda char: char.upper() == char, word))
