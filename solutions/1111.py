# Question 1111: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

"""
   Very interesting question, just do it greedily.
   Actually, you don't need to keep 2 stacks, just the count of the '('.
   I just did it because it made it get the solution come to my mind faster.
"""

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack1 = []
        stack2 = []

        answer = [None for i in range(len(seq))]

        for index, char in enumerate(seq):
            if char == '(':
                if len(stack1) < len(stack2):
                    answer[index] = 0
                    stack1.append(index)
                else:
                    answer[index] = 1
                    stack2.append(index)
            if char == ')':
                if len(stack1) > len(stack2):
                    answer[index] = 0
                    stack1.pop()
                else:
                    answer[index] = 1
                    stack2.pop()
        return answer
