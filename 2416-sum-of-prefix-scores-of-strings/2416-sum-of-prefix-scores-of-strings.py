from collections import defaultdict, Counter

class TrieNode:
    def __init__(self, nodeVal=""):
        self.data = nodeVal
        self.children = defaultdict()
        self.end = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode("")
        
    def insert(self, word, freq):
        curr = self.root
        
        for eachChar in word:
            if eachChar in curr.children:
                curr = curr.children[eachChar]
            else:
                nn = TrieNode(eachChar)
                curr.children[eachChar] = nn
                curr = nn
        curr.end = freq
        # print("Insert success")
        
    def search(self, word):
        count = 0
        curr = self.root
        flag = True
        
        for eachChar in word:
            if eachChar not in curr.children:
                flag = False
                break
            curr = curr.children[eachChar]
        if flag:
            branches = []
            self.numBranches(curr, branches)
            # print(word, branches)
            count += sum(branches)
        return count
    
    def numBranches(self, node, branches):
        if node.end > 0:
            # branches.extend([prefix]*node.end)
            branches.append(node.end)
            
        for eachChild in node.children:
            self.numBranches(node.children[eachChild], branches)
            
    def printTrie(self):
        curr = self.root
        def recursivePrint(node):
            # for nnode in node.children:
            #     print(node[nnode].children)
            #     recursivePrint(nnode)
            for nnode in node.children:
                # print(nnode)
                recursivePrint(node.children[nnode])
                
        recursivePrint(curr)
                
        
        

class _Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        cache = {}
        trie = Trie()
        counter = Counter(words)
        # construct trie
        for word, freq in counter.items():
            trie.insert(word, freq)
            
        # print("printing data", trie, trie.root.data, trie.root.children)
        # trie.printTrie()
            
        output = []
        seenmap = {}
        for word in words:
            if word in seenmap:
                output.append(seenmap[word])
                continue
            curSum = 0
            for i in range(len(word)):
                subStr = word[:i+1]
                if subStr in cache:
                    curSum += cache[subStr]
                else:
                    cache[subStr] = trie.search(subStr)
                    curSum += cache[subStr]
                    
            output.append(curSum)
            seenmap[word] = curSum
            
        return output
    
class TrieNode:
    def __init__(self):
        self.next = {}
        self.score = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        result = []
        
        root = TrieNode()
        
        # build the trie
        for i, word in enumerate(words):
            node = root
            for j, c in enumerate(word):
                if c not in node.next:
                    node.next[c] = TrieNode()
                node.next[c].score += 1
                node = node.next[c]
        
        # get the scores
        for i, word in enumerate(words):
            node = root
            sum_score = 0
            for j, c in enumerate(word):
                sum_score += node.score
                node = node.next[c]
            sum_score += node.score
            result.append(sum_score)
        
        return result
        