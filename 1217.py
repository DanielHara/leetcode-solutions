# Question 1217: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

"""
    A really interesting question! If the diffenrence in positions two elements is 2, there is no cost of moving them.
    Take 0, 2, 4, ..., as ths "free road" and then compute how many odd numbers there are. You'll need to pay 1 for each.
    Take 1, 3, 5, ..., as ths "free road" and then compute how many even numbers there are. You'll need to pay 1 for each.
    Then, choose the minimum.
"""

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = 0
        for element in position:
            if element % 2 == 1:
                odds = odds + 1
        
        return min(odds, len(position) - odds)
