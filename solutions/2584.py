"""
    Question 2587: https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

    Quite easy question, just do it greedily.
"""

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        prefix = []
        for num in nums:
            prefix.append(num + (prefix[-1] if prefix else 0))

        result = 0
        for num in prefix:
            if num > 0:
                result = result + 1
            else:
                return result

        return result
