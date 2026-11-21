# Question 890: https://leetcode.com/problems/find-and-replace-pattern/

"""
  Quite easy "medium" question, just greedily build a permutation dict for each word. If you mapped a letter already,
  in any of the sides of the bijection, watch out so that you don't do it twice.
"""

class Solution:
    def validate_word(self, word: str, pattern: str) -> bool:
        permutation_dict = {}
        mapped_letters = set()
        for index in range(len(pattern)):
            char = pattern[index]
            if char not in permutation_dict:
                permutation_dict[char] = word[index]
                if word[index] in mapped_letters:
                    return False
                mapped_letters.add(word[index])
            elif permutation_dict[char] != word[index]:
                return False

        return True

    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        result = []
        for word in words:
            if self.validate_word(word, pattern):
                result.append(word)

        return result
