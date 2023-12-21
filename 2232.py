# Question 2232: https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

"""
    Looking at the constraints, I saw: 3 <= expression.length <= 10, so I just brute-forced. It passes the judge, and is
    according to it, this is faster than 100% of accepted solutions :)
"""

class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_index = 0
        while expression[plus_index] != '+':
            plus_index = plus_index + 1
        

        # Just brute-force. Break the expression in 4 parts:
        # expression[0:i]
        # expression[i:plus_index] + expression[plus_index + 1: j]
        # expression[j:]

        best_expression = None
        best_value = None
        for i in range(0, plus_index):
            for j in range(plus_index + 2, len(expression) + 1):
                part1 = int(expression[0: i]) if i > 0 else 1
                part2 = int(expression[i:plus_index]) + int(expression[plus_index + 1: j])
                part3 = int(expression[j:]) if j <= len(expression) - 1 else 1

                candidate = part1 * part2 * part3

                if best_value is None or best_value > candidate:
                    best_value = candidate
                    best_expression = expression[0: i] + '(' + expression[i:plus_index] + '+' + expression[plus_index + 1: j] + ')' + expression[j:]

        return best_expression
