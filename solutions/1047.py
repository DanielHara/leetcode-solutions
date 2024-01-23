# Question 1047: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

"""
    Fairly trivial question.
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Use a stack to do it!
        
        stack = []
        
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
