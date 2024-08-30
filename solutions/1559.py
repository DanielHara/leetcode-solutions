"""
Question 1559: https://leetcode.com/problems/detect-cycles-in-2d-grid/description/

    Typical question into how to find a cycle in a graph.
"""

class Solution:
    def DFS(self, row, col, from_to_dict):
        serialized = str(row) + '_' + str(col)
        if serialized in self.visited:
            return False
        
        self.visited.add(serialized)

        neighbors = from_to_dict[serialized]

        while neighbors:
            [neighbor_row, neighbor_col] = neighbors.pop()
            serialized_neighbor = str(neighbor_row) + '_' + str(neighbor_col)
            from_to_dict[serialized_neighbor].remove([row, col])

            if serialized_neighbor in self.visited:
                return True
            
            if self.DFS(neighbor_row, neighbor_col, from_to_dict):
                return True

        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        number_rows = len(grid)
        number_cols = len(grid[0])

        from_to_dict = {}

        for row in range(number_rows):
            for col in range(number_cols):
                serialized = str(row) + '_' + str(col)

                if serialized not in from_to_dict:
                    from_to_dict[serialized] = []

                points = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
                for [point_row, point_col] in points:
                    if point_row >= 0 and point_row < number_rows and point_col >= 0 and point_col < number_cols and grid[point_row][point_col] == grid[row][col]:
                        from_to_dict[serialized].append([point_row, point_col])
        
        self.visited = set()
        for row in range(number_rows):
            for col in range(number_cols):
                if self.DFS(row, col, from_to_dict):
                    return True

        return False
