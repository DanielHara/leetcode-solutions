# Question 349: https://leetcode.com/problems/number-of-segments-in-a-string/

# Trivial question

class Solution:
    def countSegments(self, s: str) -> int:
        tokens = s.split(' ')

        return len(list(filter(lambda token: len(token) > 0, tokens)))

