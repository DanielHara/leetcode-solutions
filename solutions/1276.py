# Question 1276: https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

"""
    Trivial question, just secondary school math :)
    
    If the answer is [total_jumbo, total_small], then the following must hold:
    4 * total_jumbo + 2 * total_small = tomatoSlices
    total_jumbo + total_small = cheeseSlices

    Therefore:
    2 * total_jumbo = tomatoSlices - 2 * cheeseSlices
    total_small = cheeseSlices - total_jumbo
"""

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if not (tomatoSlices - 2 * cheeseSlices >= 0 and (tomatoSlices - 2 * cheeseSlices) % 2 == 0):
            return []
        
        total_jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        total_small = cheeseSlices - total_jumbo

        if total_small < 0:
            return []
        
        return [total_jumbo, total_small]
