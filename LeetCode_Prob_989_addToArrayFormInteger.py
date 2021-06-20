class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        value,n = 0, len(num)
        for i in range(0, n):
            value += num[i]*10**(n-i-1)
        output = value + k
        return [int(val) for val in str(output)]
        