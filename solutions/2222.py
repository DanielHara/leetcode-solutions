# Question 2222: https://leetcode.com/problems/number-of-ways-to-select-buildings/

"""
    This is a very interesting question! You can use some DP to solve it
"""

class Solution:
    def numberOfWays(self, s: str) -> int:
        N = len(s)
        S = [None for i in range(N)]

        number_zeros = 0
        number_ones = 0
        for i in range(N - 1, -1, -1):
            if s[i] == '1':
                S[i] = number_zeros
            else:
                S[i] = number_ones

            if s[i] == '0':
                number_zeros = number_zeros + 1
            else:
                number_ones = number_ones + 1

        T = [0 for i in range(N)]
        last_zeros_sum = 0
        last_ones_sum = 0
        for i in range(N - 1, -1, -1):
            if s[i] == '0':
                T[i] = T[i] + last_ones_sum
                last_zeros_sum = last_zeros_sum + S[i]
            else:
                T[i] = T[i] + last_zeros_sum
                last_ones_sum = last_ones_sum + S[i]
        
        return sum(T)
