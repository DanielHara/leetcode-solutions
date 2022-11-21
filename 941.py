"""
Question 941: https://leetcode.com/problems/valid-mountain-array/
"""

"""
Trivial question, just do it!
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        i = 0
        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i = i + 1
        
        if i + 1 >= len(arr) or i == 0:
            return False
        
        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            i = i + 1
        
        if i + 1 < len(arr):
            return False
        
        return True
