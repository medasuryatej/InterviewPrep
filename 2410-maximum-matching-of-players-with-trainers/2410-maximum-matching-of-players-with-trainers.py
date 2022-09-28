class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        heapq.heapify(players)
        heapq.heapify(trainers)
        output = 0
        while players and trainers:
            # print(players, trainers)
            top = heapq.heappop(players)
            while trainers and top > trainers[0]:
                heapq.heappop(trainers)
            if trainers:
                heapq.heappop(trainers)
                output += 1
            
        return output