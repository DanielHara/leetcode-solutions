"""
    Question 2101: https://leetcode.com/problems/detonate-the-maximum-bombs/

    Interesting question, you can just use DFS to solve it. Tricky description, though. The first time, I mixed up the range of the bomb,
and its location. In order to detonate another bomb, the range of the first bomb must include the location of the second, and not
just overlapping ranges.
"""

class Solution:
    def DFS(self, start, from_to_dict, detonated):
        if start in detonated:
            return 0
        detonated.add(start)

        result = 1        
        for neighbor in from_to_dict.get(start, []):
            result = result + self.DFS(neighbor, from_to_dict, detonated)
        return result
    
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        from_to_dict = {}

        self.detonated_set = set()
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                [x1, y1, r1] = bombs[i]
                [x2, y2, r2] = bombs[j]

                if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1** 2:
                    if i not in from_to_dict:
                        from_to_dict[i] = []

                    from_to_dict[i].append(j)

        result = 0
        for i in range(len(bombs)):
            result = max(result, self.DFS(i, from_to_dict, set()))

        return result
