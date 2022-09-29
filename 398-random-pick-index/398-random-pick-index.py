import random
from collections import defaultdict
class Solution:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        self.cmap = defaultdict(list)
        self.updateMap()
        
    def updateMap(self):
        for i in range(len(self.nums)):
            self.cmap[self.nums[i]].append(i)
        

    def pick(self, target: int) -> int:
        return self.cmap[target][random.randint(0, len(self.cmap[target]) - 1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)