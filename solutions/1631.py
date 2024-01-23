"""
Question 1631: https://leetcode.com/problems/path-with-minimum-effort/
"""

"""
After pondering about this question for a long time, trying to figure out some kind of DP solution for it, I just peeked at the hints and
followed them, and TADA!
"""

class Solution:
    # The answer must be between i and j (inclusive), let's binary-search for it:
    def binarySearch(self, i: int, j: int, heights) -> int:
        if i > j:
            return None
        
        half = (i + j) // 2
        
        n_rows = len(heights)
        n_columns = len(heights[0])
        
        exploration = self.exploreGraph((0,0), heights, set(), half)
        if (n_rows - 1, n_columns - 1) in exploration:
            if half == i:
                return half

            exploration = self.exploreGraph((0,0), heights, set(), half - 1)
            
            if (n_rows - 1, n_columns - 1) not in exploration:
                return half

            return self.binarySearch(i, half - 1, heights)

        return self.binarySearch(half + 1, j, heights)

    
    
    # Explores the graph from source (row, column), using edges with cost <= threshold, returns the visited set
    def exploreGraph(self, source, heights, visited, threshold):
        if source in visited:
            return
        
        visited.add(source)
        
        n_rows = len(heights)
        n_columns = len(heights[0])
        
        (i, j) = source
        
        if i + 1 < n_rows and abs(heights[i + 1][j] - heights[i][j]) <= threshold:
            self.exploreGraph((i + 1, j), heights, visited, threshold)
        
        if i - 1 >= 0 and abs(heights[i - 1][j] - heights[i][j]) <= threshold:
            self.exploreGraph((i - 1, j), heights, visited, threshold)
        
        if j + 1 < n_columns and abs(heights[i][j + 1] - heights[i][j]) <= threshold:
            self.exploreGraph((i, j + 1), heights, visited, threshold)
        
        if j - 1 >= 0 and abs(heights[i][j - 1] - heights[i][j]) <= threshold:
            self.exploreGraph((i, j - 1), heights, visited, threshold)
            
        return visited
    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        maximum = 0
        
        n_rows = len(heights)
        n_columns = len(heights[0])
        
        for i in range(n_rows):
            for j in range(n_columns):
                maximum = max(heights[i][j], maximum)
        
        
        return self.binarySearch(0, maximum, heights)
