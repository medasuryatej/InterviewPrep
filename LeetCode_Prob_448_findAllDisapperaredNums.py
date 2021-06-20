def findDisappearedNumbers(nums):
        for i in range(0, len(nums)):
            nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1]) * -1
            print(nums)
        output = []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                output.append(i+1)
        return output
nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))