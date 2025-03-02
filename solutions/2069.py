# Question 2069: https://leetcode.com/problems/walking-robot-simulation-ii/

"""
  Just do it! Remember that, as num can be high, you have to keep in mind that running in circles around the grid
  will not make the robot move. Just account for cycles.
"""

class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dir = 'East'
        self.pos = [0, 0]

    def step(self, num: int) -> None:
        while num > 0:
            if num > (2 * (self.width - 1) + 2 * (self.height - 1)) and (self.pos == [0, 0] and self.dir == 'East'):
                num = num % (2 * (self.width - 1) + 2 * (self.height - 1))
                if num == 0:
                    self.dir = 'South'

            if self.dir == 'East':
                x = self.pos[0]
                steps = min(self.width - 1 - x, num)
                self.pos[0] = x + steps
                num = num - steps
                if num > 0:
                    self.dir = 'North'
            elif self.dir == 'North':
                y = self.pos[1]
                steps = min(self.height - 1 - y, num)
                self.pos[1] = y + steps
                num = num - steps
                if num > 0:
                    self.dir = 'West'
            elif self.dir == 'West':
                x = self.pos[0]
                steps = min(x, num)
                self.pos[0] = x - steps
                num = num - steps
                if num > 0:
                    self.dir = 'South'
            elif self.dir == 'South':
                y = self.pos[1]
                steps = min(y, num)
                self.pos[1] = y - steps
                num = num - steps
                if num > 0:
                    self.dir = 'East'



    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()