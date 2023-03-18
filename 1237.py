# Question 1237: https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

"""
    A really interesting question! Just use the same approach as binary-search does for a 1D array, and apply
    it for a 2-D matrix!
"""

class Solution:
    # the rectangle a (bottom-left corner), b (top-right) are the boundaries (inclusive)
    def recursiveFindSolution(self, a: List[int], b: List[int], customfunction, z:int):
        if a[0] > b[0]:
            return []
        
        if a[1] > b[1]:
            return []

        half_x = (a[0] + b[0]) // 2
        half_y = (a[1] + b[1]) // 2

        if customfunction.f(half_x, half_y) < z:
            A = self.recursiveFindSolution([a[0], half_y + 1], [half_x, b[1]], customfunction, z)
            B = self.recursiveFindSolution([half_x + 1, a[1]], [b[0], b[1]], customfunction, z)
        
            return A + B
        
        if customfunction.f(half_x, half_y) > z:
            A = self.recursiveFindSolution([a[0], a[1]], [half_x - 1, b[1]], customfunction, z)
            B = self.recursiveFindSolution([half_x, a[1]], [b[0], half_y - 1], customfunction, z)
        
            return A + B
        
        A = self.recursiveFindSolution([half_x + 1, a[1]], [b[0], half_y - 1], customfunction, z)
        B = self.recursiveFindSolution([a[0], half_y + 1], [half_x - 1, b[1]], customfunction, z)

        return A + B + [[half_x, half_y]]

    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        return self.recursiveFindSolution([1,1], [1000,1000], customfunction, z)
