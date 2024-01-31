# Question 2349: https://leetcode.com/problems/design-a-number-container-system/

"""
    When it says "give me the smallest index", I already suspected there would be a trick to solve this question
    using a heap.
"""

import heapq

class NumberContainers:
    def __init__(self):
        self.dictionary = {}
        self.index_to_number = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            stored_number = self.index_to_number[index]
            self.dictionary[stored_number]['deleted_indexes'].add(index)

        self.index_to_number[index] = number

        if number not in self.dictionary:
            heap = []
            heapq.heappush(heap, index)

            self.dictionary[number] = {
                'heap': heap,
                'deleted_indexes': set()
            }

            return 
        
        entry = self.dictionary[number]
        heap = entry['heap']
        deleted_indexes = entry['deleted_indexes']

        if index in deleted_indexes:
            deleted_indexes.remove(index)
        
        heapq.heappush(heap, index)
        

    def find(self, number: int) -> int:
        if number not in self.dictionary:
            return -1
        
        entry = self.dictionary[number]
        heap = entry['heap']
        deleted_indexes = entry['deleted_indexes']

        while heap:
            if heap[0] not in deleted_indexes:
                return heap[0]
            
            heapq.heappop(heap)

        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)