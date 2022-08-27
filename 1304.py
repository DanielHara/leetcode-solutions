# Question 1304: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

"""
    Fairly trivial question
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        for i in range(1, n):
            answer.append(i)

        answer.append(-1*(n) * (n-1) // 2)

        return answer
