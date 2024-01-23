# Question 1937: https://leetcode.com/problems/maximum-number-of-points-with-cost/

"""
  There is an obvious solution that is O(n*3), where n is max(len(points), len(points[0])). I thought it coould be enough, implemented it,
  and got a timeout. Then I gave up on the question and tried again after 2 days, and could come up with a tricky O(n*2) solution.
"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        
        results = [[None for i in range(m)] for j in range(n)]
        
        for i in range(m):
            results[0][i] = points[0][i]
        
        for i in range(1, n):
            results[i][0] = results[i - 1][0] + points[i][0]
            for j in range(1, m):
                results[i][j] = max(results[i - 1][j] + points[i][j], results[i][j - 1] - 1 - points[i][j - 1] + points[i][j])
            
            results[i][m - 1] = max(results[i][m - 1], results[i-1][m - 1] + points[i][m - 1])
            for j in range(m - 2, -1, -1):
                results[i][j] = max(results[i-1][j] + points[i][j], results[i][j + 1] - 1 - points[i][j+1] + points[i][j], results[i][j])
        
        return max(results[n - 1])
