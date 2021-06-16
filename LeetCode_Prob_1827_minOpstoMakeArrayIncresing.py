def minOperations(nums):
        count = 0
        if len(nums) == 1:
            return count
        for i in range(1, len(nums)):
            # print(count, nums[i], nums)
            if nums[i] > nums[i-1]:
                # if strictly increasing nothing to do
                continue
            elif nums[i] == nums[i-1]:
                # exactly equal to increment by 1
                nums[i] += 1
                count += 1
            else:
                count += abs(nums[i] - nums[i-1]) + 1
                nums[i] += abs(nums[i] - nums[i-1]) + 1
        # print(nums)
        return count

nums = [1,5,2,4,1]
print(minOperations(nums))