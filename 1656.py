# Question 1656: https://leetcode.com/problems/design-an-ordered-stream/

"""
    No secret here, easy question
"""

class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.chunks = [None for i in range(n)]
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.chunks[idKey - 1] = value

        tokens = []
        while self.pointer < self.n and self.chunks[self.pointer] is not None:
            tokens.append(self.chunks[self.pointer])
            
            self.pointer = self.pointer + 1
        
        return tokens


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)