# Question 733: https://leetcode.com/problems/flood-fill/

"""
Quite easy question, solvable by simple breadth-first search. Quite interesting, though!
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # You can just use a breadth-first search:
        initial_color = image[sr][sc]
        border = [[sr, sc]]

        N = len(image)
        M = len(image[0])

        while border:
            new_border = []

            for [x, y] in border:
                if image[x][y] == color:
                    continue

                image[x][y] = color
                if x - 1 >= 0 and image[x - 1][y] == initial_color:
                    new_border.append([x - 1, y])
                if x + 1 < N and image[x + 1][y] == initial_color:
                    new_border.append([x + 1, y])
                if y - 1 >= 0 and image[x][y - 1] == initial_color:
                    new_border.append([x, y - 1])
                if y + 1 < M and image[x][y + 1] == initial_color:
                    new_border.append([x, y + 1])
            
            border = new_border

        return image
