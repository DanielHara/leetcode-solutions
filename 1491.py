"""
Question 1491: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

Really trivial questio
"""

class Solution:
    def average(self, salary: List[int]) -> float:
        maximum = salary[0]
        minimum = salary[0]
        
        total_sum = 0
        for s in salary:
            maximum = max(s, maximum)
            minimum = min(s, minimum)
            
            total_sum = total_sum + s
        
        return (total_sum - maximum - minimum) / (len(salary) - 2)
