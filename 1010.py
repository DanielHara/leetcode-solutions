# Question 1010: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/

"""
The main trick in this question is: It's very similar to the 2-sum problem, because you have a very limited
number of possibilities to try to sum up to a number that is divisible by 60, as one constraint of the problem is:
1 <= time[i] <= 500
"""


class Solution:
    # Returns the smallest index for which vector[index] > target, and None if there is none    
    def binarySearch(self, vector: List[int], target: int, i: int, j: int):
        if i > j:
            return None
        
        half = (i + j) // 2

        if vector[half] > target and (half == i or vector[half - 1] <= target):
            return half
        
        if vector[half] > target:
            return self.binarySearch(vector, target, i, half - 1)
        return self.binarySearch(vector, target, half + 1, j)


    def numPairsDivisibleBy60(self, time: List[int]) -> int:    
        if len(time) <= 1:
            return 0

        time.sort()

        maximum_possible_sum = time[len(time) - 1] + time[len(time) - 2]

        index_dictionary = {}
        for index, t in enumerate(time):
            if t not in index_dictionary:
                index_dictionary[t] = [index]
            else:
                index_dictionary[t].append(index)
        
        result = 0
        for index, t in enumerate(time):
            possibility = 60 - t

            while possibility <= maximum_possible_sum:
                if possibility in index_dictionary:
                    target_index = self.binarySearch(index_dictionary[possibility], index, 0, len(index_dictionary[possibility]) - 1)
                    
                    if target_index is not None:
                        result = result + len(index_dictionary[possibility]) - target_index
                
                possibility = 60 + possibility

        return result

