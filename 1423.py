# Question 1423: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

"""
    Fairly trivial question, just pick n cards on the left and k - n on the right, and iterate on 0 <= n <= k, and
    get the largest result.
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = sum(cardPoints[0: k])
        right = 0
        
        result = max(left, sum(cardPoints[len(cardPoints) - k:]))
        i = k - 1
        while i >= 0:
            result = max(result, left + right)
            
            left = left - cardPoints[i]
            right = right + cardPoints[len(cardPoints) - 1 + i - k + 1]
            
            i = i - 1
        
        return result
