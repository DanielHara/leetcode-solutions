# Question 2929: https://leetcode.com/problems/distribute-candies-among-children-ii/

"""
    Very interesting question, but non-trivial (quite hard, actually). First, come up with a non-optimized solution in O(limit) time, like this:    
"""

class NonOptimizedSolution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0

        for first in range(0, limit + 1):
            if min(n - first, limit) >= max(0, n - limit - first):
                result = result + min(n - first, limit) + 1 - max(0, n - limit - first)

        return result

"""
    Then, see if you can make it optimized by using math. Split up the range(0, limit + 1) in 2 intervals.
    For one of them, you'll have n - first >= limit, and otherwise for the other.
    Then you can simplify the expression and get a sum over a MIN and MAX, which results in a arithmetic progression.
    Use the sum of an arithmetic progression to arrive in an optimized answer.
"""

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0

        MIN = max(0, n - 2 * limit)
        MAX = min(n - limit, limit)
        if MAX >= MIN:
            result = result + (MAX - MIN + 1) * (1 - n + 2 * limit) + (MIN + MAX) * (MAX - MIN + 1) // 2
        
        MIN = max(0, n - limit + 1)
        MAX = min(limit, n)
        if MAX >= MIN:
            result = result + (n + 1) * (MAX - MIN + 1) - (MIN + MAX) * (MAX - MIN + 1) // 2
        
        return result

