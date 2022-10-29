# Question 349: https://leetcode.com/problems/ransom-note/

# Trivial question, just use a frequency dictionary.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency_dict_magazine = {}
        
        for char in magazine:
            frequency_dict_magazine[char] = frequency_dict_magazine.get(char, 0) + 1
        
        for char in ransomNote:
            if frequency_dict_magazine.get(char, 0) <= 0:
                return False
        
            frequency_dict_magazine[char] = frequency_dict_magazine[char] - 1
        
        return True        
        