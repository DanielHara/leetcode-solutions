# Question 558: https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

"""
    Just do it recursively.
    It helps a lot to have solved question 427: https://leetcode.com/problems/construct-quad-tree/description/ before hand.
"""


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    # Just do it recursively
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf and quadTree2.isLeaf:
            quadTree = Node()
            quadTree.isLeaf = True
            quadTree.val = quadTree1.val or quadTree2.val

            return quadTree

        if quadTree1.isLeaf and not quadTree2.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        
        if not quadTree1.isLeaf and quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        
        top_left = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        top_right = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottom_left = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottom_right = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf:
            if top_left.val is True and top_right.val is True and bottom_left.val is True and bottom_right.val is True:
                quadTree = Node()
                quadTree.isLeaf = True
                quadTree.val = True
                return quadTree
            
            if top_left.val is False and top_right.val is False and bottom_left.val is False and bottom_right.val is False:
                quadTree = Node()
                quadTree.isLeaf = True
                quadTree.val = False
                return quadTree
            
        quadTree = Node()
        quadTree.isLeaf = False
        quadTree.topLeft = top_left
        quadTree.topRight = top_right
        quadTree.bottomLeft = bottom_left
        quadTree.bottomRight = bottom_right
        
        return quadTree
