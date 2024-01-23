# Question 2126: https://leetcode.com/problems/destroying-asteroids/

"""
    Do it greedily. Your best change of the planet not being destroyed is to hit it with the smallest asteroid
    and keep on increasing its mass.
"""

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Do it greedily:
        
        asteroids.sort()
        
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            
            mass = mass + asteroid
        
        return True
