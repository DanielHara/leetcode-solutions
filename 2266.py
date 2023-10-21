# Question 2266: https://leetcode.com/problems/count-number-of-texts

"""
    Just use some DP for the solution not to explode in time.
"""

class Solution:
    def recursivePossibilities(self, n_digits: int, n: int) -> int:
        mod = 10**9 + 7

        if n < 0:
            return 0
        
        if n <= 1:
            return 1
        
        key = str(n_digits) + '_' + str(n)

        if key in self.dp:
            return self.dp[key]
        
        result = 0
        for index in range(1, n_digits + 1, 1):
            result = (result + self.recursivePossibilities(n_digits, n - index) % mod) % mod
        
        self.dp[key] = result
        
        return result


    def countTexts(self, pressedKeys: str) -> int:
        i = 0
        
        tokens = []
        while i < len(pressedKeys):
            n_digits = 4 if pressedKeys[i] == '7' or pressedKeys[i] == '9' else 3

            j = i
            while j < len(pressedKeys) and pressedKeys[j] == pressedKeys[i]:
                j = j + 1
            
            tokens.append([n_digits, j - i])
            i = j

        self.dp = {}
        
        mod = 10**9 + 7
        result = 1
        for [n_digits, n] in tokens:
            possibilities = self.recursivePossibilities(n_digits, n)

            result = (result * (possibilities % mod)) % mod
        
        return result
