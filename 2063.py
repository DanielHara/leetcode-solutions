# Question 2063: https://leetcode.com/problems/vowels-of-all-substrings/

"""
  Just make S[i] the result considering only the substrings starting at word[i]
"""

class Solution:
    def countVowels(self, word: str) -> int:
        S = [None for i in range(len(word))]

        S[-1] = 1 if word[-1] in ['a', 'e', 'i', 'o', 'u'] else 0

        for i in range(len(word) - 2, -1, -1):
            if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
                S[i] = len(word) - i + S[i + 1]
            else:
                S[i] = S[i + 1]

        return sum(S)
