# Question 1839: https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

"""
    Not a difficult question, just accumulate the input as objects with 'char' and 'count' so that
    the job gets easier.
"""

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        array = []

        i = 0
        while i < len(word):
            j = i + 1
            while j < len(word) and word[j] == word[i]:
                j = j + 1

            array.append({
                'char': word[i],
                'count': j - i
            })
            
            i = j 

        result = 0
        for i in range(0, len(array) - 4):
            if array[i]['char'] == 'a' and array[i + 1]['char'] == 'e' and array[i + 2]['char'] == 'i' and array[i + 3]['char'] == 'o' and array[i + 4]['char'] == 'u':
                result = max(result, array[i]['count'] + array[i + 1]['count'] + array[i + 2]['count'] + array[i + 3]['count'] + array[i + 4]['count'])
        
        return result
