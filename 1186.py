"""
Question 1186: https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

For this question, I got inspired from question https://leetcode.com/problems/maximum-subarray/
I thought I could use the same approach, but instead of just saving the maximum subarray that starts with nums[i]
for each interation, I could save two values: one without deletion and one with deletion, and calculate them
for the whole array.
"""

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        result = arr[-1]
        maximum = arr[-1]
        
        # with each iteration, nums[i] becomes an array: [a, b], where
        # a: sum of maximum subarray with no deletion
        # b: sum of maximum subarray with 1 deletion
        
        N = len(arr)
        
        arr[N - 1] = [arr[N - 1], 0]
        
        for i in range(N - 2, -1, -1):  
            maximum = max(maximum, arr[i])

            [a, b] = arr[i + 1]

            arr[i] = [max(arr[i], arr[i] + a), max(arr[i] + b, a, 0)]
            
            result = max(result, arr[i][0], arr[i][1])
        
        if maximum < 0:
            return maximum
        
        return result
        