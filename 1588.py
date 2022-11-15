# Question 1588: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

"""
I went straight to the less trivial, O(n) solution. Basically, count how many times each elements happens in the odd-length subarrays.
You have following possibilities.
  1. The element, and an even number of elements in the right of it and in the left of it,
  2. The element, and an odd number of elements in the left of it and in the right of it.
  3. The element, and an even number of elements to its right
  4. The element, and an even number of elements to its left

And then subtract one so that will don't count the same number twice.
That's the O(n) answer!
"""

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        
        for index, num in enumerate(arr):
            factor1 = (index // 2) * ((len(arr) - 1 - index) // 2)
            factor2 = ((len(arr) - 1 - index) - (len(arr) - 1 - index) // 2) * (index - index // 2)
            factor3 = (len(arr) - index - (len(arr) - index) // 2) - 1
            factor4 = (index + 1 - (index + 1) // 2)
            
            factor = factor1 + factor2 + factor3 + factor4            
            
            result = result + num * factor
        
        return result
