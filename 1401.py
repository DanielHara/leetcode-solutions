# Question 1401: https://leetcode.com/problems/circle-and-rectangle-overlapping/

"""
    I approached this question like in geometry at school. See the value of x in the rectangle which is closest to the center of the circle.
    This is the best chance of finding an intersection. Then find if there's an intersection of the y values.
"""

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = None
        
        if x1 <= xCenter and xCenter <= x2:
            x = xCenter
        elif x1 >= xCenter:
            x = x1
        else:
            x = x2
        
        if radius**2 - (x - xCenter) **2 < 0:
            return False
        
        return max(yCenter - math.sqrt(radius**2 - (x - xCenter) **2), y1) <= min(yCenter + math.sqrt(radius**2 - (x - xCenter) **2), y2)
