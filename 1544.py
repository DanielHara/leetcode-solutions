"""
Question 1544: https://leetcode.com/problems/make-the-string-great

Trivial question
"""

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if (stack and stack[-1].lower() == char.lower() and (stack[-1].islower() and char.isupper() or stack[-1].isupper() and char.islower())):
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
