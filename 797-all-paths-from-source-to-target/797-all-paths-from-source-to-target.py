class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_paths = []
        
        destination = len(graph) - 1
        
        def backtrack(currentNode, currentPath):
            if currentNode == destination:
                # once we reached end node, store the current path
                all_paths.append(currentPath.copy())
                return
            
            for neighbor in graph[currentNode]:
                backtrack(neighbor, currentPath + [neighbor])
                
            
                
        backtrack(0, [0])
        
        return all_paths