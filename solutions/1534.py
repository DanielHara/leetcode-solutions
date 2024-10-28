"""
    Question 1534: https://leetcode.com/problems/count-good-triplets/

    As the bounds are low: 3 <= arr.length <= 100, brute-force is just enough.
"""

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0

        N = len(arr)
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        result = result + 1

        return result
