# Question 852: https://leetcode.com/problems/peak-index-in-a-mountain-array/

"""
   Just use binary search to do it in O(log N) time
"""

class Solution:
    def binarySearch(self, arr: List[int], i: int, j: int):
        if i > j:
            return None
        
        half = (i + j) // 2

        if half > 0 and half < len(arr) - 1 and arr[half] > arr[half + 1] and arr[half - 1] < arr[half]:
            return half
        
        if half == 0:
            return self.binarySearch(arr, 1, j)
        
        if half == len(arr) - 1:
            return self.binarySearch(arr, i, len(arr) - 2)
        
        if arr[half] < arr[half + 1]:
            return self.binarySearch(arr, half + 1, j)

        return self.binarySearch(arr, i, half - 1)

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.binarySearch(arr, 0, len(arr) - 1)


