# Question 1436: https://leetcode.com/problems/destination-city/

"""
    Very trivial question. I decided to solve it just because it mentions my home city, Sao Paulo
"""

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:    
        cities = set()

        for [start, destination] in paths:
            cities.add(start)
            cities.add(destination)
        
        for [start, destination] in paths:
            if start in cities:
                cities.remove(start)
        
        return next(iter(cities))
