"""
    Question 2593: https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

    Nothing fancy, just do it
"""

class Solution:
    def findScore(self, nums: List[int]) -> int:
        elements = []
        for index, num in enumerate(nums):
            elements.append([index, num])
        
        elements.sort(key=lambda el: el[1])
        elements.reverse()

        marked_indices = set()

        score = 0
        while elements:
            [index, num] = elements.pop()

            if index not in marked_indices:
                score = score + num
                marked_indices.add(index + 1)
                marked_indices.add(index - 1)
        
        return score
