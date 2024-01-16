"""
    Question 2559: https://leetcode.com/problems/count-vowel-strings-in-ranges/
    
    No secret about this question, just use prefix sum to do it.
"""

class Solution:
    def isVowel(self, char: str) -> bool:
        return char in ['a', 'e', 'i', 'o', 'u']


    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        start_and_end_with_vowel_array = []

        for word in words:
            start_and_end_with_vowel_array.append(1 if self.isVowel(word[0]) and self.isVowel(word[-1]) else 0)
        
        S = []

        for el in start_and_end_with_vowel_array:
            S.append(el + (S[-1] if S else 0))

        result = []

        for [begin, end] in queries:
            result.append(S[end] - (S[begin - 1] if begin >= 1 else 0))

        return result
