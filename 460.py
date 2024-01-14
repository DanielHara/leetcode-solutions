"""
    Question 460: https://leetcode.com/problems/lfu-cache/

    A very interesting question!
    This is kinda similar problem to question 432: https://leetcode.com/problems/all-oone-data-structure/
    I reused some of the code and modified it just a bit.

    To solve the requirement:
        For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

    , you can just use Python dicts (not sets), because they are already ordered dicts since Python 3.7
"""


class Node:
    def __init__(self):
        self.key_set = {}
        self.count = 1

        self.left = None
        self.right = None

        
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.beginning = None
        self.end = None

        self.key_to_node_dict = {}
        self.key_to_value_dict = {}
    
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

    def get(self, key: int) -> int:
        if key not in self.key_to_node_dict:
            return -1

        if self.beginning is None:
            node = Node()
            node.key_set[key] = True
            node.count = 1

            self.beginning = node
            self.end = node

            self.key_to_node_dict[key] = node

            return key_to_value_dict[key]
        
        node = self.key_to_node_dict[key]

        if node.right and node.right.count == node.count + 1:
            node.right.key_set[key] = True
            self.key_to_node_dict[key] = node.right
        else:
            new_node = Node()
            new_node.left = node
            new_node.right = node.right
            if node.right:
                node.right.left = new_node
            else:
                self.end = new_node
            
            node.right = new_node

            new_node.key_set[key] = True
            new_node.count = node.count + 1

            self.key_to_node_dict[key] = new_node
        
        del node.key_set[key]

        if len(node.key_set) == 0:
            self.removeNodeFromList(node)
        
        return self.key_to_value_dict[key]
        

    def put(self, key: int, value: int) -> None:
        self.key_to_value_dict[key] = value
        
        # Case in which you have to remove a key from the cache
        if key not in self.key_to_node_dict and len(self.key_to_node_dict) == self.capacity:
            node = self.beginning
            least_recently_used_key = next(iter(node.key_set))
            del node.key_set[least_recently_used_key]

            if len(node.key_set) == 0:
                self.removeNodeFromList(node)

            del self.key_to_node_dict[least_recently_used_key]
            del self.key_to_value_dict[least_recently_used_key]

        if key not in self.key_to_node_dict:
            if self.beginning is None:
                node = Node()
                node.key_set[key] = True
                node.count = 1

                self.beginning = node
                self.end = node

                self.key_to_node_dict[key] = node
                
                return

            beginning = self.beginning
            if beginning.count == 1:
                self.key_to_node_dict[key] = beginning
                beginning.key_set[key] = True

                return

            node = Node()
            node.key_set[key] = True
            node.count = 1
            self.key_to_node_dict[key] = node

            node.right = beginning
            beginning.left = node
            self.beginning = node

            return
        
        # Case where the key was present

        node = self.key_to_node_dict[key]

        if node.right and node.right.count == node.count + 1:
            node.right.key_set[key] = True
            self.key_to_node_dict[key] = node.right
        else:
            new_node = Node()
            new_node.left = node
            new_node.right = node.right
            if node.right:
                node.right.left = new_node
            else:
                self.end = new_node
            
            node.right = new_node

            new_node.key_set[key] = True
            new_node.count = node.count + 1

            self.key_to_node_dict[key] = new_node
        
        del node.key_set[key]

        if len(node.key_set) == 0:
            self.removeNodeFromList(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
