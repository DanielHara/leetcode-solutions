# Question 1390: https://leetcode.com/problems/four-divisors/

"""
    Not a difficult question, just remember that you can get the divisors in O(sqrt(N)) time.
"""

import math

class Solution:
    def incrementFourDivisor(self, num):
        root = math.floor(math.sqrt(num))
        if root ** 2 == num:
            return 0

        sum_divisors = 1 + num
        number_divisors = 2
        for i in range(2, root + 1, 1):
            if num % i == 0:
                if number_divisors >= 4:
                    return 0

                sum_divisors = sum_divisors + i + num // i
                number_divisors = number_divisors + 2

        return sum_divisors if number_divisors == 4 else 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result + self.incrementFourDivisor(num)

        return result
