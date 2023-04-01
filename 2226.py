# Question 2226: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/

"""
    Same strategy as that of question 1870
"""

class Solution:
    # Returns true if it's possible to give N candies to each child
    def isPossible(self, N: int, candies: List[int], k: int) -> bool:
        acc = 0
        for candy in candies:
            acc = acc + candy // N
        
        return acc >= k
    
    def binarySearch(self, lower_bound: int, upper_bound: int, candies: List[int], k: int):
        if lower_bound > upper_bound:
            return None
        
        half = (lower_bound + upper_bound) // 2

        if self.isPossible(half, candies, k) and (half == upper_bound or not self.isPossible(half + 1, candies, k)):
            return half
        
        if self.isPossible(half, candies, k):
            return self.binarySearch(half + 1, upper_bound, candies, k)
        
        return self.binarySearch(lower_bound, half - 1, candies, k)


    def maximumCandies(self, candies: List[int], k: int) -> int:
        answer = self.binarySearch(1, max(candies), candies, k)

        if answer is None:
            return 0
        
        return answer
