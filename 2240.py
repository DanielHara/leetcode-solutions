# Question 2240: https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

"""
    Another medium question that should actually be rated as easy.
"""

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        pencils_cost = 0

        result = 0
        while pencils_cost <= total:
            result = result + (total - pencils_cost) // cost2 + 1

            pencils_cost = pencils_cost + cost1
        
        return result
