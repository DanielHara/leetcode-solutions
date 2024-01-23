# Question 937: https://leetcode.com/problems/reorder-data-in-log-files/

"""
    Really dull question. Basically, just do it.
"""

import functools

class Solution:
    def comparison(self, log1: List[str], log2: List[str]):
        tokens1 = log1.split(' ')
        tokens2 = log2.split(' ')

        if tokens1[1][0].isdigit() and not tokens2[1][0].isdigit():
            return 1
        
        if not tokens1[1][0].isdigit() and tokens2[1][0].isdigit():
            return -1

        if not tokens1[1][0].isdigit() and not tokens2[1][0].isdigit():
            for i in range(1, min(len(tokens1), len(tokens2)), 1):
                if tokens1[i] > tokens2[i]:
                    return 1
                if tokens2[i] > tokens1[i]:
                    return -1
            
            if len(tokens1) > len(tokens2):
                return 1
            
            if len(tokens1) < len(tokens2):
                return -1
            
            if tokens1[0] > tokens2[0]:
                return 1
            
            if tokens1[0] < tokens2[0]:
                return -1
            
            return 0

        return 0
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs.sort(key=functools.cmp_to_key(self.comparison))

        return logs
        
