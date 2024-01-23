# Question 935: https://leetcode.com/problems/knight-dialer/description/

"""
Do it the naive way, and just use DP by storing the results in a dict so that the solution doesn't explode in time.
"""

class Solution:
    def recursiveKnightDealer(self, initial_position: List[int], n: int):
        mod = 10 ** 9 + 7

        if n == 0:
            return 1

        [i, j] = initial_position

        key = '_'.join([str(i), str(j), str(n)])

        if key in self.results:
            return self.results[key]

        positions = [[i - 2, j - 1], [i - 1, j - 2], [i - 1, j + 2], [i - 2, j + 1], [i + 1, j - 2], [i + 2, j - 1], [i + 2, j + 1], [i + 1, j + 2]]

        result = 0
        for [x, y] in positions:
            if x >= 0 and x <= 3 and y >= 0 and y <= 2 and not (x == 3 and y == 0 or x == 3 and y == 2):
                result = ((result % mod) + (self.recursiveKnightDealer([x, y], n - 1) % mod)) % mod
        
        self.results[key] = result

        return result

    
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7

        self.results = {}

        result = 0
        for x in range(4):
            for y in range(3):
                if x >= 0 and x <= 3 and y >= 0 and y <= 2 and not (x == 3 and y == 0 or x == 3 and y == 2):
                    result = ((result % mod) + (self.recursiveKnightDealer([x, y], n - 1) % mod)) % mod
        
        return result
