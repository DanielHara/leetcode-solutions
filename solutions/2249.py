"""
Question 2249: https://leetcode.com/problems/count-lattice-points-inside-a-circle/
"""

import math

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        point_set = set()

        for [x_center, y_center, r] in circles:
            for x in range(x_center - r, x_center + r + 1):
                y_max = y_center + math.floor(math.sqrt(r ** 2 - (x - x_center)** 2))
                y_min = y_center - math.floor(math.sqrt(r ** 2 - (x - x_center)** 2))
                
                for y in range(y_min, y_max + 1):
                    if (x_center - x) ** 2 + (y_center - y) ** 2 <= r ** 2:
                        point_set.add(str(x) + '_' + str(y))

        return len(point_set)
