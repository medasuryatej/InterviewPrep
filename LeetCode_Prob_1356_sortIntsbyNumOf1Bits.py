class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # first sort the array
        arr = sorted(arr)
        # sort based on count of 1's in each element of array
        return sorted(arr, key=lambda x: bin(x).count("1"))