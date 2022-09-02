# Question 2135: https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

# I went for a dynamic progamming approach.
class Solution:
    def isObtainable(self, targetWord: str, startWords_set):
        frequency_dict = {}
        for char in targetWord:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
            
        chars = list(frequency_dict.items())
        chars.sort(key=lambda entry: entry[0])
        
        candidates = list(filter(lambda el: el[1] == 1, chars))
        
        for candidate in candidates:
            letter = candidate[0]
            
            tokens = []
            for [key, value] in chars:
                if key != letter:
                    tokens.append(key + str(value))
            
            if '_'.join(tokens) in startWords_set:
                return True
        
        return False
    
    
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startWords_set = set()
        for word in startWords:
            frequency_dict = {}
            for char in word:
                frequency_dict[char] = frequency_dict.get(char, 0) + 1
                
            chars = list(frequency_dict.items())
            chars.sort(key=lambda entry: entry[0])
            
            tokens = []
            for [key, value] in chars:
                tokens.append(key + str(value))
            
            startWords_set.add('_'.join(tokens))
        
        result = 0
        for targetWord in targetWords:
            if self.isObtainable(targetWord, startWords_set):
                result = result + 1
        
        return result
