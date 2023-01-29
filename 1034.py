# Question 1034: https://leetcode.com/problems/coloring-a-border/description/

"""
   Just find the border by breadth-first search and color it
"""

class Solution:
    def getBorder(self, grid: List[List[int]], row: int, col: int):
        visited = set()

        color = grid[row][col]

        border = [[row, col]]
        result = []
        while border:
            new_border = []

            while border:
                [a, b] = border.pop()
                key = str(a) + '_' + str(b)
                if key in visited:
                    continue

                visited.add(key)
                
                if grid[a][b] == color and (a == 0 or a == len(grid) - 1 or b == 0 or b == len(grid[0]) - 1 or grid[a + 1][b] != color or grid[a - 1][b] != color or grid[a][b + 1] != color or grid[a][b - 1] != color):
                    result.append([a, b])
                
                if a < len(grid) - 1 and grid[a + 1][b] == color:
                    new_border.append([a + 1, b])
                if a > 0 and grid[a - 1][b] == color:
                    new_border.append([a - 1, b])
                if b < len(grid[0]) - 1 and grid[a][b + 1] == color:
                    new_border.append([a, b + 1])
                if b > 0 and grid[a][b - 1] == color:
                    new_border.append([a, b - 1])
            
            border = new_border

        return result
    
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        border = self.getBorder(grid, row, col)

        for [a, b] in border:
            grid[a][b] = color
        
        return grid
        
