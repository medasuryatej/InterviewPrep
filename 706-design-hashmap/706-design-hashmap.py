class Node:
    def __init__(self, key, value, nextNode=None):
        self.key = key
        self.value = value
        self.next = nextNode
        
class Bucket:
    def __init__(self):
        self.head = Node(float("-inf"),float("-inf"))
        
    def insert(self, newKey, newValue):
        # just create a new node
        self.delete(newKey)
        newNode = Node(newKey, newValue, self.head.next)
        # reposition head to the newly created node
        self.head.next = newNode
        
    def exists(self, newKey):
        curr = self.head.next
        while curr is not None:
            if curr.key == newKey:
                return curr.value
            curr = curr.next
        return -1
    
    def delete(self, newKey):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.key == newKey:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

class MyHashMap:

    def __init__(self):
        self.keyRange = 967
        self.buckRange = [Bucket() for i in range(self.keyRange)]
        
        
    def _hash(self, val):
        return val % self.keyRange
        

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        self.buckRange[index].insert(key, value)
        return None
        

    def get(self, key: int) -> int:
        index = self._hash(key)
        return self.buckRange[index].exists(key)
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        return self.buckRange[index].delete(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)