"""
Question 1530: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

I just followed the hints of the question
"""

class Solution:
    # Explore Tree and return list of leaf node
    def exploreTree(self, root: TreeNode):
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root]
        
        result = []
        if root.left:
            self.child_to_parent[id(root.left)] = root
            result = result + self.exploreTree(root.left)
        
        if root.right:
            self.child_to_parent[id(root.right)] = root
            result = result + self.exploreTree(root.right)
        
        return result
    
    def DFS(self, node: TreeNode, distance: int, visited) -> int:
        if not node:
            return 0
        
        if distance < 0:
            return 0
    
        if id(node) in visited:
            return 0

        visited[id(node)] = True
        
        result = 0
        
        if not node.right and not node.left:
            result = result + 1

        result = result + self.DFS(node.left, distance - 1, visited)
        result = result + self.DFS(node.right, distance - 1, visited)
        result = result + self.DFS(self.child_to_parent.get(id(node), None), distance - 1, visited)
        
        return result

    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.child_to_parent = {}
        
        leaf_nodes = self.exploreTree(root)
        
        result = 0
        for node in leaf_nodes:
            result = result + self.DFS(node, distance, {})
            
        result = (result - len(leaf_nodes)) // 2
        
        return result
