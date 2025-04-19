"""
    Question 1545: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

    Just try to use recursion, breaking the problem down to a smaller problem.
"""

class Solution:
    def invert(self, char):
        if char == '1':
            return '0'
        return '1'

    # String S_n has 2**n - 1 characters
    # The number of characters is always odd
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        length = 2 ** n - 1

        if k == length // 2 + 1:
            return '1'

        # If it's in the first half
        if k < length // 2 + 1:
            return self.findKthBit(n - 1, k)
        
        # If it's in the second half
        dist = k - length // 2 - 2
        index = length // 2
        return self.invert(self.findKthBit(n - 1, length // 2 - dist))
