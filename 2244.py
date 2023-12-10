"""
Question 2244: https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/

    Should actually be rated as easy.
"""

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks_frequency_dict = {}
        
        for task in tasks:
            tasks_frequency_dict[task] = tasks_frequency_dict.get(task, 0) + 1
        
        result = 0
        for frequency in tasks_frequency_dict.values():
            a = frequency // 3

            while a >= 0:
                b = (frequency - 3 * a) // 2
                if 3 * a + 2 * b == frequency:
                    result = result + a + b
                    break
                a = a - 1
            
            if a < 0:
                return -1
        
        return result
