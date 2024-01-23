# Question 2079: https://leetcode.com/problems/watering-plants/

"""
    Just pop from the initial position of the array, saving how many steps you need to come
    back to the river if needed.
"""

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = 0
        
        steps = 0
        S = 0
        while plants:
            while plants and (S + plants[0]) <= capacity:
                plant = plants.pop(0)
                
                S = S + plant
                
                result = result + 1
                steps = steps + 1
            
            if plants:
                # Go to the river and back
                result = result + 2 * steps
            
            S = 0
        
        return result
