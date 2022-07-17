"""
Question 1619: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
"""

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # Delete the first len(arr) // 20 elements after sorting        
        arr.sort()

        k = len(arr) // 20
        arr = arr[k: len(arr) - k]
       
        return sum(arr) / len(arr)        
