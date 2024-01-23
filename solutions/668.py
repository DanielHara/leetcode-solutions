# Question 668: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

"""
    This question is very similar to question 719: https://leetcode.com/problems/find-k-th-smallest-pair-distance/

    So, I simply used the same trick with binary search
"""    

class Solution:
    def binarySearchForResult(self, start: int, end: int, rows: int, columns: int, k: int):
        if start > end:
            return None
        
        half = (start + end) // 2

        number_of_pairs_less_or_equal = self.getNumberOfPairsWithMultiplicationLessOrEqualTo(rows, columns, half)
        number_of_pairs_less_or_equal_previous = self.getNumberOfPairsWithMultiplicationLessOrEqualTo(rows, columns, half - 1)

        if number_of_pairs_less_or_equal >= k and number_of_pairs_less_or_equal_previous < k:
            return half
        
        if number_of_pairs_less_or_equal < k:
            return self.binarySearchForResult(half + 1, end, rows, columns, k)
        
        return self.binarySearchForResult(start, half - 1, rows, columns, k)

    # returns the number of pairs which have multiplication <= target
    def getNumberOfPairsWithMultiplicationLessOrEqualTo(self, rows: int, columns: int, target: int):
        result = 0

        for i in range(1, columns + 1):
            result = result + min(rows, target // i)
        
        return result

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        rows = m
        columns = n

        return self.binarySearchForResult(0, rows * columns, rows, columns, k)
