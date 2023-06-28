# Question 1482: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets

"""
    Just use binary search
"""

class Solution:
    def isPossible(self, bloomDay: List[int], m: int, k: int, day: int) -> bool:
        consecutive = 0
        bouquets = 0

        for bloom in bloomDay:
            if day >= bloom:
                consecutive = consecutive + 1
                if consecutive >= k:
                    bouquets = bouquets + 1
                    consecutive = 0
            else:
                consecutive = 0
        return bouquets >= m
    
    def binarySearch(self, bloomDay: List[int], m: int, k: int, i: int, j: int) -> int:
        if i > j:
            return None
        
        half = (i + j) // 2

        if self.isPossible(bloomDay, m, k, half) and (half == i or not self.isPossible(bloomDay, m, k, half - 1)):
            return half
        
        if self.isPossible(bloomDay, m, k, half):
            return self.binarySearch(bloomDay, m, k, i, half - 1)
        
        return self.binarySearch(bloomDay, m, k, half + 1, j)

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        result = self.binarySearch(bloomDay, m, k, 0, max(bloomDay))

        return result if result is not None else -1
