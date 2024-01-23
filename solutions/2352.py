# Question 2352: https://leetcode.com/problems/equal-row-and-column-pairs/

"""
    Actually a fairly simple question. Just use a dict to avoid the solution exploding in time.
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        column_elements_to_frequency = {}

        for col in range(len(grid[0])):
            tokens = []
            for row in range(len(grid)):
                tokens.append(str(grid[row][col]))

            key = '_'.join(tokens)
            column_elements_to_frequency[key] = column_elements_to_frequency.get(key, 0) + 1

        result = 0
        for row in range(len(grid)):
            tokens = []
            for col in range(len(grid[0])):
                tokens.append(str(grid[row][col]))

            key = '_'.join(tokens)
            
            result = result + column_elements_to_frequency.get(key, 0)

        return result
