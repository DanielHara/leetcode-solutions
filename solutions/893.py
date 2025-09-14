# Question 893: https://leetcode.com/problems/groups-of-special-equivalent-strings/description/

"""
    Straightforward question. Two strings are special-equivalent if the frequency dicts of their even- and odd-indexed
    chars match. You can get those frequency dicts serialized for fast look-up.
"""

class Solution:
    def getSerializedFrequencyDict(self, frequency_dict):
        tokens = []

        for char_index in range(ord('a'), ord('z') + 1):
            char = chr(char_index)
            tokens.append(char + '_' + str(frequency_dict.get(char, 0)))
        
        return '+'.join(tokens)

    def numSpecialEquivGroups(self, words: List[str]) -> int:
        serialized_set = set()

        for word in words:
            frequency_dict_1 = {}
            frequency_dict_2 = {}
            for index, char in enumerate(word):
                if index % 2 == 0:
                    frequency_dict_1[word[index]] = frequency_dict_1.get(word[index], 0) + 1
                else:
                    frequency_dict_2[word[index]] = frequency_dict_2.get(word[index], 0) + 1
            
            key = self.getSerializedFrequencyDict(frequency_dict_1) + '-' + self.getSerializedFrequencyDict(frequency_dict_2)
            serialized_set.add(key)

        return len(serialized_set)
