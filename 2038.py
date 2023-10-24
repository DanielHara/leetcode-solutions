# Question 2038: https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

"""
    Use a greedy approach and heaps to do the heavy-lifting of finding the tastiest chunk of the string Alice or Bob
    can find in each move of the game.
"""

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A_heap = []
        B_heap = []

        i = 0
        while i < len(colors):
            j = i + 1
            while j < len(colors) and colors[j] == colors[i]:
                j = j + 1
            
            if colors[i] == 'A':
                heapq.heappush(A_heap, -1*(j - i))
            else:
                heapq.heappush(B_heap, -1*(j - i))
            
            i = j

        while True:
            if not A_heap or abs(A_heap[0]) <= 2:
                return False
            
            element = heapq.heappop(A_heap)
            heapq.heappush(A_heap, element + 1)

            if not B_heap or abs(B_heap[0]) <= 2:
                return True
            
            element = heapq.heappop(B_heap)
            heapq.heappush(B_heap, element + 1)
        
        return True
