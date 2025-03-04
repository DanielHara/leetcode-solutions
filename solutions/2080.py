# Question 2080: https://leetcode.com/problems/range-frequency-queries/

"""
    Just use a map to store the indexes where each value occurs, and then use binary search.
"""

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.value_to_indexes = {}
        for index, num in enumerate(arr):
            if num not in self.value_to_indexes:
                self.value_to_indexes[num] = []
            self.value_to_indexes[num].append(index)

    # Gives the smallest index in arr so that arr[index] >= target
    # Returns None if there's none
    def binarySearch1(self, start: int, end: int, target: int, arr: List[int]):
        if start > end:
            return None
        
        half = (start + end) // 2
        if arr[half] >= target and (half == start or arr[half - 1] < target):
            return half
        if arr[half] >= target:
            return self.binarySearch1(start, half - 1, target, arr)

        return self.binarySearch1(half + 1, end, target, arr)
    
    # Gives the largest index in arr so that arr[index] <= target
    # Returns None if there's none
    def binarySearch2(self, start: int, end: int, target: int, arr: List[int]):
        if start > end:
            return None
        
        half = (start + end) // 2
        if arr[half] <= target and (half == end or arr[half + 1] > target):
            return half
        if arr[half] <= target:
            return self.binarySearch2(half + 1, end, target, arr)

        return self.binarySearch2(start, half - 1, target, arr)        
    
    def query(self, left: int, right: int, value: int) -> int:
        indexes_with_value = self.value_to_indexes.get(value, [])
        start_index = self.binarySearch1(0, len(indexes_with_value) - 1, left, indexes_with_value)
        end_index = self.binarySearch2(0,  len(indexes_with_value) - 1, right, indexes_with_value)
        
        if start_index is not None and end_index is not None:
            return end_index - start_index + 1
        
        return 0



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)