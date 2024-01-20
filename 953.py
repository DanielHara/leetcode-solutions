# Question 953: https://leetcode.com/problems/verifying-an-alien-dictionary/

"""
    No secret, just do it. Very nicely written problem, by the way!
"""

class Solution:
    def compare(self, word1, word2, order_dictionary):
        for i in range(len(word1)):
            if i >= len(word2):
                return False
            
            if order_dictionary[word1[i]] > order_dictionary[word2[i]]:
                return False
            
            if order_dictionary[word1[i]] < order_dictionary[word2[i]]:
                return True
        
        return True


    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dictionary = {}

        for index, char in enumerate(order):
            order_dictionary[char] = index

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if not self.compare(word1, word2, order_dictionary):
                return False

        return True
