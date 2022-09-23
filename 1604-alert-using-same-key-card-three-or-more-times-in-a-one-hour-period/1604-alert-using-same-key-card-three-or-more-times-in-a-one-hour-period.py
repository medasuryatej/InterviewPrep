class Solution:
    def getTime(self, hr24format):
        hours, mins = hr24format.split(":")
        return int(hours)*60 + int(mins)
    
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        userMap = defaultdict(list)
        for user, time in zip(keyName, keyTime):
            userMap[user].append(self.getTime(time))
            
        output = []
        
        for user in userMap:
            entries = sorted(userMap[user]) # need to sort if required
            # print(user, entries)
            for i in range(len(entries)-2):
                minTime = entries[i] + 60
                if entries[i+1] <= minTime and entries[i+2] <= minTime:
                    output.append(user)
                    break
                    
        return sorted(output)
                
        