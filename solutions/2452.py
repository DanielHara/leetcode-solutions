"""
    Question 2452: https://leetcode.com/problems/words-within-two-edits-of-dictionary/

    I had to react with thumbs-down on this question, because this trivial, O(N**3) solution passes the judge.
    As the constraits are low, it does passes the judge. If this is the case, the question should be actually be rated as Easy.
"""

class Solution:
    def match(self, query: str, word: str):
        count = 0

        if len(query) != len(word):
            return False
        
        count = 0
        for i in range(len(query)):
            if word[i] != query[i]:
                count = count + 1
            
            if count >= 3:
                return False
        
        return True

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        
        for query in queries:
            for word in dictionary:
                if self.match(query, word):
                    result.append(query)
                    break

        return result
