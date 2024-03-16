# Question 502: https://leetcode.com/problems/ipo/

"""
    Amayzingly interesting question, and not that hard.
    This is a solution with 2 heaps, and use a greedy approach. Use heap to save the projects will have the capital for,
    and another heap to save the projects for which you still don't have enough capital.
"""

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Use a heap to always choose the project which you have enough capital for, and which gives you the most profit
        current_capital = w

        possible_projects_heap = []
        not_possible_projects_heap = []
        for i in range(0, len(profits)):
            profit = profits[i]
            necessary_capital = capital[i]
            if current_capital >= necessary_capital:
                heapq.heappush(possible_projects_heap, (-1 * profit, (profit, necessary_capital)))
            else:
                heapq.heappush(not_possible_projects_heap, (necessary_capital, (profit, necessary_capital)))
        
        # Process the projects:
        for i in range(k):
            if not possible_projects_heap:
                return current_capital

            (profit, necessary_capital) = heapq.heappop(possible_projects_heap)[1]
            
            current_capital = current_capital + profit

            while not_possible_projects_heap and not_possible_projects_heap[0][0] <= current_capital:
                (profit, necessary_capital) = heapq.heappop(not_possible_projects_heap)[1]
                heapq.heappush(possible_projects_heap, (-1 * profit, (profit, necessary_capital)))
        
        return current_capital
