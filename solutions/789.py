# Question 789: https://leetcode.com/problems/escape-the-ghosts/

"""
    Just use a greedy approach: your best chance of reaching the target is going directly to it, and, from the way the ghosts
    can move, it doesn't really matter the way you move, provided you make the smallest possible number of steps.
    And, given you made k steps, just use an efficient way to find out whether you're in reach of a ghost.
"""

class Solution:
    def recursiveEspaceGhosts(self, start, ghosts, target, k):
        [x, y] = start

        for [ghost_x, ghost_y] in ghosts:
            if abs(ghost_x - x) + abs(ghost_y - y) <= k:
                return False

        if target == start:
            return True
        
        [target_x, target_y] = target
        
        factor_x = 1
        if target_x == x:
            factor_x = 0
        elif target_x < x:
            factor_x = -1
        
        factor_y = 1
        if target_y == y:
            factor_y = 0
        elif target_y < y:
            factor_y = -1

        if factor_y != 0:
            return self.recursiveEspaceGhosts([x, y + factor_y], ghosts, target, k + 1)
        
        return self.recursiveEspaceGhosts([x + factor_x, y], ghosts, target, k + 1)
    
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        return self.recursiveEspaceGhosts([0,0], ghosts, target, 0)
