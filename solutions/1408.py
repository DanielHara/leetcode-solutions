# Question 1408: https://leetcode.com/problems/string-matching-in-an-array/description/

"""
    The trivial solution  gets accepted.
"""

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for index, word in enumerate(words):
            for i in range(len(words)):
                if i != index and word in words[i]:
                    result.append(word)
                    break
    
        return result
