# Question 2353: https://leetcode.com/problems/design-a-food-rating-system/

"""
    Quite interesting question, just use a trick with cmp_to_key and a heap, to deal with the requirement
    of returning the lexicographically smallest string when there's a tie.
"""

from functools import cmp_to_key
import heapq

class FoodRatings:
    def comparisonFunction(self, food_entry1, food_entry2):
        (rating1, food1) = food_entry1
        (rating2, food2) = food_entry2

        if rating1 > rating2:
            return -1
        if rating1 < rating2:
            return 1
        
        if food1 > food2:
            return 1
        if food2 > food1:
            return -1
        
        return 0

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        key_function = cmp_to_key(self.comparisonFunction)

        self.food_to_rating_dict = {}
        self.food_to_cuisine_dict = {}
        self.cuisine_to_max_heap = {}

        self.key_function = key_function

        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]

            self.food_to_cuisine_dict[food] = cuisine

            if cuisine not in self.cuisine_to_max_heap:
                self.cuisine_to_max_heap[cuisine] = []
            
            heap = self.cuisine_to_max_heap[cuisine]
            heapq.heappush(heap, (self.key_function((rating, food)), (rating, food)))

            self.food_to_rating_dict[food] = rating

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating_dict[food] = newRating

        cuisine = self.food_to_cuisine_dict[food]
        heap = self.cuisine_to_max_heap[cuisine]
        heapq.heappush(heap, (self.key_function((newRating, food)), (newRating, food)))

    def highestRated(self, cuisine: str) -> str:
        if cuisine not in self.cuisine_to_max_heap:
            return None

        heap = self.cuisine_to_max_heap[cuisine]

        while heap:
            (key, food_entry) = heapq.heappop(heap)
            (rating, food) = food_entry

            if self.food_to_rating_dict[food] == rating:
                heapq.heappush(heap, (self.key_function((rating, food)), (rating, food)))
                return food

        return None

        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)