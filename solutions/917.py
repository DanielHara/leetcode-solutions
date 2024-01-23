# Question 917: https://leetcode.com/problems/reverse-only-letters/

"""
Trivial question, just do it!
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        array = list(s)
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            while i < j and not array[i].isalpha():
                i = i + 1
            
            while j > i and not array[j].isalpha():
                j = j - 1
            
            if i < j:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                
            i = i + 1
            j = j - 1
        
        return ''.join(array)
