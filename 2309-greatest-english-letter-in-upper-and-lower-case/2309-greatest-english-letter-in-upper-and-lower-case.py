class Solution:
    def greatestLetter(self, s: str) -> str:
        small = [False] * 26
        captal = [False] * 26
        for eachChar in s:
            index = ord(eachChar)
            if 65 <= index <= 90:
                captal[index - ord("A")] = True
            else:
                small[index - ord("a")] = True
                
        # print(small)
        # print(captal)
        
        caps = string.ascii_uppercase
        ind = 0
        for sm, cap in zip(captal[::-1], small[::-1]):
            if sm and cap:
                return caps[26 - ind - 1]
            ind += 1
        return ""