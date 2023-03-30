# Question 1828: https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle

"""
    A "just do it" approach passes the judge. But the follow up is interesting: Could you find the answer for each query in better complexity than O(n)?
    I still didn't think about that, something like "Premature optimisation is the root of all evil"
"""

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []

        for [x, y, r] in queries:
            result = 0

            for [a, b] in points:
                if (a - x) ** 2 + (b - y) ** 2 <= r ** 2:
                    result = result + 1
            
            answer.append(result)

        return answer
