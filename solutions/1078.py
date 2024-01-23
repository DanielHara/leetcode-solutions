# Question 1078: https://leetcode.com/problems/occurrences-after-bigram/

"""
   Trivial question
"""

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        tokens = text.split(' ')

        result = []
        for i in range(0, len(tokens) - 2):
            if tokens[i] == first and tokens[i + 1] == second:
                result.append(tokens[i + 2])

        return result
