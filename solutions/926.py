# Question 926: https://leetcode.com/problems/flip-string-to-monotone-increasing/

"""
    Just iterate through all positions in s, and check the number of ones to the left of that position,
    and the number of zeros to the right. These are the positions you'll need to flip if that position were to be where
    monotonically increasing array goes from 0 to 1.
    Then pick the best answer.
"""

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        number_ones = 0
        for char in s:
            if char == '1':
                number_ones = number_ones + 1
        number_zeros = len(s) - number_ones

        result = len(s)

        left_zeros = 0
        left_ones = 0
        for index in range(len(s)):
            # Suppose s[0:index] is made up of zeros, and s[index+1:] is made up of ones
            right_zeros = number_zeros - left_zeros - (1 if s[index] == '0' else 0)

            result = min(result, left_ones + right_zeros)
            
            if s[index] == '0':
                left_zeros = left_zeros + 1
            if s[index] == '1':
                left_ones = left_ones + 1
            
        return result
