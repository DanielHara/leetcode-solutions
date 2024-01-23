# Question 1833: https://leetcode.com/problems/maximum-ice-cream-bars/

"""
    Quite trivial question, I'm wondering why it's rated as medium.
"""

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        result = 0
        
        while coins > 0 and costs and costs[0] <= coins:
            coins = coins - costs.pop(0)
            result = result + 1
            
        return result
