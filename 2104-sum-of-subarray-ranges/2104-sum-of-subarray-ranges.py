class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def minSum(arr):
            # referred youtube
            MOD = 10**9 + 7
            numEle = len(arr)
            previousLess = [-1] * numEle
            result = [0] * numEle

            monStack = []
            top = -1

            for i in range(numEle):
                while monStack and arr[monStack[top]] > arr[i]:
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
            # print(result)
            # print(sum(result))
            return sum(result)
        
        def maxSum(arr):
            # referred youtube
            MOD = 10**9 + 7
            numEle = len(arr)
            previousLess = [-1] * numEle
            result = [0] * numEle

            monStack = []
            top = -1

            for i in range(numEle):
                while monStack and arr[monStack[top]] < arr[i]:
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
            # print(result)
            # print(sum(result))
            return sum(result)
        
        return maxSum(nums) - minSum(nums)