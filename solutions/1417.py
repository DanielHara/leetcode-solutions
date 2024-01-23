# Question 1417: https://leetcode.com/problems/reformat-the-string/

"""
    Trivial question
"""

class Solution:
    def reformat(self, s: str) -> str:
        digits = []
        characters = []

        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                characters.append(char)
        
        if abs(len(digits) - len(characters)) > 1:
            return ''
        
        if len(digits) > len(characters):
            tokens = []
            while digits:
                digit = digits.pop()
                tokens.append(digit)

                if characters:
                    char = characters.pop()
                    tokens.append(char)
            
            return ''.join(tokens)
                
        tokens = []
        while characters:
            char = characters.pop()
            tokens.append(char)

            if digits:
                digit = digits.pop()
                tokens.append(digit)
        
        return ''.join(tokens)
