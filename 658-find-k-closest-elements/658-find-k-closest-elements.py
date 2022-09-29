import heapq as hq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        k_elements = []
        hq.heapify(k_elements)
        for each in arr:
            if len(k_elements) < k:
                hq.heappush(k_elements, (-1 * (abs(x - each)), each))
                continue
            curDiff = abs(x - each)
            if curDiff < -1 * k_elements[0][0]:
                hq.heappop(k_elements)
                hq.heappush(k_elements, (-1 * curDiff, each))
                
        # print(k_elements)
        output = []
        for each in k_elements:
            output.append(each[1])
        return sorted(output)