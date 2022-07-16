"""
Question 1636: https://leetcode.com/problems/sort-array-by-increasing-frequency/
Just use the feature of passing a function to the sort function.
"""

class Solution:
    def compare(self, a: int, b: int) -> int:
        if self.frequency_dictionary[a] < self.frequency_dictionary[b]:
            return -1
        
        if self.frequency_dictionary[a] > self.frequency_dictionary[b]:
            return 1
        
        return b - a
    
    def frequencySort(self, nums: List[int]) -> List[int]:
        self.frequency_dictionary = {}
        
        for num in nums:
            self.frequency_dictionary[num] = self.frequency_dictionary.get(num, 0) + 1
        
        nums.sort(key=cmp_to_key(self.compare))
        
        return nums
