class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        modes, occurs = self.mode(nums)
        minLength = float("inf")
        for maxRepNum, maxRepFreq in zip(modes, occurs):
            output = []
            counter = 0
            firstOccur = False
            for num in nums:
                if firstOccur and counter < maxRepFreq:
                    output.append(num)
                    if num == maxRepNum:
                        counter += 1
                elif counter >= maxRepFreq:
                    break
                if num == maxRepNum and not firstOccur:
                    counter += 1
                    output.append(num)
                    firstOccur = True
            minLength = min(minLength, len(output))
        return minLength
    
    def mode(self, num_list):
        from collections import Counter
        max_value = float('-inf')
        maxes = None
        counter = Counter(num_list)
        for key, value in counter.items():
            if value == max_value:
                maxes.add(key)
            elif value > max_value:
                max_value = value
                maxes = {key}
        return maxes, [counter[occ] for occ in maxes]
