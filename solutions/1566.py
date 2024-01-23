# Question 1566: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

"""
    Quite trivial question
"""

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m + 1):
            count = 0
            j = i
            while j + m <= len(arr):
                if arr[j:j+m] != arr[i:i+m]:
                    break
                
                j = j + m
                count = count + 1
                if count == k:
                    return True
            
        return False
