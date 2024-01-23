# Question 1638: https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

# I went for a dynamic progamming approach.
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)
        
        # P[i][j] is the length of the longest string which is equal and begins on s[i] and t[j]
        P = [[None for i in range(M)] for j in range(N)]
        
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if s[i] == t[j]:
                    P[i][j] = 1 + (P[i + 1][j + 1] if (i + 1 < N and j + 1 < M) else 0)
                else:
                    P[i][j] = 0
                    
        Q = [[None for i in range(M)] for j in range(N)]
        for i in range(0, N, 1):
            for j in range(0, M, 1):
                if s[i] == t[j]:
                    Q[i][j] = 1 + (Q[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0)
                else:
                    Q[i][j] = 0
        
        result = 0
        for i in range(N):
            for j in range(M):
                if s[i] != t[j]:
                    left = P[i+1][j+1] if (i + 1 < N and j + 1 < M) else 0
                    right = Q[i - 1][j - 1] if (i - 1 >= 0 and j - 1 >= 0) else 0
                    result = result + (left + 1)* (right + 1)
        
        return result
