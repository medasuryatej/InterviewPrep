class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # referred solution
        result = 0
        while len(arr) > 1:
            # find the index of minimum element
            index = arr.index(min(arr))
            # index in bounds
            if 0 < index < len(arr) - 1:
                # current element into min of its neighbors
                result += arr[index] * min(arr[index-1], arr[index+1])
            else:
                # either of the bordes
                result += arr[index] * (arr[index+1] if index==0 else arr[index-1])
            arr.pop(index)
        return result