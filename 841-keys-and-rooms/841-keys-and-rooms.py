class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        visit.add(0)
        
        q = [0]
        
        while q:
            top = q.pop(0)
            for neigh in rooms[top]:
                if neigh not in visit:
                    visit.add(neigh)
                    q.append(neigh)
                    
        return len(visit) == len(rooms)