# Question 2211: https://leetcode.com/problems/count-collisions-on-a-road/description/

"""
    Not a difficult question. Think of the collions as a stack.
"""

class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        result = 0
        for direction in directions:
            if not stack:
                stack.append(direction)
                continue
            
            if stack[-1] == 'S' and direction == 'R':
                stack.append('R')
                continue
            
            if stack[-1] == 'S' and direction == 'L':
                stack.pop()

                while stack and stack[-1] == 'R':
                    stack.pop()
                    result = result + 1

                stack.append('S')
                result = result + 1
                continue
            
            if stack[-1] == 'L' and direction == 'S':
                stack.append('S')
                continue
            
            if stack[-1] == 'R' and direction == 'S':
                stack.pop()

                while stack and stack[-1] == 'R':
                    stack.pop()
                    result = result + 1

                stack.append('S')
                result = result + 1
                continue
            
            if stack[-1] == direction:
                stack.append(direction)
                continue
            
            if stack[-1] == 'R' and direction == 'L':
                result = result + 2
                stack.pop()

                while stack and stack[-1] == 'R':
                    stack.pop()
                    result = result + 1

                stack.append('S')
            else:
                stack.append('R')
        
        return result
