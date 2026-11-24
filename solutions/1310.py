# Question 1310: https://leetcode.com/problems/xor-queries-of-a-subarray/

"""
    Cool question to remember that A ^ A ^ B = B 
"""

class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        accumulated_xor = []

        for num in arr:
            accumulated_xor.append(num ^ (accumulated_xor[-1] if accumulated_xor else 0))
        
        answer = []
        for query in queries:
            if query[0] == 0:
                answer.append(accumulated_xor[query[1]])
            else:
                answer.append(accumulated_xor[query[1]] ^ accumulated_xor[query[0] - 1])
        
        return answer
