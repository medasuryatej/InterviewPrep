class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        cache = set()
        wordMap = set(words)
        if "" in wordMap:
            wordMap.remove("")
        result = []
        
        def canConcat(word):
            if word in cache:
                return True
            
            for i in range(len(word)):
                left = word[:i]
                right = word[i:]
                if left in wordMap and (right in wordMap or canConcat(right)):
                    cache.add(word)
                    return True
            return False
        
        
        for word in words:
            if canConcat(word):
                result.append(word)
        return result
     