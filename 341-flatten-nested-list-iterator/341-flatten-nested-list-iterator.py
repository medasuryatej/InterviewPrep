class NestedIterator(object):
    # referred solutions

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        
        self.queue = collections.deque(nestedList)
        
    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.queue:
            if self.queue[0].isInteger():
                return True
            first = self.queue.popleft()
            self.queue.extendleft(first.getList()[::-1])
        return False