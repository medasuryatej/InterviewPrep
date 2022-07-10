class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [i for i in range(1, 1001)]
        heapq.heapify(self.nums)
        self.pop = set()
        

    def popSmallest(self) -> int:
        small = heapq.heappop(self.nums)
        self.pop.add(small)
        return small
        

    def addBack(self, num: int) -> None:
        if num in self.pop:
            self.pop.remove(num)
            heapq.heappush(self.nums, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)