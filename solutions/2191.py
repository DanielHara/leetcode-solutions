# Question 2191: https://leetcode.com/problems/sort-the-jumbled-numbers/

"""
    Quite easy question, just use .sorted with a key parameter.
"""

class Solution:
    def mapNumber(self, number: int, mapping: List[int]) -> int:
        if number == 0:
            return mapping[0]

        reversed_digits = []
        while number > 0:
            reversed_digits.append(number % 10)
            number = number // 10
        
        result = 0
        power = len(reversed_digits) - 1
        while reversed_digits:
            result = result + mapping[reversed_digits.pop()] * 10 ** power
            power = power - 1

        return result

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda num: self.mapNumber(num, mapping))

