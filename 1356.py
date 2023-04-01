"""
Question 1356: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

Trivial question
"""

import functools

def numberOf1s (number: int) -> int:
    result = 0

    while number > 0:
        result = result + (number % 2)
        number = number // 2
    
    return result


def compare_numbers(number1: int, number2: int) -> int:
    if numberOf1s(number1) > numberOf1s(number2):
        return 1
    if numberOf1s(number1) < numberOf1s(number2):
        return -1
    
    if number1 > number2:
        return 1

    return -1

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=functools.cmp_to_key(compare_numbers))

        return arr
