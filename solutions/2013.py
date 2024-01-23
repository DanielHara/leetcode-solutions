# Question 2013: https://leetcode.com/problems/detect-squares/

"""
    Just use some maps to look up data in O(1) time.
"""


class DetectSquares:
    def __init__(self):
        self.x_2_y = {}
        self.y_2_x = {}
        self.total_points_frequency = {}

    def serialize_point(self, point: List[int]) -> str:
        [x, y] = point
        
        return str(x) + '_' + str(y)    

    def add(self, point: List[int]) -> None:
        [x, y] = point
        if x not in self.x_2_y:
            self.x_2_y[x] = []    
        self.x_2_y[x].append(y)

        if y not in self.y_2_x:
            self.y_2_x[y] = []
        self.y_2_x[y].append(x)

        serialized_point = self.serialize_point(point)
        self.total_points_frequency[serialized_point] = self.total_points_frequency.get(serialized_point, 0) + 1
    
    def count(self, point: List[int]) -> int:
        [x, y] = point

        # Look at the points on the same x axis:
        y_positions = self.x_2_y.get(x, [])

        result = 0
        for y_position in y_positions:
            d = y - y_position
            if d == 0:
                continue

            point_1 = self.serialize_point([x + d, y])
            point_2 = self.serialize_point([x + d, y_position])
            
            result = result + self.total_points_frequency.get(point_1, 0) * self.total_points_frequency.get(point_2, 0)

            point_1 = self.serialize_point([x - d, y])
            point_2 = self.serialize_point([x - d, y_position])
            
            result = result + self.total_points_frequency.get(point_1, 0) * self.total_points_frequency.get(point_2, 0)
        
        return result


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)