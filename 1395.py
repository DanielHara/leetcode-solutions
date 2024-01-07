# Question 1395: https://leetcode.com/problems/count-number-of-teams/

"""
    Just use some DP
"""

class Solution:
    def numTeam2(self, rating: List[int]) -> int:
        result = 0

        # S[i] is the number of indexes j > i with rating[j] < rating[i]
        # T[i] is the number of indexes j < i with rating[j] > rating[i]

        S = [None for i in range(len(rating))]
        T = [None for i in range(len(rating))]

        S[-1] = 0
        for i in range(len(rating) - 2, -1, -1):
            number = 0
            for j in range(i + 1, len(rating), 1):
                if rating[j] < rating[i]:
                    number = number + 1
            S[i] = number

        T[0] = 0
        for i in range(0, len(rating)):
            number = 0
            for j in range(0, i, 1):
                if rating[j] > rating[i]:
                    number = number + 1
            T[i] = number
        
        result = 0
        for i in range(1, len(rating) - 1):
            result = result + S[i] * T[i]
        
        return result


    def numTeam1(self, rating: List[int]) -> int:
        result = 0

        # S[i] is the number of indexes j > i with rating[j] > rating[i]
        # T[i] is the number of indexes j < i with rating[j] < rating[i]

        S = [None for i in range(len(rating))]
        T = [None for i in range(len(rating))]

        S[-1] = 0
        for i in range(len(rating) - 2, -1, -1):
            number = 0
            for j in range(i + 1, len(rating), 1):
                if rating[j] > rating[i]:
                    number = number + 1
            S[i] = number

        T[0] = 0
        for i in range(0, len(rating)):
            number = 0
            for j in range(0, i, 1):
                if rating[j] < rating[i]:
                    number = number + 1
            T[i] = number
        
        result = 0
        for i in range(1, len(rating) - 1):
            result = result + S[i] * T[i]
        
        return result


    # Probably you can do this in quadratic time    
    def numTeams(self, rating: List[int]) -> int:
        return self.numTeam1(rating) + self.numTeam2(rating)
        