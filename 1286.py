# Question 1286: https://leetcode.com/problems/iterator-for-combination/

"""
    Looking at the constraints: 1 <= combinationLength <= characters.length <= 15, I noticed that,
    becazse 2**15 = 32768, just brute-forcing it would pass the judge. And indeed it does!
"""

class CombinationIterator:
    def getAllCombinations(self, characters: str, combinationLength: int):
        if combinationLength == 0:
            return [[]]
        
        if len(characters) < combinationLength:
            return []
        
        result = self.getAllCombinations(characters[1:], combinationLength - 1)
        for v in result:
            v.append(characters[0])
        
        result = result + self.getAllCombinations(characters[1:], combinationLength)

        return result
    
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = self.getAllCombinations(characters, combinationLength)
        self.index = 0

    def next(self) -> str:
        result = ''.join(reversed(self.combinations[self.index]))
        self.index = self.index + 1

        return result

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()