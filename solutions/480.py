# Question 480: https://leetcode.com/problems/sliding-window-median/

"""
    Very interesting, but quite hard question :)
    Use 2 heaps so that you can insert, delete and read the median in an efficient way. Use a max heap to store the numbers
    in the first half of the sorted array (and the median itself, if the array had an odd size),
    and use a min heap to store the numbers in the second half of the sorted array.

    Use lazy-deletion to delete from the heaps, and just read from the top of the heaps to get the medians.
    When inserting into the heaps, be sure to keep them balanced, i.e., the top element of the max-heap should always the <= the top element of the min-heap,
    and the size if the max-heap should always be min_heap.size() or  min_heap.size() + 1.
    If any of these conditions isn't fulfilled, move elements around so that they are fulfilled.
"""

import heapq

class Heap:
    def __init__(self, is_max_heap):
        self.heap = []
        self.frequency_dict = {}
        self.size = 0
        self.is_max_heap = is_max_heap
    
    def push(self, val):
        if self.is_max_heap:
            heapq.heappush(self.heap, (-val, val))
        else:
            heapq.heappush(self.heap, (val, val))

        self.frequency_dict[val] = self.frequency_dict.get(val, 0) + 1
        self.size = self.size + 1

    def delete(self, val):
        if self.frequency_dict.get(val, 0) == 0:
            return

        self.frequency_dict[val] = self.frequency_dict[val] - 1
        if self.frequency_dict[val] == 0:
            del self.frequency_dict[val]

        self.size = self.size - 1

    def includes(self, val):
        return self.frequency_dict.get(val, 0) > 0
    
    def get_size(self):
        return self.size

    def pop(self):
        while self.heap and self.heap[0][1] not in self.frequency_dict:
            heapq.heappop(self.heap)

        if not self.heap:
            return None

        top = heapq.heappop(self.heap)[1]

        self.frequency_dict[top] = self.frequency_dict[top] - 1
        if self.frequency_dict[top] == 0:
            del self.frequency_dict[top]

        self.size = self.size - 1

        return top

    def top(self):
        while self.heap and self.heap[0][1] not in self.frequency_dict:
            heapq.heappop(self.heap)
        
        if self.heap:
            return self.heap[0][1]
            
        return None


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        min_heap = Heap(False)
        max_heap = Heap(True)

        for i in range(k):
            max_heap.push(nums[i])

            # Rebalance
            while min_heap.get_size() > 0 and max_heap.get_size() > 0 and max_heap.top() > min_heap.top():
                popped_val = max_heap.pop()
                min_heap.push(popped_val)

            while max_heap.get_size() > min_heap.get_size() + 1:
                popped_val = max_heap.pop()
                min_heap.push(popped_val)
            
            while max_heap.get_size() < min_heap.get_size():
                popped_val = min_heap.pop()
                max_heap.push(popped_val)

        result = []

        # Add median here
        if max_heap.get_size() == min_heap.get_size():
            median = (max_heap.top() + min_heap.top()) / 2
            result.append(median)
        else:
            result.append(max_heap.top())

        for i in range(k, len(nums), 1):
            # Delete nums[i - k]
            if max_heap.includes(nums[i - k]):
                max_heap.delete(nums[i - k])
            else:
                min_heap.delete(nums[i - k])

            max_heap.push(nums[i])

            # Rebalance
            while min_heap.get_size() > 0 and max_heap.get_size() > 0 and max_heap.top() > min_heap.top():
                popped_val = max_heap.pop()
                min_heap.push(popped_val)

            while max_heap.get_size() > min_heap.get_size() + 1:
                popped_val = max_heap.pop()
                min_heap.push(popped_val)
            
            while max_heap.get_size() < min_heap.get_size():
                popped_val = min_heap.pop()
                max_heap.push(popped_val)
            
            # Add median here
            if max_heap.get_size() == min_heap.get_size():
                median = (max_heap.top() + min_heap.top()) / 2
                result.append(median)
            else:
                result.append(max_heap.top())

        return result
