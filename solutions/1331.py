# Question 1331: https://leetcode.com/problems/rank-transform-of-an-array/

"""
    Many ways to do it. Using a heap, for example
"""

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        heap = []

        for index, number in enumerate(arr):
            heapq.heappush(heap, (number, index))
        
        rank = 0
        previous = None
        while heap:
            (number, index) = heapq.heappop(heap)
            
            if previous != number:
                rank = rank + 1
            
            previous = number
            arr[index] = rank
        
        return arr
