import heapq
class Solution:
    def mostBooked(self, n, meetings):
        ready = [r for r in range(n)]
        rooms = []
        heapify(ready)
        res = [0] * n
        for s,e in sorted(meetings):
            while rooms and rooms[0][0] <= s:
                t,r = heappop(rooms)
                heappush(ready, r)
            if ready:
                r = heappop(ready)
                heappush(rooms, [e, r])
            else:
                t,r = heappop(rooms)
                heappush(rooms, [t + e - s, r])
            res[r] += 1
        return res.index(max(res))
    
    def _mostBooked_mycode(self, n: int, meetings: List[List[int]]) -> int:
        meeting_time_room_map = {} # tuple : int
        room_usage = [0] * n
        rooms_minheap = [i for i in range(n)]
        heapq.heapify(rooms_minheap) # needed for retrieving lowest room number
        
        heapq.heapify(meetings) # need to retrieve the meetings with earlier start time
        
        meetings_finished_minheap = []
        heapq.heapify(meetings_finished_minheap) # needed for retrieving the room number that is finished
        
        counter = 0
        num_meetings = len(meetings)
        offset = 0
        time_delta = 0
        
        while counter < num_meetings:
            if not meetings:
                break
            # rooms available
            while rooms_minheap:
                room_allocated = heapq.heappop(rooms_minheap)
                room_usage[room_allocated] += 1
                if not meetings:
                    break
                meeting_started = heapq.heappop(meetings)
                counter += 1
                
                if offset != 0 and offset > meeting_started[0] :
                    time_delta = offset - meeting_started[0]
                    # print("delta: ", time_delta)
                heapq.heappush(meetings_finished_minheap, (time_delta + meeting_started[1], time_delta + meeting_started[0]))
                meeting_time_room_map[(time_delta + meeting_started[0], time_delta + meeting_started[1])] = room_allocated
            
                
            # rooms not available
            completed_meeting = heapq.heappop(meetings_finished_minheap)
            room_that_got_used = meeting_time_room_map[(completed_meeting[1], completed_meeting[0])]
            heapq.heappush(rooms_minheap, room_that_got_used)
            offset = completed_meeting[0]
            
            # pop until the start time of current meeting is greater than end times of map
            # current_meeting_start = meetings[counter][0]
            # while meetings_finished_minheap and current_meeting_start > meetings_finished_minheap[0][0]:
            #     completed_meeting = heapq.heappop(meetings_finished_minheap)
            #     offset = max(offset, completed_meeting[0])
            #     room_that_got_used = meeting_time_room_map[(completed_meeting[1], completed_meeting[0])]
            #     heapq.heappush(rooms_minheap, room_that_got_used)
                
            
            # print("Offset", offset)
            
        # min_room_num, max_room_used = float("inf"), float("-inf")
        print(room_usage)
        
                
        return room_usage.index(max(room_usage))
        
        