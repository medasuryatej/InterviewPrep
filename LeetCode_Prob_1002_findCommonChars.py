class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        wordList = [Counter(word) for word in words]
        output = wordList[0]
        for j in range(1, len(wordList)):
            output &= wordList[j]
        return output.elements()