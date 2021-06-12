class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list("AEIOU") + list("AEIOU".lower())
        pointer = len(s) - 1
        result = ""
        for eachChar in s:
            # consonant
            if eachChar not in vowels:
                result += eachChar
            else:
                for j in range(pointer, -1, -1):
                    if s[j] in vowels:
                        result += s[j]
                        pointer = j-1
                        break
        return result