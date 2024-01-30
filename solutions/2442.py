"""
    Question 2442: https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

    Trivial question, just do it
"""

class Solution:
    def reverseNumber(self, num: int) -> int:
        digits = []

        while num > 0:
            digits.append(num % 10)
            num = num // 10
        
        result = 0
        for index, digit in enumerate(digits):
            result = result + digit * (10 ** (len(digits) - 1 - index))
        
        return result
    
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_set = set()

        for num in nums:
            nums_set.add(num)

        for num in nums:
            nums_set.add(self.reverseNumber(num))

        return len(nums_set)
