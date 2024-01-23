# Question 2365: https://leetcode.com/problems/task-scheduler-ii/

"""
    Not a difficult question, just do it
"""

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        minimum_time_dict = {}

        result = 0

        for task in tasks:
            if task not in minimum_time_dict or result >= minimum_time_dict[task]:
                result = result + 1
                
                minimum_time_dict[task] = result + space + 1
            else:
                result = minimum_time_dict[task]

                minimum_time_dict[task] = result + space + 1

        return result
