# Question 676: https://leetcode.com/problems/implement-magic-dictionary/

"""
    Looks like simple brute-force passes the judge. I suspect you could also use a trie to optimize it.
"""

class MagicDictionary:
    def __init__(self):
        self.mapLengthToWord = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            if len(word) not in self.mapLengthToWord:
                self.mapLengthToWord[len(word)] = []
            
            self.mapLengthToWord[len(word)].append(word)

    def compareWord(self, word: str, searchWord: str) -> bool:
        changed = False
        for i in range(len(searchWord)):
            if searchWord[i] != word[i]:
                if changed:
                    return False

                changed = True
        
        return changed


    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.mapLengthToWord:
            return False

        for word in self.mapLengthToWord[len(searchWord)]:
            for i in range(len(searchWord)):
                if self.compareWord(word, searchWord):
                    return True
                    
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)