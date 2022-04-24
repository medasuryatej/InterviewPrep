class User:
    def __init__(self, id, source, time):
        self.id = id
        self.src = source
        self.time = time
        
class UndergroundSystem:

    def __init__(self):
        self.userMap =  {} # id: {"source": time}
        self.source_dest_map = defaultdict(list) # souce-dest: [time]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.userMap[id] = User(id, stationName, t)
        return None
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        srcName = self.userMap[id].src
        srcTime = self.userMap[id].time
        self.source_dest_map[f"{srcName}-{stationName}"].append(t-srcTime)
        return None
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.source_dest_map[f"{startStation}-{endStation}"]
        return sum(times) / len(times)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)