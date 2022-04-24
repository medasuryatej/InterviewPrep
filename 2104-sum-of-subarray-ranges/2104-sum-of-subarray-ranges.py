import operator
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def max_min_sum(arr, operation):
            numEle = len(arr)
            previousLess = [-1] * numEle
            result = [0] * numEle

            monStack = []
            top = -1

            for i in range(numEle):
                # while monStack and arr[monStack[top]] > arr[i]:  # change size from > to < for finding maxSum
                while monStack and operation(arr[monStack[top]], arr[i]):
                    monStack.pop()

                if monStack:
                    previousLess[i] = monStack[top]
                monStack.append(i)

            # print(previousLess)
            for i in range(numEle):
                if previousLess[i] != -1:
                    result[i] = result[previousLess[i]] + \
                            (i - previousLess[i]) * arr[i]
                else:
                    result[i] = (i - previousLess[i]) * arr[i]
            return sum(result)
        
        return max_min_sum(nums, operator.lt) - max_min_sum(nums, operator.gt)