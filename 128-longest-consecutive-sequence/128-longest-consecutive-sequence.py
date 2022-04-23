class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if no numbers are in list
        if not nums:
            # longest seq is zero
            return 0
        # output default initialiation to neg infinity
        result = float("-inf")
        # creating a set of given numbers for O(1) lookup
        givenNums = set(nums)
        # keep track of visited nums 
        visited = set()
        # iterate over numbers
        for num in nums:
            # reset counter to 1
            counter = 1
            # temporary var for lookups on left and rightside
            temp = num
            # if number is already visited nothing to do
            if num in visited:
                continue
            # lookup on left
            while temp - 1 in givenNums:
                # add number to visited
                visited.add(temp-1)
                # further left lookup
                temp -= 1
                # update counter
                counter += 1
            # reassignemnet for right side lookup
            temp = num
            # lookup now on right side
            while temp + 1 in givenNums:
                # add number to visited
                visited.add(temp+1)
                # further right lookup
                temp += 1
                # increment counter
                counter += 1
            # update result with max of current result and counter
            result = max(result, counter)
        # return answer
        return result