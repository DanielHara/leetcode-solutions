# Question 2140: https://leetcode.com/problems/solving-questions-with-brainpower/

# Just a bit of DP does the trick

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [None for i in range(len(questions))]

        dp[-1] = questions[-1][0]

        for i in range(len(questions) - 2, -1, -1):
            question = questions[i]

            dp[i] = max(dp[i + 1], question[0] + (dp[i + question[1] + 1] if i + question[1] + 1 < len(dp) else 0) )

        return max(dp)
