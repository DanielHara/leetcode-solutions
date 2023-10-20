# Question 2833: https://leetcode.com/problems/furthest-point-from-origin/

# Trivial question, do it greedily

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        balance = 0
        blanks = 0

        for move in moves:
            if move == 'L':
                balance = balance + 1
            elif move == 'R':
                balance = balance - 1
            else:
                blanks = blanks + 1

        return blanks + abs(balance)
