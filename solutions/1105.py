# Question 1079: https://leetcode.com/problems/filling-bookcase-shelves/description/

"""
    A very interesting question! DP does the trick
"""


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = []

        for i in range(len(books)):
            width = books[i][0]
            height = books[i][1]

            best_height = (dp[i - 1] if i > 0 else 0) + books[i][1]

            j = i - 1
            while j >= 0 and width + books[j][0] <= shelfWidth:
                width = width + books[j][0]
                height = max(height, books[j][1])

                j = j - 1

                best_height = min(best_height, (dp[j] if j >= 0 else 0) + height)            

            best_height = min(best_height, (dp[j] if j >= 0 else 0) + height)            
            dp.append(best_height)
        
        return dp[-1]
