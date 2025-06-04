# Question 365: https://leetcode.com/problems/water-and-jug-problem/

"""
    Just use depth-first search to find out which states you can reach, and see if any of them
    contains an amount of water equal to target.
"""

class Solution:
    def depthFirstSearch(self, start_x: int, start_y: int):
        if start_x < 0 or start_x > self.x or start_y < 0 or start_y > self.y:
            return

        key = str(start_x) + '_' + str(start_y)
        if key in self.visited:
            return

        self.visited.add(key)

        if start_x < self.x:
            self.depthFirstSearch(self.x, start_y)
        if start_y < self.y:
            self.depthFirstSearch(start_x, self.y)
        if start_y > 0:
            self.depthFirstSearch(start_x, 0)
        if start_x < 0:
            self.depthFirstSearch(0, start_y)

        if start_x > 0 and start_y < self.y:
            amount = min(start_x, self.y - start_y)
            self.depthFirstSearch(start_x - amount, start_y + amount)

        if start_y > 0 and start_x < self.x:
            amount = min(start_y, self.x - start_x)
            self.depthFirstSearch(start_x + amount, start_y - amount)

    
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        self.x = x
        self.y = y

        self.visited = set()

        self.depthFirstSearch(0, 0)

        for t in range(0, target + 1):
            key = str(t) + '_' + str(target - t)
            if key in self.visited:
                return True
        
        return False
