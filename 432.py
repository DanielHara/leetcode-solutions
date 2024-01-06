# Question 432: https://leetcode.com/problems/all-oone-data-structure/

"""
    This is a very interesting, but also quite hard question to implement.
    Basically, using a double linked list allows you to do the operations in O(1) time.
"""

class Node:
    def __init__(self):
        self.key_set = set()
        self.count = None

        self.left = None
        self.right = None

class AllOne:
    def __init__(self):
        self.beginning = None
        self.end = None

        self.string_to_node_dict = {}
    
    def removeNodeFromList(self, node) -> None:
        left = node.left
        right = node.right

        if left:
            left.right = right
        
        if right:
            right.left = left
        
        if not right:
            self.end = left
        
        if not left:
            self.beginning = right
    
    
    def inc(self, key: str) -> None:
        if self.beginning is None:
            node = Node()
            node.key_set.add(key)
            node.count = 1

            self.beginning = node
            self.end = node

            self.string_to_node_dict[key] = node

            return
        
        if key not in self.string_to_node_dict:
            beginning = self.beginning
            if beginning.count == 1:
                self.string_to_node_dict[key] = beginning
                beginning.key_set.add(key)

                return
            
            node = Node()
            node.key_set.add(key)
            node.count = 1
            self.string_to_node_dict[key] = node

            node.right = beginning
            beginning.left = node
            self.beginning = node

            return
        
        node = self.string_to_node_dict[key]
        
        if node.right and node.right.count == node.count + 1:
            node.right.key_set.add(key)
            self.string_to_node_dict[key] = node.right
        else:
            new_node = Node()
            new_node.left = node
            new_node.right = node.right
            if node.right:
                node.right.left = new_node
            else:
                self.end = new_node
            
            node.right = new_node

            new_node.key_set.add(key)
            new_node.count = node.count + 1

            self.string_to_node_dict[key] = new_node

        node.key_set.remove(key)

        if len(node.key_set) == 0:
            self.removeNodeFromList(node)

    def dec(self, key: str) -> None:
        node = self.string_to_node_dict[key]

        if node.left and node.left.count == node.count - 1:
            node.left.key_set.add(key)
            
            self.string_to_node_dict[key] = node.left
        elif node.count > 1:
            new_node = Node()
            new_node.right = node
            new_node.left = node.left
            if node.left:
                node.left.right = new_node
            else:
                self.beginning = new_node
            
            node.left = new_node

            new_node.key_set.add(key)
            new_node.count = node.count - 1

            self.string_to_node_dict[key] = new_node
        else:
            del self.string_to_node_dict[key]

        node.key_set.remove(key)

        if len(node.key_set) == 0:
            self.removeNodeFromList(node)

        return
        

    def getMaxKey(self) -> str:
        end = self.end

        return '' if not end else next(iter(end.key_set))

    def getMinKey(self) -> str:
        beginning = self.beginning

        return '' if not beginning else next(iter(beginning.key_set))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()