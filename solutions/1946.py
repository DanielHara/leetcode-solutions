# Question 1946: https://leetcode.com/problems/largest-number-after-mutating-substring/

"""
  Just do it greedily.
"""

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num_array = [char for char in num]

        index = 0
        while index < len(num_array):
            if int(change[int(num_array[index])]) > int(num_array[index]):
                while index < len(num_array) and int(change[int(num_array[index])]) >= int(num_array[index]):
                    num_array[index] = str(change[int(num_array[index])])
                    index = index + 1
                
                return ''.join(num_array)

            index = index + 1

        return ''.join(num_array)
