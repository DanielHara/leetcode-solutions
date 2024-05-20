# Question 2745: https://leetcode.com/problems/construct-the-longest-new-string/

"""
    Very interesting question, not very hard. Just "brute force" it, and use some DP so that the solution doesn't explode exponentially.
"""

class Solution:
    def firstCase(self, x: int, y: int, z: int) -> int:
        if x <= 0:
            return 0

        if y < 0 or z < 0:
            return 0
        
        if self.dp1[x][y][z] is not None:
            return self.dp1[x][y][z]

        result = 2 + self.thirdCase(x - 1, y, z)
        self.dp1[x][y][z] = result
        return result
    
    def secondCase(self, x: int, y: int, z: int) -> int:
        if z <= 0:
            return 0
        
        if x < 0 or y < 0:
            return 0
        
        if self.dp2[x][y][z] is not None:
            return self.dp2[x][y][z]
        
        result = 2 + max(self.firstCase(x, y, z - 1), self.secondCase(x, y, z - 1))
        self.dp2[x][y][z] = result
        return result
    
    def thirdCase(self, x: int, y: int, z: int) -> int:
        if z <= 0:
            return 0

        if x < 0 or y < 0:
            return 0
        
        if self.dp3[x][y][z] is not None:
            return self.dp3[x][y][z]

        result = 2 + max(self.firstCase(x, y - 1, z), self.secondCase(x, y - 1, z))
        self.dp3[x][y][z] = result
        return result

    def longestString(self, x: int, y: int, z: int) -> int:
        # First case: you start with "AA"
        # Then, you must choose "BB"

        # Second case: you start with "AB"
        # Then, you can choose between "AB" and "AA"

        # Third case: you start with "BB"
        # Then, you must choose between "AA", or "AB"

        self.dp1 = [[[None for i in range(z + 1)] for j in range(y + 1)] for k in range(x + 1)]
        self.dp2 = [[[None for i in range(z + 1)] for j in range(y + 1)] for k in range(x + 1)]
        self.dp3 = [[[None for i in range(z + 1)] for j in range(y + 1)] for k in range(x + 1)]

        return max(self.firstCase(x, y, z), self.secondCase(x, y, z), self.thirdCase(x, y, z))
