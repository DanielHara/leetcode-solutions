# Question 2712: https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

"""
    Very interesting question as well! Use some DP
"""

class Solution:
    def minimumCostFromNetFlips(self, net_flips: List[int]) -> int:
        N = len(net_flips)

        cost_left = [0 for i in range(N)]
        for index in range(0, N):
            if net_flips[index] == 0:
                cost_left[index] = cost_left[index - 1] if index - 1 >= 0 else 0
            elif index - 1 >= 0 and net_flips[index] == net_flips[index - 1]:
                cost_left[index] = cost_left[index - 1] + 1
            else:
                cost_left[index] = (cost_left[index - 1] if index - 1 >= 0 else 0) + index + 1 + index
        
        cost_right = [0 for i in range(N)]
        for index in range(N - 1, -1, -1):
            if net_flips[index] == 0:
                cost_right[index] = cost_right[index + 1] if index + 1 <= N - 1 else 0
            elif index + 1 <= N - 1 and net_flips[index] == net_flips[index + 1]:
                cost_right[index] = cost_right[index + 1] + 1
            else:
                cost_right[index] = (cost_right[index + 1] if index + 1 <= N - 1 else 0) + N - index + N - index - 1

        result = None
        for index in range(-1, N):
            candidate = (cost_left[index] if index >= 0 else 0) + (cost_right[index + 1] if index + 1 <= N - 1 else 0)
            result = min(result, candidate) if result is not None else candidate
        
        return result


    def minimumCost(self, s: str) -> int:
        # First: try to make everything 0
        net_flips = [0 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == '1':
                net_flips[i] = 1
        
        possibility1 = self.minimumCostFromNetFlips(net_flips)

        # Second: try to make everything 1
        net_flips = [0 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == '0':
                net_flips[i] = 1

        possibility2 = self.minimumCostFromNetFlips(net_flips)

        return min(possibility1, possibility2)

