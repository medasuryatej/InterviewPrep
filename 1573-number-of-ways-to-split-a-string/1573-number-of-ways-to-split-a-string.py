class Solution:
    def numWays(self, s: str) -> int:
        n,ones = len(s),[]
        for i,val in enumerate(s):
            if val == '1':
                ones.append(i)
        total = len(ones)
        if total == 0:
		    # ref: https://en.wikipedia.org/wiki/Combination
			# combination of selecting 2 places to split the string out of n-1 places
            return ((n-1)*(n-2)//2) % (10**9+7) 
        if total % 3 != 0:
            return 0
        target = total // 3
        return (ones[target]-ones[target-1])*(ones[target*2]-ones[target*2-1])%(10**9+7)


class _Solution:
    def _numWays(self, s: str) -> int:
        num_ones = sum(True if bit == '1' else False for bit in s)
        if num_ones % 3 != 0:
            return 0
        if num_ones == 0 and len(s) == 3:
            return 1
        if num_ones == 0:
            num_zeros = len(s)
            return (num_zeros-2) * (num_zeros-1)//2
        partition_ones_count = num_ones // 3
        part1 = 0
        part2 = 0
        part3 = 0
        left_side = 1
        right_side = 1
        pointer = 0
        while pointer < len(s):
            if part1 == partition_ones_count:
                break
            else:
                part1 += 1 if s[pointer] == '1' else 0
            pointer += 1
        while pointer < len(s):
            if s[pointer] == '1':
                break
            else:
                left_side += 1
            pointer += 1
        while pointer < len(s):
            if part2 == partition_ones_count:
                break
            else:
                part2 += 1 if s[pointer] == '1' else 0
            pointer += 1
        while pointer < len(s):
            if s[pointer] == '1':
                break
            else:
                right_side += 1
            pointer += 1
        # print(left_side, right_side)
        return ((left_side)*(right_side)) % ((10**9)+7)
            