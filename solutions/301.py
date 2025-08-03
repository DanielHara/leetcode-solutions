"""
    Question 301: https://leetcode.com/problems/remove-invalid-parentheses/

    Just try all the possibilities using recursion, actually not that hard :)
    Use DP for the solution not to explode exponentially in time.
"""

class Solution:
    def isBalanced(self, s: str, start: index, end: int) -> bool:
        balance = 0
        for char in s:
            if char == '(':
                balance = balance + 1
            elif char == ')':
                balance = balance - 1
            if balance < 0:
                return False

        return balance == 0

    def recursivelyGetList(self, s: str, start: int, end: int) -> List[str]:
        if start > end:
            return ['']
        
        if start == end:
            if s[start] == '(' or s[start] == ')':
                return ['']
            return [s[start]]
        
        if self.dp[start][end] is not None:
            return self.dp[start][end]
        
        if s[start] != '(' and s[start] != ')':
            recursive_list = self.recursivelyGetList(s, start + 1, end)
            result = []
            for string in recursive_list:
                result.append(s[start] + string)

            self.dp[start][end] = result
            return result
        
        if s[end] != '(' and s[end] != ')':
            recursive_list = self.recursivelyGetList(s, start, end - 1)
            result = []
            for string in recursive_list:
                result.append(string + s[end])
            
            self.dp[start][end] = result
            return result
        
        if s[start] == ')':
            result = self.recursivelyGetList(s, start + 1, end)
            self.dp[start][end] = result
            return result
        
        if s[end] == '(':
            result = self.recursivelyGetList(s, start, end - 1)
            self.dp[start][end] = result
            return result
        
        if self.isBalanced(s, start, end):
            result = [s[start : end + 1]]
            self.dp[start][end] = result
            return result
        
        possibilities = []
        for possibility in self.recursivelyGetList(s, start + 1, end - 1):
            possibilities.append('(' + possibility + ')')

        for index in range(start + 1, end):
            first_parts = self.recursivelyGetList(s, start, index)
            second_parts = self.recursivelyGetList(s, index + 1, end)

            for first_part in first_parts:
                for second_part in second_parts:
                    possibilities.append(first_part + second_part)

        # Get only the strings with maximum length
        max_length = 0
        for possibility in possibilities:
            max_length = max(max_length, len(possibility))
        
        result = set()
        for possibility in possibilities:
            if len(possibility) == max_length:
                result.add(possibility)

        self.dp[start][end] = result
        return list(result)


    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.dp = [[None for col in range(len(s))] for row in range(len(s))]

        return self.recursivelyGetList(s, 0, len(s) - 1)

