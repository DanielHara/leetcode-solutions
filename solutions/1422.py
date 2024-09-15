# Question 1422: https://leetcode.com/problems/maximum-score-after-splitting-a-string/

"""
    Just use some DP. Actually, it wouldn't even have been necessary, because the problem boundaries are quite small:
    2 <= s.length <= 500
"""

class Solution:
    def maxScore(self, s: str) -> int:
        number_zeros_left = []

        for char in s:
            increment = 1 if char == '0' else 0
            number_zeros_left.append(increment + (number_zeros_left[-1] if number_zeros_left else 0))

        number_ones_right = [0 for char in s]
        number_ones_right[-1] = 1 if s[-1] == '1' else 0

        for index in range(len(s) - 2, -1, -1):
            increment = 1 if s[index] == '1' else 0
            number_ones_right[index] = number_ones_right[index + 1] + increment

        result = 0
        for index in range(0, len(s) - 1):
            score_left = number_zeros_left[index]
            score_right = (number_ones_right[index + 1] if index + 1 < len(number_ones_right) else 0)
            score = score_left + score_right

            result = max(result, score)

        return result
