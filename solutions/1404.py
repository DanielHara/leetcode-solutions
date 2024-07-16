# Question 1404: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

"""
    One way to do this is just to convert the number to an integer, and just do the steps. As the number is always divided by 2 if it's even,
    it won't take much more than 2 * 500 = 1000 steps to do it in the worst case.
"""

class Solution:
    def numSteps(self, s: str) -> int:
        n = 0
        for index, char in enumerate(s):
            if char == '1':
                n = n + 2 ** (len(s) - 1 - index)
        
        result = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n + 1
            
            result = result + 1

        return result
