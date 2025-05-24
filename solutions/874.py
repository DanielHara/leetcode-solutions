"""
    Question 874: https://leetcode.com/problems/walking-robot-simulation/

    As the contraints for k are low: 1 <= k <= 9, a trivial solution is enough, without many optimizations.
    Just don't forget to serialize the obstacles and put them into a set, so that you can check in O(1) time
    if a (x, y) position is occupied by an obstacle.
"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set()
        for [x, y] in obstacles:
            key = str(x) + '_' + str(y)
            obstacle_set.add(key)

        direction = 'north'

        position_x = 0
        position_y = 0

        result = 0
        for command in commands:
            if command == -2:
                if direction == 'north':
                    direction = 'west'
                elif direction == 'west':
                    direction = 'south'
                elif direction == 'south':
                    direction = 'east'
                elif direction == 'east':
                    direction = 'north'
            elif command == -1:
                if direction == 'north':
                    direction = 'east'
                elif direction == 'east':
                    direction = 'south'
                elif direction == 'south':
                    direction = 'west'
                elif direction == 'west':
                    direction = 'north'
            else:
                for step in range(command):
                    if direction == 'north':
                        key = str(position_x) + '_' + str(position_y + 1)
                        if key not in obstacle_set:
                            position_y = position_y + 1
                        else:
                            break
                    
                    elif direction == 'east':
                        key = str(position_x + 1) + '_' + str(position_y)
                        if key not in obstacle_set:
                            position_x = position_x + 1
                        else:
                            break

                    elif direction == 'south':
                        key = str(position_x) + '_' + str(position_y - 1)
                        if key not in obstacle_set:
                            position_y = position_y - 1
                        else:
                            break

                    elif direction == 'west':
                        key = str(position_x - 1) + '_' + str(position_y)
                        if key not in obstacle_set:
                            position_x = position_x - 1
                        else:
                            break
                    
                    result = max(result, position_x ** 2 + position_y ** 2)
        
        return result
