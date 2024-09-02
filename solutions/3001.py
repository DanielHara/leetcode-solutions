# Question 3001: https://leetcode.com/problems/minimum-moves-to-capture-the-queen/

"""
    Just walk from the queen and see you can find a bishop or rook. If you can, return 1, otherwise, return 2
"""


class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        for row in range(e - 1, 0, -1):
            if row == a and b == f:
                return 1
            if row == c and d == f:
                break
        
        for row in range(e + 1, 9, 1):
            if row == a and b == f:
                return 1
            if row == c and d == f:
                break

        for col in range(f - 1, 0, -1):
            if e == a and col == b:
                return 1            
            if e == c and col == d:
                break

        for col in range(f + 1, 9, 1):
            if e == a and col == b:
                return 1            
            if e == c and col == d:
                break
        
        p = 1
        while e + p < 9 and f + p < 9:
            if e + p == c and f + p == d:
                return 1
            if e + p == a and f + p == b:
                break
            
            p = p + 1

        p = 1
        while e - p > 0 and f + p < 9:
            if e - p == c and f + p == d:
                return 1
            if e - p == a and f + p == b:
                break
            
            p = p + 1
        
        p = 1
        while e + p < 9 and f - p > 0:
            if e + p == c and f - p == d:
                return 1
            if e + p == a and f - p == b:
                break
            
            p = p + 1
        
        p = 1
        while e - p > 0 and f - p > 0:
            if e - p == c and f - p == d:
                return 1
            if e - p == a and f - p == b:
                break
            
            p = p + 1
        
        return 2
