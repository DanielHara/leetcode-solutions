"""
    Question 1342: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

    Just a trivial question
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        
        if num % 2 == 0:
            return 1 + self.numberOfSteps(num // 2)

        return 1 + self.numberOfSteps(num - 1)
