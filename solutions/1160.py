# Question 1160: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

"""
    Trivial question
"""

class Solution:
    def canForm(self, word: str, frequency_dict_chars: Dict[str, int]) -> bool:
        word_frequency_dict = {}
        for char in word:
            word_frequency_dict[char] = word_frequency_dict.get(char, 0) + 1
        
        for [char, frequency] in word_frequency_dict.items():
            if frequency > frequency_dict_chars.get(char, 0):
                return False
        return True
    
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        frequency_dict_chars = {}
        for char in chars:
            frequency_dict_chars[char] = frequency_dict_chars.get(char, 0) + 1
        
        result = 0
        for word in words:
            if self.canForm(word, frequency_dict_chars):
                result = result + len(word)
        return result
