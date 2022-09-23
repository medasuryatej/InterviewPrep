class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        trie = dict()
        for dom in cpdomains:
            _, domain = dom.split(" ")
            visit_count = int(_)
            node = trie
            
            for subd in domain.split(".")[::-1]:
                if subd not in node:
                    node[subd] = {"#" : visit_count}
                else:
                    node[subd]["#"] += visit_count
                node = node[subd]
                
            
        que = deque([([key], value) for key, value in trie.items()])

        result = []

        while que:
            size = len(que)
            for i in range(size):
                prefix, node = que.popleft()
                if prefix[-1] == "#":
                    subd = ".".join(prefix[:-1][::-1])
                    result.append(f"{node} {subd}")
                else:
                    for key, val in node.items():
                        que.append((prefix + [key], val))
                            
        return result
                    