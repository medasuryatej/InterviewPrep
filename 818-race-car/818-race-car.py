from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        visited = set()
        que = deque([(0, 0, 1)]) # moves, pos, speed
        
        while que:
            moves, pos, speed = que.popleft()
            
            if pos == target:
                return moves
            
            if (pos, speed) in visited:
                continue
                
            visited.add((pos, speed))
            que.append((moves+1, pos + speed, speed*2))
            
            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                que.append((moves+1, pos, -1 if speed > 0 else 1))