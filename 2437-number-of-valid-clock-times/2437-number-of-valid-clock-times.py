class Solution:
    def countTime(self, time: str) -> int:
        output = 1
        if time[0:2] == "??":
            output *= 24
        elif time[0] == "?":
            if int(time[1]) > 3:
                output *= 2
            else:
                output *= 3
        elif time[1] == "?":
            if int(time[0]) == 2:
                output *= 4
            else:
                output *= 10
        if time[3] == "?":
            output *= 6
        if time[4] == "?":
            output *= 10
            
        return output