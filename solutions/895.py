# Question 895: https://leetcode.com/problems/maximum-frequency-stack/

"""
    Very nice question! Just use a heap to keep track of the most frequent element.
    Use a trick with cmp_to_key to make the heap take into account of when the element was pushed, so that
    you can take the one closest to the top of the stack.
"""

from functools import cmp_to_key

class FreqStack:
    def heap_compare(self, e1, e2):
        (freq_1, index_1) = e1
        (freq_2, index_2) = e2

        if freq_1 != freq_2:
            return freq_2 - freq_1

        return index_2 - index_1

    def __init__(self):
        self.heap = []
        self.frequency_dict = {}
        self.index = 0

        self.heap_key_function = cmp_to_key(self.heap_compare)

    def push(self, val: int) -> None:
        self.frequency_dict[val] = self.frequency_dict.get(val, 0) + 1
        freq = self.frequency_dict[val]

        heapq.heappush(self.heap, (self.heap_key_function((freq, self.index)), (freq, self.index, val)))
        self.index = self.index + 1
        
    def pop(self) -> int:
        while self.heap:
            (heap_key, element) = heapq.heappop(self.heap)
            (freq, index, val) = element
        
            if self.frequency_dict.get(val, 0) == freq:
                self.frequency_dict[val] = self.frequency_dict[val] - 1
                return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()