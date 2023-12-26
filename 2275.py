# Question 2275: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/d

"""
    Easy, but interesting question. We know each number has at most 24 bits, because 2**24 - 1 > 10**7.
    So, just iterate thorough all numbers 24 times, and get the best amount of candidates which have 1 in the same bit.
"""

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_bit = 24
        
        result = 0
        for index in range(0, max_bit + 1):
            power = 2 ** index

            possibility = 0
            for candidate in candidates:
                if candidate & power > 0:
                    possibility = possibility + 1
            
            result = max(result, possibility)
        
        return result
