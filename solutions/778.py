# Question 778: https://leetcode.com/problems/swim-in-rising-water/

"""
Write a function that returns you if it's possible to reach the bottom right corner of the matrix within time T.
Then binary search from 0 to the maximum element in the grid to get tbe answer.
"""

class Solution:
    def recursiveExploreGrid(self, grid: List[List[int]], i: int, j: int):
        if i > len(grid) - 1 or i < 0 or j > len(grid[0]) - 1 or j < 0:
            return False

        if grid[i][j] > self.t:
            return False
        
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return True
        
        if (i, j) in self.visited:
            return False
        
        self.visited[(i, j)] = 1
        
        for el in [[i + 1,j], [i - 1, j], [i, j + 1], [i, j - 1]]:
            if self.recursiveExploreGrid(grid, el[0], el[1]):
                return True
        return False

    def isTimePossible(self, grid: List[List[int]], t: int) -> bool:
        self.t = t        
        self.visited = {}
        
        return self.recursiveExploreGrid(grid, 0, 0)
        
    def binarySearch(self, grid: List[int], i: int, j: int):
        if i > j:
            return None
        
        metade = (i + j) // 2
        
        if self.isTimePossible(grid, metade) and (metade == i or not self.isTimePossible(grid, metade - 1)):
            return metade
        
        if self.isTimePossible(grid, metade):
            return self.binarySearch(grid, i, metade - 1)
        return self.binarySearch(grid, metade + 1, j)
    
    
    def swimInWater(self, grid: List[List[int]]) -> int:
        maximum = 0
        
        for line in grid:
            for num in line:
                maximum = max(maximum, num)
        
        return self.binarySearch(grid, 0, maximum)
