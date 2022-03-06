class Solution:
    """
    0 1 2  - From 0th slot you can swap to 1st or 3rd pos
    3 4 5    From 1st slot you can swap to 2nd or 0th or 4rth pos and so on
    """
    moveMapper = {
        0: [1,3],
        1: [0,2,4],
        2: [1,5],
        3: [0,4],
        4: [1,3,5],
        5: [2,4]
    }
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # given starting string
        starting = ""
        for row in board:
            for num in row:
                starting += str(num)
                
        # print(starting)
        # perform bfs from the starting move
        query = [starting]
        moves = 0 # increment moves
        visited = [] # keep track of visited moves
        
        # bfs
        while query:
            size = len(query)
            # for number of moves at a current level
            for i in range(size):
                top = query.pop(0)
                # if reached solution return num moves
                if top == "123450":
                    return moves
                # traverse
                self.traverse(top, visited, query)
            moves += 1
        # havent found a solution
        return -1
    
    def traverse(self, move, visited, query):
        # get the empty slot index
        zero_pos = move.index("0")
        # how many places can we move?
        for direction in self.moveMapper[zero_pos]:
            new_move = self.swap_positions(move, zero_pos, direction)
            # if a move is already visited continue to next possible move
            if new_move not in visited:
                query.append(new_move)
                # mark a move as visited
                visited.append(new_move)
                
    def swap_positions(self, move, from_pos, to_pos):
        # swap the slots
        string_list = list(move)
        string_list[from_pos], string_list[to_pos] = string_list[to_pos], string_list[from_pos]
        return "".join(string_list)
