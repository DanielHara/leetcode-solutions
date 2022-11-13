"""
Question 575: https://leetcode.com/problems/distribute-candies/
"""

"""
Just do it greedily, pick 1 candy from each time!
"""

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_set = set()
        
        for candy in candyType:
            candy_set.add(candy)
       
        return min(len(candy_set), len(candyType) // 2)
