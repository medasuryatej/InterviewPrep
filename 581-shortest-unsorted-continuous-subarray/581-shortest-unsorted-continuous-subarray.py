class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        # NlogN solution
        
        sorted_nums = sorted(nums)
        start = len(nums)-1
        end = 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = min(start, i)
                end = max(end, i)
        return end - start + 1 if end - start > 0 else 0
        """
        minE = float("inf")
        maxE = float("-inf")
        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                flag = True
            if flag:
                minE = min(minE, nums[i])
                
        flag = False
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                flag = True
            if flag:
                maxE = max(maxE, nums[i])
            
        for i in range(0, len(nums)):
            if minE < nums[i]:
                break
                
        for j in range(len(nums)-1, -1, -1):
            if maxE > nums[j]:
                break
        return j - i + 1 if j - i > 0 else 0