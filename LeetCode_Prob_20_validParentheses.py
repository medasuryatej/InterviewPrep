class Solution:
    def isValid(self, s: str) -> bool:
        temp = ""
        st = []
        open = ["[", "{", "("]
        closed = ["]", "}", ")"]
        for eachChar in s:
            if eachChar in open:
                st.append(eachChar)
            else:
                if (len(st) == 0):
                    return False
                temp = st.pop()
                if not self.match(temp, eachChar, open, closed):
                    return False
        if len(st)>0:
            return False
        return True
    def match(self, tempChar, eachChar, open, closed):
        if open.index(tempChar) == closed.index(eachChar):
            return True
        else:
            return False