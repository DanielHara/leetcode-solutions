# Question 835: https://leetcode.com/problems/image-overlap/

"""
   Looking at the constrains of the problem, I see n <= 30, which is a rather small value.
   Therefore, I just opted for brute-force, which solves the question.
"""

class Solution:
    def calculateOverlap(self, img1: List[List[int]], img2: List[List[int]], position: List[int]):
        N = len(img1)
        [x, y] = position

        first_overlap = 0
        for i in range(x, N, 1):
            for j in range(y, N, 1):
                first_overlap = first_overlap + img1[i][j] * img2[i - x][j - y]
        
        second_overlap = 0
        for i in range(0, x + 1, 1):
            for j in range(0, y + 1, 1):
                second_overlap = second_overlap + img1[i][j] * img2[i - x + N - 1][j - y + N - 1]
        
        third_overlap = 0
        for i in range(x, N, 1):
            for j in range(0, y + 1, 1):
                third_overlap = third_overlap + img1[i][j] * img2[i - x][j - y + N - 1]

        fourth_overlap = 0
        for i in range(0, x + 1, 1):
            for j in range(y, N, 1):
                fourth_overlap = fourth_overlap + img1[i][j] * img2[i - x + N - 1][j - y]
        
        return max(first_overlap, second_overlap, third_overlap, fourth_overlap)
    
    def getLargestOverlap(self, steady_img: List[List[int]], moving_img: List[List[int]]):
        N = len(steady_img)

        result = 0
        for i in range(0, N, 1):
            for j in range(0, N, 1):
                result = max(result, self.calculateOverlap(steady_img, moving_img, [i, j]))

        return result
    
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        return max(self.getLargestOverlap(img1, img2), self.getLargestOverlap(img2, img1))
