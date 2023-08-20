# Question 2049: https://leetcode.com/problems/count-nodes-with-the-highest-score/

"""
    This question has no secret, just do it
"""

class Solution:
    def calculateSizes(self, children: List[int], i: int):
        result = 1
        for child in children[i]:
            result = result + self.calculateSizes(children, child)
        
        self.sizes[i] = result
        return result
    
    
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        children = []
        for i in range(len(parents)):
            children.append([])
        
        for i in range(len(parents)):
            if parents[i] >= 0:
                children[parents[i]].append(i)
        
        # Calculate size of tree with root
        self.sizes = [None for i in range(len(parents))]
        self.calculateSizes(children, 0)

        n_trees = 0
        maximum = 0
        for i in range(len(parents)):
            children_nodes = children[i]
            
            size1 = 0
            if len(children_nodes) > 0:
                size1 = self.sizes[children_nodes[0]]

            size2 = 0
            if len(children_nodes) > 1:
                size2 = self.sizes[children_nodes[1]]
            
            size3 = self.sizes[0] - size1 - size2 - 1

            product = max(size1, 1) * max(size2, 1) * max(size3, 1)

            if product == maximum:
                n_trees = n_trees + 1
            elif product > maximum:
                maximum = product
                n_trees = 1
        
        return n_trees
