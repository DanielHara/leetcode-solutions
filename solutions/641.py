"""
Question 641: https://leetcode.com/problems/design-circular-deque/
"""

"""
A simple doubly linked list will do the trick.
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.previous = None
        self.next = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.limit = k
        self.count = 0
        self.doublyLinkedListFront = None
        self.doublyLinkedListRear = None

    def insertFront(self, value: int) -> bool:
        if self.limit == self.count:
            return False

        self.count = self.count + 1
        node = Node(value)

        if self.doublyLinkedListFront:
            node.next = self.doublyLinkedListFront
            self.doublyLinkedListFront.previous = node
            self.doublyLinkedListFront = node
        else:
            self.doublyLinkedListFront = node
            self.doublyLinkedListRear = node

        return True

    def insertLast(self, value: int) -> bool:
        if self.limit == self.count:
            return False
        
        self.count = self.count + 1
        node = Node(value)

        if self.doublyLinkedListRear:
            node.previous = self.doublyLinkedListRear
            self.doublyLinkedListRear.next = node
            self.doublyLinkedListRear = node
        else:
            self.doublyLinkedListFront = node
            self.doublyLinkedListRear = node

        return True

    def deleteFront(self) -> bool:
        if not self.doublyLinkedListFront:
            return False
        
        self.doublyLinkedListFront = self.doublyLinkedListFront.next
        if self.doublyLinkedListFront is not None:
            self.doublyLinkedListFront.previous = None

        if self.doublyLinkedListFront is None:
            self.doublyLinkedListRear = None
        
        self.count = self.count - 1
        
        return True

    def deleteLast(self) -> bool:
        if not self.doublyLinkedListRear:
            return False
        
        self.doublyLinkedListRear = self.doublyLinkedListRear.previous
        if self.doublyLinkedListRear is not None:
            self.doublyLinkedListRear.next = None

        if self.doublyLinkedListRear is None:
            self.doublyLinkedListFront = None
        
        self.count = self.count - 1

        return True

    def getFront(self) -> int:
        if not self.doublyLinkedListFront:
            return -1
        
        return self.doublyLinkedListFront.val
        

    def getRear(self) -> int:
        if not self.doublyLinkedListRear:
            return -1
        
        return self.doublyLinkedListRear.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.limit
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()