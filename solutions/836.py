# Question 836: https://leetcode.com/problems/rectangle-overlap/description/

"""
   Trivial question
"""

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        [x1, y1, x2, y2] = rec1
        [a1, b1, a2, b2] = rec2

        return not (x2 <= a1 or a2 <= x1 or y2 <= b1 or b2 <= y1)
