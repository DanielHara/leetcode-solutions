# Question 1813: https://leetcode.com/problems/sentence-similarity-iii/

"""
    I cheated in this question and took a look at the second hint, which gives you a really elegant
    way of solving the question.
"""

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        tokens1 = sentence1.split(' ')
        tokens2 = sentence2.split(' ')
        
        if len(tokens1) < len(tokens2):
            temp = tokens1
            tokens1 = tokens2
            tokens2 = temp
        
        # find longest common prefix:
        i = 0
        while i < len(tokens2) and tokens1[i] == tokens2[i]:
            i = i + 1
        
        # the longest common prefix is tokens2[0:i]
        
        # find longest common suffix:
        j = 0
        while j < len(tokens2) and tokens2[len(tokens2) - 1 - j] == tokens1[len(tokens1) - 1 - j]:
            j = j + 1
            
        # the longest common suffix is tokens2[len(tokens2) - 1 - j + 1:]
        
        return i - 1 >= len(tokens2) - 1 - j
        
        