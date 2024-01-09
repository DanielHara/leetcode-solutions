# Question 2718: https://leetcode.com/problems/sum-of-matrix-after-queries/

"""
    Very interesting question with an elegant solution!
    I confess I had to peak at the hints to come up with the solution, and was impressed by
    the elegance and simplicity of the answer. That after having spent something like 1 hour trying
    to come up with a fancy solution to this problem.
"""

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:        
        seen_rows = set()
        seen_columns = set()

        result = 0
        for [type_query, index, val] in reversed(queries):
            if type_query == 0:
                row = index
                if row in seen_rows:
                    continue
               
                result = result + val * (n - len(seen_columns))
                seen_rows.add(row)
            if type_query == 1:
                col = index
                if col in seen_columns:
                    continue

                result = result + val * (n - len(seen_rows))
                seen_columns.add(col)
        
        return result
