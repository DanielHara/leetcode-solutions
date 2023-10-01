"""
Question 2100: https://leetcode.com/problems/find-good-days-to-rob-the-bank/

Just a little bit of DP is enought to solve this question
"""

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        N = len(security)

        S = [None for i in range(N)]
        S[-1] = 0

        for i in range(N - 2, -1, -1):
            if security[i] <= security[i + 1]:
                S[i] = 1 + S[i + 1]
            else:
                S[i] = 0
        
        T = [None for i in range(N)]
        T[0] = 0

        for i in range(1, N, 1):
            if security[i - 1] >= security[i]:
                T[i] = 1 + T[i - 1]
            else:
                T[i] = 0
        
        result = []
        for i in range(N):
            if S[i] >= time and T[i] >= time:
                result.append(i)
        
        return result
