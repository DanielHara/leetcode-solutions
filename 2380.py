# Question 2380: https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

"""
    A trivial, O(N*2) solution is already enough to pass the judge.
"""

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        tokens = list(s)

        result = 0
        finished = False
        
        while not finished:
            finished = True
            i = 0
            while i < len(tokens) - 1:
                if tokens[i] == '0' and tokens[i + 1] == '1':
                    tokens[i] = '1'
                    tokens[i + 1] = '0'
                    finished = False

                    i = i + 2
                else:
                    i = i + 1
        
            if finished:
                return result
        
            result = result + 1

        return result
