# Question 1897: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

"""
    Trivial question. Just put all characters in one basket and count if the frequency of every character
    is a multiple of the number of words.
"""

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)

        frequency_dict = {}
        for word in words:
            for char in word:
                frequency_dict[char] = frequency_dict.get(char, 0) + 1

        for frequency in frequency_dict.values():
            if frequency % n != 0:
                return False

        return True
