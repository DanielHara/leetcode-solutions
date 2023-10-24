"""
Question 605: https://leetcode.com/problems/can-place-flowers/
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0

        count = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i = i + 2
            else:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    i = i + 2
                    count = count + 1
                else:
                    i = i + 1

        return count >= n
