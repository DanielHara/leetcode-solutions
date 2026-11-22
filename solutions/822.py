# Question 822: https://leetcode.com/problems/card-flipping-game/

"""
    Easy question - understanding the problem statement is harder than the coding
"""

class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        result = None

        denylist = set()

        for index in range(len(fronts)):
            if fronts[index] == backs[index]:
                denylist.add(fronts[index])
                continue

        for index in range(len(fronts)):
            if fronts[index] not in denylist:
                result = min(result, fronts[index]) if result is not None else fronts[index]
            
            if backs[index] not in denylist:
                result = min(result, backs[index]) if result is not None else backs[index]

        return result if result is not None else 0
