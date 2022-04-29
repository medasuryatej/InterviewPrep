class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # adj_list = defaultdict(list)
        DEFAULT_COLOR = 0
        MODIFIED_COLOR = 1
        
        # for idx, adjNodes in enumerate(graph):
        #    adj_list[idx].extend(adjNodes)
            
        # for idx in adj_list:
        #    print(idx, adj_list[idx])
        numNodes = len(graph)
        
        nodeColors = [0] * numNodes
        
        for nodeIdx in range(numNodes):
            if (nodeColors[nodeIdx] == DEFAULT_COLOR):
                if not self.isValidColoring(graph, nodeColors, MODIFIED_COLOR, nodeIdx):
                    return False
            
        return True
    
    def isValidColoring(self, graph, nodeColors, ALT_COLOR, nodeIdx):
        
        if nodeColors[nodeIdx] != 0:
            return nodeColors[nodeIdx] == ALT_COLOR
        
        nodeColors[nodeIdx] = ALT_COLOR
        
        for adjNode in graph[nodeIdx]:
            if not self.isValidColoring(graph, nodeColors, ALT_COLOR * -1, adjNode):
                return False
            
        return True