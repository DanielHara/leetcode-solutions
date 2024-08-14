# Question 2895: https://leetcode.com/problems/minimum-processing-time/

"""
    Interesting, easy question
"""

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        N_cores = 4
        
        processorTime.sort(reverse=True)
        tasks.sort()
        
        result = 0
        while processorTime:
            time_available = processorTime.pop()

            longest_task = tasks.pop()
            for i in range(N_cores - 1):
                tasks.pop()

            result = max(result, time_available + longest_task)
        
        return result
