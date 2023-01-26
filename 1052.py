# Question 1052: https://leetcode.com/problems/grumpy-bookstore-owner/description/

"""
   Not a difficult question. Just see which subarray of length minutes will give you the best number of more customers
   And don't throw away the sums of each subarray, but use it to calculate the next step, so that your solution doesn't become O(N**2).
"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        for i in range(len(grumpy)):
            grumpy[i] = 1 if grumpy[i] == 0 else 0

        # Cover customers[i: i + minutes]

        # Initialize stuff:
        actual = 0
        potential = 0
        for i in range(0, minutes, 1):
            potential = potential + customers[i]
            actual = actual + grumpy[i] * customers[i]

        maximum = potential - actual
        for i in range(0, len(customers) - minutes, 1):
            actual = actual - grumpy[i] * customers[i] + grumpy[i + minutes] * customers[i + minutes]
            potential = potential - customers[i] + customers[i + minutes]

            maximum = max(potential - actual, maximum)

        actual = 0
        for i in range(0, len(customers), 1):
            actual = actual + grumpy[i] * customers[i]

        return maximum + actual
