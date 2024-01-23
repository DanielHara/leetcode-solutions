# Question 1481: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

"""
    Just use a frequency dictionary and do it greedily
"""

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequency_dictionary = {}
        for number in arr:
            frequency_dictionary[number] = frequency_dictionary.get(number, 0) + 1
        
        values = list(frequency_dictionary.values())
        values.sort()

        removed = 0
        for value in values:
            if k >= value:
                removed = removed + 1
                k = k - value
            else:
                break
        
        return len(values) - removed
