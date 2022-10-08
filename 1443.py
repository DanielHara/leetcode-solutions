"""
Question 1443: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

Do it greedily. For each node, check if any of its descendants have an apple. Every time you have to go down one level in the tree, add 2
to the answer.
"""

class Solution:
    def recursiveMinTime(self, rootIndex):
        if rootIndex in self.visited:
            return False, 0
        
        self.visited[rootIndex] = True
        hasApple = self.hasApple[rootIndex]
        result = 0
        
        childrenHaveApple = False
        for child in self.tree.get(rootIndex, []):
            (apple, steps) = self.recursiveMinTime(child)
            
            childrenHaveApple = childrenHaveApple or apple
            result = result + steps
            if apple:
                result = result + 2
        
        if childrenHaveApple:
            return True, result
        
        if hasApple:
            return True, 0
        
        return False, 0
    
    
    
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.hasApple = hasApple
        self.tree = {}
        self.visited = {}
        
        for [a, b] in edges:
            if a not in self.tree:
                self.tree[a] = [b]
            else:
                self.tree[a].append(b)
            
            if b not in self.tree:
                self.tree[b] = [a]
            else:
                self.tree[b].append(a)
        
        
        return self.recursiveMinTime(0)[1]
