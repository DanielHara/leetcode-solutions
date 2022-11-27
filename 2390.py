"""
Question 2390: https://leetcode.com/problems/removing-stars-from-a-string/

Quite easy question
"""

class Solution:
    def removeStars(self, s: str) -> str:
        # Use a stack to do it!
        
        stack = []
        
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
