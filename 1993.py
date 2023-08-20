# Question 1993: https://leetcode.com/problems/operations-on-tree/

"""
    Just brute-force it.
"""


class LockingTree:
    def __init__(self, parents: List[int]):
        self.locked = {}
        self.parents = parents

        self.children = {}

        for i in range(len(parents)):
            parent = parents[i]

            if parent >= 0:
                if parent not in self.children:
                    self.children[parent] = []
                self.children[parent].append(i)

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            return False
        
        if self.locked[num] != user:
            return False
        
        del self.locked[num]
        return True

    def hasLockedDescendant(self, num: int) -> bool:
        if num in self.locked:
            return True
        
        for child in self.children.get(num, []):
            if self.hasLockedDescendant(child):
                return True
        
        return False

    def unlockAllDescendants(self, num: int) -> bool:
        for child in self.children.get(num, []):
            if child in self.locked:
                del self.locked[child]
            self.unlockAllDescendants(child)

    def upgrade(self, num: int, user: int) -> bool:
        # Check if the node isn't locked and doesn't have locked ancestors:
        
        current_num = num
        while current_num != -1:
            if current_num in self.locked:
                return False
            current_num = self.parents[current_num]

        children = self.children.get(num, [])
        for child in children:
            if self.hasLockedDescendant(child):
                self.locked[num] = user
                self.unlockAllDescendants(num)

                return True

        return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)