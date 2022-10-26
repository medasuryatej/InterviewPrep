class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def getInMins(timstr):
            hrs, mins = map(int, timstr.split(":"))
            return hrs * 60 + mins
        
        event1 = getInMins(event1[0]), getInMins(event1[1])
        event2 = getInMins(event2[0]), getInMins(event2[1])
        if event1[0] < event2[0]:
            pass
        else:
            event2, event1 = event1, event2
            
        a,b = event1
        c,d = event2
        if c > b:
            return False
        return True