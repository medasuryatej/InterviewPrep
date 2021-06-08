def decompressRLElist(nums):
        result = []
        for i in range(1, len(nums), 2):
            result.extend([nums[i]]*nums[i-1])
        return result

def decompressRLEURL(nums):
        result = []
        for i in range(1, len(nums), 2):
            result.extend([nums[i-1]]*int(nums[i]))
        return result
nums = "h1t2p1s1:1/2l1e2t1c1o1d1e1.1c1o1m1/1p1r1o1b1l1e1m1s1/1d1e1s1i1g1n1-1t1i1n1y1u1r1l1"
print("".join(decompressRLEURL(nums)))

nums = "h1t2p1:1/2g1o59g1l1e1.1c1o1m1/1"
