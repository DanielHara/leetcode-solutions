"""
    Question 1362: https://leetcode.com/problems/closest-divisors/

    You don't need to go all the way from num to 0 in trying to find divisors, but trying simply from sqrt(num) to 1
    will already do.
"""

import math

class Solution:
    def closestDivisorPair(self, num: int) -> List[int]:
        ceiling = math.ceil(math.sqrt(num))
        for product in range(ceiling, 0, -1):
            if num % product == 0:
                return [product, num // product]

    def closestDivisors(self, num: int) -> List[int]:
        option1 = self.closestDivisorPair(num + 1)
        option2 = self.closestDivisorPair(num + 2)

        if option1[1] - option1[0] <= option2[1] - option2[0]:
            return option1

        return option2
