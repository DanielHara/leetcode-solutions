"""
Question 2105: https://leetcode.com/problems/watering-plants-ii/

Should actually be an easy question. Simply follow the steps described in watering the plants
and that's your answer, no real algorithm needed.
"""

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        i = 0
        j = len(plants) - 1
        
        result = 0
        A = capacityA
        B = capacityB

        while i < j:
            if A >= plants[i]:
                A = A - plants[i]
            else:
                A = capacityA - plants[i]
                result = result + 1
            
            i = i + 1
            
            if B >= plants[j]:
                B = B - plants[j]
            else:
                B = capacityB - plants[j]
                result = result + 1
            
            j = j - 1
        
        if i == j:
            if (A >= B and A < plants[i]) or (A < B and B < plants[j]):
                result = result + 1
        
        return result
