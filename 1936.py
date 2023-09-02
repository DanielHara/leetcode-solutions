# Question 1936: https://leetcode.com/problems/add-minimum-number-of-rungs/

"""
    An easy question, to be really honest.
"""


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        result = 0

        for i in range(len(rungs)):
            distance = rungs[i] - (rungs[i - 1] if i >= 1 else 0)
            if distance > dist:
                if distance % dist > 0:
                    result = result + distance // dist
                else:
                    result = result + distance // dist - 1
        
        return result
