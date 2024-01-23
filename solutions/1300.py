# Question 1300: https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

# Sorting the array helps! Then the answer came to me naturally.

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()

        N = len(arr)

        S = 0
        result = None
        sum_result = None
        for i in range(0, N):
            possibilities = [(target - S) // (N  - i), 1 + (target - S) // (N  - i), arr[i]]

            for possibility in possibilities:
                if possibility > arr[i] or (i > 0 and possibility < arr[i-1]):
                    continue
                
                if result is None:
                    result = possibility
                    sum_result = S + (N - i) * possibility
                else:
                    if abs(S + (N - i) * possibility - target) < abs(sum_result - target):
                        result = possibility
                        sum_result = S + (N - i) * possibility
                    elif abs(S + (N - i) * possibility - target) == abs(sum_result - target):
                        result = min(result, possibility)
                        sum_result = S + (N - i) * possibility
            
            S = S + arr[i]

        return result
