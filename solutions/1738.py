# Question 1738: https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

# Do it with dynamic programming. To find out how, just some bit manipuliation will do.

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # matrix is N x M matrix
        N = len(matrix)
        M = len(matrix[0])

        heap = []
        dp = [[None for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                dp[i][j] = matrix[i][j] ^ (dp[i - 1][j] if i >= 1 else 0) ^ (dp[i][j - 1] if j >= 1 else 0) ^ (dp[i - 1][j - 1] if i >= 1 and j >= 1 else 0)
                heapq.heappush(heap, (-1) * dp[i][j])
        
        for i in range(k-1):
            heapq.heappop(heap)

        return (-1) * heap[0]
