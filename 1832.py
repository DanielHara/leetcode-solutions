# Question 1832: https://leetcode.com/problems/check-if-the-sentence-is-pangram/

"""
    Trivial question
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chart_set = set()

        for char in sentence:
            chart_set.add(char)
        
        for i in range(ord('a'), ord('z') + 1):
            if chr(i) not in chart_set:
                return False
        
        return True
