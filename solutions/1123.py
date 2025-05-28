# Question 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

"""
    Quite straightfoward tree question. Create a map from each node id to its parent, find the deepest tree using in-order transversal,
    and keep finding the parents of the deepest nodes until there's just 1 parent left.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def exploreTree(self, root: Optional[TreeNode]):
        if root is None:
            return
        
        if root.left:
            self.node_id_to_parent[id(root.left)] = root
            self.exploreTree(root.left)

        if root.right:
            self.node_id_to_parent[id(root.right)] = root
            self.exploreTree(root.right)

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.node_id_to_parent = {}
        self.exploreTree(root)

        queue = [root, None]

        deepest_nodes = []
        current_level_nodes = []
        while len(queue) > 1:
            dequeued = queue.pop(0)

            if dequeued == None:
                current_level_nodes = []
                queue.append(None)
            else:
                current_level_nodes.append(dequeued)
                if dequeued.left:
                    queue.append(dequeued.left)
                if dequeued.right:
                    queue.append(dequeued.right)

        while len(current_level_nodes) > 1:
            new_current_level_nodes = []
            for node in current_level_nodes:
                new_current_level_nodes.append(self.node_id_to_parent.get(id(node), node))

            current_level_nodes = new_current_level_nodes
            
            ancestor_set = set()
            for current_level_node in current_level_nodes:
                ancestor_set.add(id(current_level_node))
            
            if len(ancestor_set) == 1:
                return current_level_nodes[0]
        
        return current_level_nodes[0]
