"""
    Question 1710: https://leetcode.com/problems/maximum-units-on-a-truck/

    Easy, but fun question
"""

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)

        filled_capacity = 0
        used_boxes = 0
        for box in boxTypes:
            [number_boxes, size_each_box] = box
            if number_boxes + used_boxes > truckSize:
                return filled_capacity + size_each_box * (truckSize - used_boxes)
            else:
                filled_capacity = filled_capacity + size_each_box * number_boxes
                used_boxes = used_boxes + number_boxes

        return filled_capacity
