"""
    Question 1518: https://leetcode.com/problems/water-bottles/

    Easy, but very well-posed and interesting question!
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        fullBottles = numBottles
        emptyBottles = 0
        
        while fullBottles > 0 or emptyBottles >= numExchange:
            result = result + fullBottles
            emptyBottles = emptyBottles + fullBottles

            fullBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange
        return result
