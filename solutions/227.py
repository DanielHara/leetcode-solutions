"""
Question 227: https://leetcode.com/problems/basic-calculator-ii/

    Very interesting, and simple question!
    Keep it simple. Because you don't need to support expressions with parenthesis, you can simply use 2 stacks to first apply multiplication
    and division (which have higher priority), and then addition and subtraction.
    No need to build a post-fixed expression or that kind of complicated stuff
"""


class Solution:
    def add_and_substract(self, tokens):
        stack = []
        for token in tokens:
            if stack and (stack[-1] == '+' or stack[-1] == '-'):
                operand2 = token
                operator = stack.pop()
                operand1 = stack.pop()

                if operator == '+':
                    stack.append(operand1 + operand2)
                else:
                    stack.append(operand1 - operand2)
            else:
                stack.append(token)
        return stack


    def multiply_and_divide(self, tokens):
        stack = []
        for token in tokens:
            if stack and (stack[-1] == '*' or stack[-1] == '/'):
                operand2 = token
                operator = stack.pop()
                operand1 = stack.pop()

                if operator == '*':
                    stack.append(operand1 * operand2)
                else:
                    stack.append(operand1 // operand2)
            else:
                stack.append(token)
        return stack


    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')

        tokens = []
        
        index = 0
        while index < len(s):
            if s[index] == '+' or s[index] == '-' or s[index] == '*' or s[index] == '/':
                tokens.append(s[index])
                index = index + 1
            else:
                end_index = index + 1
                while end_index < len(s) and s[end_index].isdigit():
                    end_index = end_index + 1

                tokens.append(int(s[index: end_index]))
                index = end_index
        
        tokens = self.multiply_and_divide(tokens)
        tokens = self.add_and_substract(tokens)

        return tokens[0]
