"""
    Question 2250: https://leetcode.com/problems/count-number-of-rectangles-containing-each-point

    Just take advantage of this constraint: 1 <= hi, yj <= 100
"""

class Solution:
    # Returns that lowest index for which array[index] >= target
    def binarySearch(self, start: int, end: int, array: List[int], target: int):
        if start > end:
            return None

        half = (start + end) // 2

        if array[half] >= target and (half == start or array[half - 1] < target):
            return half
        if array[half] >= target:
            return self.binarySearch(start, half - 1, array, target)
        return self.binarySearch(half + 1, end, array, target)
    

    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        height_2_widths = {}

        for [width, height] in rectangles:
            if height not in height_2_widths:
                height_2_widths[height] = []

            height_2_widths[height].append(width)

        for array in height_2_widths.values():
            array.sort()

        result = []
        for [point_x, point_y] in points:
            current = 0
            for height in range(point_y, 100 + 1):
                widths = height_2_widths.get(height, [])
                # Binary search
                index = self.binarySearch(0, len(widths) - 1, widths, point_x)

                if index is not None:
                    current = current + len(widths) - index
            
            result.append(current)

        return result
