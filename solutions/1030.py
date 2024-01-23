"""
Question 1030: https://leetcode.com/problems/matrix-cells-in-distance-order/
"""

"""
   Trivial question 
"""
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        array = []
        for i in range(rows):
            for j in range(cols):
                array.append([i, j])

        array.sort(key=lambda coordinate: abs(coordinate[0] - rCenter) + abs(coordinate[1] - cCenter))

        return array
