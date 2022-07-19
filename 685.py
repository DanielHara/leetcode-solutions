# Question 685: https://leetcode.com/problems/redundant-connection-ii/

"""
Go through the edges and find one that, if removed, results in a tree-like structure. For every vertex,
go up to its parent recursively, as far as you can, until you the candidates to be the root. If there is only
one for every node, you're done! Beware to save the elements you've already seen in your way up in a set, so that
you don't get trapped in an infinite loop if there's a cycle.
"""

class Solution:
    def searchUppermostDescendant(self, node: int, recStack):
        if node in recStack:
            return None
        
        recStack[node] = True
        
        if node in self.upper_most_descendant:
            return self.upper_most_descendant[node]
        
        if node not in self.child_to_parent:
            self.upper_most_descendant[node] = node
            return node    

        result = self.searchUppermostDescendant(self.child_to_parent[node], recStack)
        self.upper_most_descendant[node] = result
        return result
    
    def isRootedTree(self, edges: List[List[int]]):
        self.child_to_parent = {}

        maximum = 0
        for edge in edges:
            parent = edge[0]
            child = edge[1]
            
            maximum = max(parent, child, maximum)
            
            if child in self.child_to_parent:
                return False

            self.child_to_parent[child] = parent
        
        self.upper_most_descendant = {}
        
        for i in range(1, maximum + 1):
            recStack = {}
            descendant = self.searchUppermostDescendant(i, recStack)
            if descendant is None:
                return False
        
        if 1 not in self.upper_most_descendant:
            return False
        
        root = self.upper_most_descendant[1]
        
        for i in range(2, maximum + 1):
            if root != self.upper_most_descendant[i]:
                return False
        
        return True
        
    
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        for i in range(len(edges) - 1, -1, -1):
            candidate = edges[:i] + edges[i + 1:]
            
            if self.isRootedTree(candidate):
                return edges[i]
