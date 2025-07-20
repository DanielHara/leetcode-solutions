"""
    Question 1529: https://leetcode.com/problems/minimum-suffix-flips/description/

    Interesting and quite easy question. Just come from the target from left to right, there's what you have to attack
    first, since the range where you can change the initial string is always [i : n - 1]
"""

class Solution:
    def minFlips(self, target: str) -> int:
        flipped_state = False
        result = 0
        for char in target:
            if (char == '1' and not flipped_state) or (char == '0' and flipped_state):
                result = result + 1
                flipped_state = not flipped_state

        return result
