# Question 2285: https://leetcode.com/problems/maximum-total-importance-of-roads/

"""
    Just do it greedily. Pick the city connected with the highest amount of roads, and assign to it the largest possible value.
"""

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        city_index_to_number_roads = {}
        for road in roads:
            city_index_to_number_roads[road[0]] = city_index_to_number_roads.get(road[0], 0) + 1
            city_index_to_number_roads[road[1]] = city_index_to_number_roads.get(road[1], 0) + 1
        
        city_number_roads_entries = list(city_index_to_number_roads.items())
        city_number_roads_entries.sort(key=lambda city_number_roads_entry: city_number_roads_entry[1])

        city_value = {}

        index = n
        while city_number_roads_entries:
            entry = city_number_roads_entries.pop()
            city = entry[0]
            city_value[city] = index
            index = index - 1

        result = 0
        for road in roads:
            result = result + city_value.get(road[0], 0) + city_value.get(road[1], 0)

        return result
