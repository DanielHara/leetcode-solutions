# Question 2059: https://leetcode.com/problems/minimum-operations-to-convert-number/

"""
  Simply get started from the start, and save on how many steps you can reach each of the numbers from 0 to 1000.
  In the worst case, you'll need approximately O(1000*len(nums)) operations.
  I've got this inspiration from Breadth First Search.
"""

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        # results[i] will hold the minimum number of operations from start to goal
        results = [None for i in range(1001)]
        
        border = [start]
        
        results[start] = 0
        
        counter = 1
        while border:
            new_border = []
            
            while border:
                el = border.pop()
            
                for num in nums:
                    possibilities = [el + num, el - num, el ^ num]
                
                    for possibility in possibilities:
                        if possibility >= 0 and possibility <= 1000 and results[possibility] is None:
                            results[possibility] = counter
                        
                            new_border.append(possibility)

            counter = counter + 1
            border = new_border
            
        if goal < 0 or goal > 1000:
            result = None
            
            for num in nums:
                possibilities = [goal + num, goal - num, goal ^ num]
                
                for possibility in possibilities:
                    if possibility >= 0 and possibility <= 1000 and results[possibility] is not None:
                        result = min(result, 1 + results[possibility]) if result is not None else (1 + results[possibility])

            return result if result is not None else -1
    
        return results[goal] if results[goal] is not None else -1
        
        
        