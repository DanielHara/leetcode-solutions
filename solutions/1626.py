"""
Question 1626: https://leetcode.com/problems/best-team-with-no-conflicts/

    A bit of sorting and DP does the trick
"""


class Solution:
    def compareItems(self, item1, items2):
        if item1[0] > items2[0]:
            return 1
        if item1[0] < items2[0]:
            return -1
        if item1[1] > items2[1]:
            return 1
        if item1[1] < items2[1]:
            return -1
        
        return 0


    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        items = [[ages[i], scores[i]] for i in range(len(scores))]

        # Sort by age
        items.sort(key=cmp_to_key(self.compareItems))

        n = len(items)
        M = [items[i][1] for i in range(n)]
        for i in range(n-2, -1, -1):
            best = 0
            for j in range(i+1, n, 1):
                if items[j][1] >= items[i][1] or items[j][0] == items[i][0]:
                    best = max(best, M[j])
        
            M[i] = max(M[i], best + M[i])
        
        return max(M)
