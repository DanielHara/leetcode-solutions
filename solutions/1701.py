# Question 1701: https://leetcode.com/problems/average-waiting-time/

"""
    Not a difficult question, just do it!
"""

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = customers[0][0]

        total_waiting_time = 0
        for customer in customers:
            if customer[0] > t:
                total_waiting_time = total_waiting_time + customer[1]
                t = customer[0] + customer[1]
            else:
                total_waiting_time = total_waiting_time + customer[1] + (t - customer[0])
                t = t + customer[1]

        return total_waiting_time / len(customers)
