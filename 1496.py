"""
Question 1496: https://leetcode.com/problems/path-crossing/

    Quite interesting question
"""


class Solution:
    def getSerializedPoint(self, point: List[int]) -> str:
        return str(point[0]) + '_' + str(point[1])

    def isPathCrossing(self, path: str) -> bool:
        location = [0, 0]
        visited_set = set()
        visited_set.add(self.getSerializedPoint(location))

        for direction in path:
            if direction == 'N':
                location[0] = location[0] + 1
            elif direction == 'S':
                location[0] = location[0] - 1
            elif direction == 'E':
                location[1] = location[1] + 1
            else:
                location[1] = location[1] - 1

            serialized_location = self.getSerializedPoint(location)
            if serialized_location in visited_set:
                return True

            visited_set.add(serialized_location)

        return False
