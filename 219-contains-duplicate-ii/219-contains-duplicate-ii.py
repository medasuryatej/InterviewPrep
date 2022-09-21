class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = defaultdict(list)
        for index, num in enumerate(nums):
            hmap[num].append(index)
            
        for key, freq in hmap.items():
            if len(freq) == 1:
                continue
            for i in range(len(freq)-1):
                if abs(freq[i] - freq[i+1]) <= k:
                    return True
                
        return False