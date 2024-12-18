# Question 1844: https://leetcode.com/problems/replace-all-digits-with-characters/

"""
    Just a trivial, warm-up question
"""

class Solution:
    def replaceDigits(self, s: str) -> str:
        tokens = [char for char in s]

        for index in range(len(tokens)):
            if index % 2 == 1:
                tokens[index] = chr(ord(tokens[index - 1]) + int(tokens[index]))
        
        return ''.join(tokens)
