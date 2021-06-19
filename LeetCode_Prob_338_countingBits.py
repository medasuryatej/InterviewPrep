class Solution:
    def countBits(self, n: int) -> List[int]:
    	# in any given number N, it contains same number of 1 as its 2N
    	# hence a number i is same as i//2 plus a one if i is odd.
        counter = [0]
        for i in range(1, n+1):
            counter.append(counter[i>>1] + i%2)
        return counter