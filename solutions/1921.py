# Question 1921: https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Array of the times in which you are eaten by a monster
        timing = []

        for i in range(0, len(dist)): 
            if dist[i] % speed[i] == 0:
                timing.append(int(dist[i] / speed[i]))
            else:
                timing.append(int(dist[i] / speed[i]) + 1)

        timing.sort()

        N = 0
        for index, time in enumerate(timing):
            if timing[index] < index + 1:
                return N
            N = N + 1

        return N
