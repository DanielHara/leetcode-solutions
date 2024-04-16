# Question 884: https://leetcode.com/problems/uncommon-words-from-two-sentences/

"""
    Trivial question
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        frequency_dict = {}

        tokens1 = s1.split()
        for word in tokens1:
            frequency_dict[word] = frequency_dict.get(word, 0) + 1
        
        tokens2 = s2.split()
        for word in tokens2:
            frequency_dict[word] = frequency_dict.get(word, 0) + 1

        result = []
        for [word, frequency] in frequency_dict.items():
            if frequency == 1:
                result.append(word)

        return result
