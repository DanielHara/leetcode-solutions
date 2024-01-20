# Question 786: https://leetcode.com/problems/k-th-smallest-prime-fraction/

"""
    This brute-force, O(N**2) solution, passes the judge. For a better, O(N * log(N)),
    we could just use the same trick as in questions 668 and 719.
"""

import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                heapq.heappush(heap, (arr[i] / arr[j],  [arr[i], arr[j]]))
        
        for i in range(k - 1):
            heapq.heappop(heap)

        return heap[0][1]
