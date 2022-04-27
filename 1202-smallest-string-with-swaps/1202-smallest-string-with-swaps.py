class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        adj_list = defaultdict(list)
        result = list(s)
        visited = [False for char in range(len(s))]
        
        # build the adjacency list
        for x,y in pairs:
            adj_list[x].append(y)
            adj_list[y].append(x)
            
        def dfs(char_list, index, chars, indices):
            if visited[index]:
                return 
            chars.append(char_list[index])
            indices.append(index)
            visited[index] = True
            
            for neighbor in adj_list[index]:
                dfs(char_list, neighbor, chars, indices)
            
            
        for i in range(len(s)):
            if not visited[i]:
                # if a node is not yet visited
                chars = []
                indices = []
                dfs(result, i, chars, indices)
                
                chars.sort()
                indices.sort()
                
                for c, i in zip(chars, indices):
                    result[i] = c
                    
        return "".join(result)