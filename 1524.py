"""
Question 1524: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

    Use DP to do it!

"""

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = [0 for i in range(len(arr))]
        even = [0 for i in range(len(arr))]

        odd[0] = 1 if arr[0] % 2 != 0 else 0
        even[0] = 1 if arr[0] % 2 == 0 else 0
        
        for i in range(1, len(arr)):
            odd[i] = 1 + even[i - 1] if arr[i] % 2 != 0 else odd[i - 1]
            even[i] = 1 + even[i - 1] if arr[i] % 2 == 0 else odd[i - 1]

        return sum(odd) % (10**9 + 7)
