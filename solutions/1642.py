# Question 1642: https://leetcode.com/problems/furthest-building-you-can-reach/

# I went for the hints and implemented it.

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        for i in range(len(heights) - 1):
            if heights[i + 1] > heights[i]:
                el = heights[i + 1] - heights[i]
                if len(heap) < ladders:
                    heapq.heappush(heap, el)
                elif heap and el > heap[0]:
                    if bricks < heap[0]:
                        return i

                    bricks = bricks - heap[0]
                    heapq.heappop(heap)
                    heapq.heappush(heap, el)
                else:
                    if bricks < el:
                        return i

                    bricks = bricks - el
    
        return len(heights) - 1
