class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        def getAnagram(word):
            l = [0] * 26
            for char in word:
                l[ord(char) - ord('a')] += 1
            return l
        prev = []
        for word in words:
            if not stack:
                prev = getAnagram(word)
                stack.append(word)
            cur = getAnagram(word)
            if cur == prev:
                continue
            else:
                prev = cur
                stack.append(word)
        return stack