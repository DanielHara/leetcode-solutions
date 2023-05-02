# Question 1413: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

"""
    Trivial solution
"""

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        result = nums[0]

        acc = None
        minimum = None
        for num in nums:
            if acc is None:
                acc = num
                minimum = num
            else:
                acc = acc + num
                minimum = min(minimum, acc)
        
        if minimum >= 0:
            return 1
        
        return -1*minimum + 1
