class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for s,e in intervals:
            start.append(s)
            end.append(e)
            
        start.sort()
        end.sort()
        
        minRooms = 0
        result = 0
        
        left,right = 0,0
        while left < len(start):
            if start[left] <= end[right]:
                minRooms += 1
                left += 1
            else:
                right += 1
                minRooms -= 1
            
            result = max(result, minRooms)
            
        return result