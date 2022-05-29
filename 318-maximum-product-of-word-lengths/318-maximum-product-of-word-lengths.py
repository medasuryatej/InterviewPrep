class Solution:
    def maxProduct(self, words: List[str]) -> int:
        import string
        charMap = {char: i for i, char in enumerate(string.ascii_lowercase)}
        wordMap = {}
        for word in words:
            wordMap[word] = [0] * 26
            for char in word:
                wordMap[word][charMap[char]] = 1
                
        max_prod = 0
        
        for i in range(len(words)-1):
            l_word = wordMap[words[i]]
            l_sum = len(words[i])
            for j in range(i+1, len(words)):
                r_word = wordMap[words[j]]
                r_sum = len(words[j])
                include = True
                for a,b in zip(l_word, r_word):
                    if a and b:
                        include = False
                        break
                if include:
                    # print(words[i], words[j])
                    max_prod = max(max_prod, l_sum * r_sum )
                    
        return max_prod