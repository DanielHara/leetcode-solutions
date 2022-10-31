"""
Question 500: https://leetcode.com/problems/keyboard-row/
"""

# Trivial question

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        
        key_to_row_map = {}
        for index, row in enumerate(rows):
            for char in row:
                key_to_row_map[char] = index
        
        result = []
        for el in words:
            word = el.lower()
            row = key_to_row_map[word[0]]
            
            possible = True
            for char in word:
                if key_to_row_map[char] != row:
                    possible = False
                    break
            
            if possible:
                result.append(el)
        
        return result
