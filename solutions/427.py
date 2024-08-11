# Question 427: https://leetcode.com/problems/construct-quad-tree/

"""
    An amazingy interesting question!
    I decided to solve this question because I'm studying System Design, and I came across QuadTrees when watching this
    amazing video on designing Uber: https://www.youtube.com/watch?v=lsKU38RKQSo
    It's very useful for optimizing geo-queries.
"""


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def getFull1Sum(self, top_left: List[int], right_bottom: List[int]):
        [top_left_x, top_left_y] = top_left
        [right_bottom_x, right_bottom_y] = right_bottom

        return (right_bottom_y - top_left_y + 1) * (right_bottom_x - top_left_x + 1)

    def getSum(self, top_left: List[int], right_bottom: List[int]):
        [top_left_x, top_left_y] = top_left
        [right_bottom_x, right_bottom_y] = right_bottom

        soma = self.S[right_bottom_x][right_bottom_y]
        if top_left_y - 1 >= 0:
            soma = soma - self.S[right_bottom_x][top_left_y - 1]
        if top_left_x - 1 >= 0:
            soma = soma - self.S[top_left_x - 1][right_bottom_y]
        if top_left_x - 1 >= 0 and top_left_y - 1 >= 0:
            soma = soma + self.S[top_left_x - 1][top_left_y - 1]
        return soma
    
    def buildS(self, grid: List[List[int]]):
        N = len(grid)
        M = len(grid[0])
        
        for i in range(N):
            for j in range(M):
                self.S[i][j] = grid[i][j]

                if i - 1 >= 0:
                    self.S[i][j] = self.S[i][j] + self.S[i - 1][j]
                if j - 1 >= 0:
                    self.S[i][j] = self.S[i][j] + self.S[i][j - 1]
                if i - 1 >= 0 and j - 1 >= 0:
                    self.S[i][j] = self.S[i][j] - self.S[i - 1][j - 1]

    def recursiveConstruct(self, grid: List[List[int]], top_left: List[int], right_bottom: List[int]):
        [top_left_x, top_left_y] = top_left
        [right_bottom_x, right_bottom_y] = right_bottom

        grid_sum = self.getSum(top_left, right_bottom)
        if grid_sum == 0 or grid_sum == self.getFull1Sum(top_left, right_bottom):
            node = Node(grid_sum, True, None, None, None, None)
            return node

        topLeft = self.recursiveConstruct(grid, [top_left_x, top_left_y], [(top_left_x + right_bottom_x) // 2, (top_left_y + right_bottom_y) // 2])
        topRight = self.recursiveConstruct(grid, [(top_left_x + right_bottom_x) // 2 + 1, top_left_y], [right_bottom_x, (top_left_y + right_bottom_y) // 2])
        bottomLeft = self.recursiveConstruct(grid, [top_left_x, (top_left_y + right_bottom_y) // 2 + 1], [(top_left_x + right_bottom_x) // 2, right_bottom_y])
        bottomRight = self.recursiveConstruct(grid, [(top_left_x + right_bottom_x) // 2 + 1, (top_left_y + right_bottom_y) // 2 + 1], [right_bottom_x, right_bottom_y])

        return Node(-1, False, topLeft, bottomLeft, topRight, bottomRight)

    
    def construct(self, grid: List[List[int]]) -> 'Node':
        # grid is a N x M matrix:
        N = len(grid)
        M = len(grid[0])

        self.S = [[0 for i in range(M)] for j in range(N)]

        self.buildS(grid)

        return self.recursiveConstruct(grid, [0,0], [N - 1, M - 1])
