# Question 1704: https://leetcode.com/problems/determine-if-string-halves-are-alike/

"""
    Trivial question, just do it!
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']

        number_of_vowels_a = 0
        a = s[0:len(s) // 2]
        for char in a:
            lower = char.lower()
            if lower in vowels:
                number_of_vowels_a = number_of_vowels_a + 1

        number_of_vowels_b = 0
        b = s[len(s) // 2:]
        for char in b:
            lower = char.lower()
            if lower in vowels:
                number_of_vowels_b = number_of_vowels_b + 1

        return number_of_vowels_a == number_of_vowels_b
