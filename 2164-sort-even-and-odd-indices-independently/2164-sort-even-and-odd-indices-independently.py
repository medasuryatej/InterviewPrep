class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for i in range(len(nums)):
            if i % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        evens.sort()
        odds.sort(reverse=True)
        output = []
        for x,y in zip(evens, odds):
            output.append(x)
            output.append(y)
            
        if len(nums) % 2 != 0:
            output.append(evens[-1])
            
        return output