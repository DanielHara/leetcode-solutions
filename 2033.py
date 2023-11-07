# Question 2033: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

"""
    Do it greedily!
"""

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        array = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                array.append(grid[i][j])
        
        if len(array) == 1:
            return 0
        
        array.sort()

        if len(array) != 0:
            half = len(array) // 2
            result = 0

            for element in array:
                if (element - array[half]) % x != 0:
                    return -1
            
                result = result + abs(element - array[half]) // x
        
            return result


        half = len(array) // 2 - 1
        
        first_possibility = 0
        second_possibility = 0

        for element in array:
            if (element - array[half]) % x != 0 or (element - array[half + 1]) % x != 0:
                return -1
            
            first_possibility = first_possibility + abs(element - array[half]) // x
            second_possibility = second_possibility + abs(element - array[half + 1]) // x
        
        return min(first_possibility, second_possibility)
