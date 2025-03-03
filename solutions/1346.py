"""
Question 1346: https://leetcode.com/problems/check-if-n-and-its-double-exist/

    Easy warm-up
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen_set = set()
        for num in arr:
            if (num % 2 == 0 and num // 2 in seen_set) or 2 * num in seen_set:
                return True
            seen_set.add(num)

        return False
