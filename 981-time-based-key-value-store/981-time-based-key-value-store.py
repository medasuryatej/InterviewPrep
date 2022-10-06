class TimeMap:

    def __init__(self):
        self.hm = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[f"{key}_{timestamp}"] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if f"{key}_{timestamp}" in self.hm:
            return self.hm[f"{key}_{timestamp}"]
        while timestamp > 0:
            timestamp -= 1
            if f"{key}_{timestamp}" in self.hm:
                return self.hm[f"{key}_{timestamp}"]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)