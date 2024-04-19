"""
    Question 2483: https://leetcode.com/problems/minimum-penalty-for-a-shop/

    Just some DP, nothing fancy
"""

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        S = []

        for i in range(len(customers)):
            if customers[i] == 'Y':
                S.append(1 + (S[i - 1] if i > 0 else 0))
            else:
                S.append(S[i - 1] if i > 0 else 0)
        
        N_hours = len(customers)
        result = None
        lowest_penalty = None

        for hour in range(N_hours):
            penalty = 0
            if hour > 0:
                penalty = penalty + hour - S[hour - 1]
            
            if hour > 0:
                penalty = penalty + S[-1] - S[hour - 1]
            else:
                penalty = penalty + S[-1]

            if lowest_penalty is None or penalty < lowest_penalty:
                lowest_penalty = penalty
                result = hour

        if lowest_penalty > N_hours - S[-1]:
            result = N_hours

        return result
