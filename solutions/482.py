# Question 482: https://leetcode.com/problems/license-key-formatting/

# Trivial question

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = ''.join(s.upper().split('-'))

        number_groups = len(chars) // k
        remainder = len(chars) % k

        tokens = []
        if remainder > 0:
            tokens.append(chars[0: remainder])

        for i in range(number_groups):
            tokens.append(chars[remainder + i * k: remainder + (i + 1) * k])

        return '-'.join(tokens)
