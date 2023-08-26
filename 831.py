# Question 831: https://leetcode.com/problems/masking-personal-information

"""
    A very simple and boring question, which would better be rated as Easy.
"""

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            tokens = s.split('@')

            name = tokens[0].lower()
            domain = tokens[1].lower()

            return name[0] + '*****' + name[-1] + '@' + domain
        
        number_without_separators = ''.join(char for char in s if char.isdigit())

        last_digits = number_without_separators[len(number_without_separators) - 4:]

        if len(number_without_separators) == 10:
            return "***-***-" + last_digits

        if len(number_without_separators) == 11:
            return "+*-***-***-" + last_digits

        if len(number_without_separators) == 12:
            return "+**-***-***-" + last_digits
        
        return "+***-***-***-" + last_digits
