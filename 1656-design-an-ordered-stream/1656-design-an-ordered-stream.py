class OrderedStream:

    def __init__(self, n: int):
        self.stream = defaultdict(str)
        self.stream_ids = []
        heapq.heapify(self.stream_ids)
        self.start = 1
        return None

    def insert(self, idKey: int, value: str) -> List[str]:
        # insert data
        self.stream[idKey] = value
        heapq.heappush(self.stream_ids, idKey)
        top = self.stream_ids[0]
        if top > self.start:
            # we don't have smaller ID yet
            return []
        topPop = heapq.heappop(self.stream_ids)
        poppedVals = [topPop]
        while self.stream_ids and self.stream_ids[0] - topPop == 1:
            topPop = heapq.heappop(self.stream_ids)
            poppedVals.append(topPop)
            
        output = []
        for val in poppedVals:
            output.append(self.stream[val])
        self.start += len(poppedVals)
        
        return output
            
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)