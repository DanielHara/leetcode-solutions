# Question 832: https://leetcode.com/problems/flipping-an-image/

"""
   Not a difficult question, basically CS 101, swap the elements to reverse the row, and then flip them.
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        N = len(image)
        M = len(image[0])
        
        # image is a N x M array 
        
        for i in range(N):
            for j in range(int(M / 2)):
                temp = image[i][j]
                image[i][j] = image[i][M - 1 - j]
                image[i][M - 1 - j] = temp
                
                image[i][j] = 1 if image[i][j] == 0 else 0
                image[i][M - 1 - j] = 1 if image[i][M - 1 - j] == 0 else 0
            
            if M % 2 == 1:
                image[i][int(M / 2)] = 1 if image[i][int(M / 2)] == 0 else 0
        
        return image
