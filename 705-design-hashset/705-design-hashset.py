class Node:
    def __init__(self, value, nextNode=None):
        self.val = value
        self.next = nextNode
        
class Bucket:
    def __init__(self):
        self.head = Node(0)
        
    def insert(self, newValue):
        # if value doesn't exists add to the linear probing chain
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            self.head.next = newNode
    def exists(self, newValue):
        curr = self.head.next
        while curr is not None:
            if curr.val == newValue:
                return True
            curr = curr.next
        return False
    def delete(self, newValue):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.val == newValue:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

class MyHashSet:

    def __init__(self):
        self.keyRange = 987
        self.buckRange = [Bucket() for i in range(self.keyRange)]
    
    def _hashPos(self, val):
        return val % self.keyRange

    def add(self, key: int) -> None:
        # find the bucket where we can put the value
        index = self._hashPos(key)
        # do linear probing and insert the value
        self.buckRange[index].insert(key)
        
    def remove(self, key: int) -> None:
        index = self._hashPos(key)
        self.buckRange[index].delete(key)
        

    def contains(self, key: int) -> bool:
        index = self._hashPos(key)
        return self.buckRange[index].exists(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)