"""
Question 1447: https://leetcode.com/problems/simplified-fractions/description/

Uses the trick of converting the fraction to float and using a dict. I think this could fail
for very high values of n, due to rounding errors. But works with the testcase of Leetcode.

"""

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        dict_fractions = {}
        
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                float_number = numerator / denominator

                if float_number not in dict_fractions:
                    dict_fractions[float_number] = str(numerator) + '/' + str(denominator)
        
        return dict_fractions.values()
