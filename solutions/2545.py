"""
    Question 2545: https://leetcode.com/problems/sort-the-students-by-their-kth-score/

    Easy question, just use Python's key parameters in the sort function.
"""

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda row: row[k], reverse=True)

        return score
