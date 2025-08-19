# Question 732: https://leetcode.com/problems/my-calendar-iii/

"""
    Quite interesting question, and that hard. Just store the start and ending points as events (like, start and even events), sort them,
    and get the maximum balance.
"""    

class MyCalendarThree:
    def compare_points(self, point1, point2):
        if point1['time'] != point2['time']:
            return point1['time'] - point2['time']
        
        if point1['point_type'] == 'start' and point2['point_type'] == 'end':
            return 1
        
        if point1['point_type'] == 'end' and point2['point_type'] == 'start':
            return -1
        
        return 0

    def __init__(self):
        self.starting_points = []
        self.ending_points = []

    def book(self, startTime: int, endTime: int) -> int:
        self.starting_points.append({
            'time': startTime,
            'point_type': 'start'
        })
        self.ending_points.append({
            'time': endTime,
            'point_type': 'end'
        })

        points = self.starting_points + self.ending_points
        points.sort(key=functools.cmp_to_key(self.compare_points))

        balance = 0
        result = 0
        for point in points:
            if point['point_type'] == 'start':
                balance = balance + 1
            else:
                balance = balance - 1
            result = max(result, balance)
        
        return result
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)