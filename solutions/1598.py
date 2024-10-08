# Question 1598: https://leetcode.com/problems/crawler-log-folder/

"""
    Trivial, but interesting question!
"""

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for log in logs:
            if log == '../':
                if depth > 0:
                    depth = depth - 1
            elif log == './':
                pass
            else:
                depth = depth + 1
        
        return depth
