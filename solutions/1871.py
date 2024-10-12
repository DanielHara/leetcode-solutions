# Question 1871: https://leetcode.com/problems/jump-game-vii/

"""
    Stunningly interesting question!
    You can use a bit of DP and a sliding window approach to solve it!
"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        self.is_reacheable = [False for char in s]

        zero_indexes_in_sliding_window = set()

        for index in range(minJump, min(maxJump, len(s) - 1) + 1):
            if s[index] == '0':
                zero_indexes_in_sliding_window.add(index)

        self.is_reacheable[0] = True
        for index in range(0, len(s), 1):
            if s[index] == '0' and self.is_reacheable[index]:
                while zero_indexes_in_sliding_window:
                    zero_index = zero_indexes_in_sliding_window.pop()
                    self.is_reacheable[zero_index] = True
            
            if index + maxJump + 1 < len(s):
                zero_indexes_in_sliding_window.add(index + maxJump + 1)
            
            if index + minJump in zero_indexes_in_sliding_window:
                zero_indexes_in_sliding_window.remove(index + minJump)

        return self.is_reacheable[-1]
