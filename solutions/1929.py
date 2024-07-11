"""
Question 1929: https://leetcode.com/problems/concatenation-of-array/

What is the question doing on Leetcode? :)
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()

        for num in nums:
            ans.append(num)
        
        return ans
