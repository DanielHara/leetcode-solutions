# Question 1816: https://leetcode.com/problems/truncate-sentence/

"""
    Trivial question
"""

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(' ')

        return ' '.join(words[0:k])
