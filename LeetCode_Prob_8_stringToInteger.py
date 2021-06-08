class Solution:
    def myAtoi(self, s: str) -> int:
        result = []
        inrange = [-1*2**31, 2**31-1]
        # strip unwanted front space
        s = s.lstrip()
        if len(s) == 0:
            return 0
        # flag to see signbit
        seen = False
        # flag to check if character is signed or unsigned
        signed = False
        firstchar = s[0]
        if firstchar in ["-", "+"] or firstchar.isnumeric():
            if firstchar == "-":
                signed = True
                s = s[1:]
            else:
                if firstchar == "+":
                    s = s[1:]
                signed = False
            for eachChar in s:
                if eachChar.isnumeric():
                    result.append(eachChar)
                else:
                    break
            if len(result) == 0:
                return 0
            if signed:
                result = -1*int("".join(result))
            else:
                result = int("".join(result))
            if result > inrange[1]:
                return inrange[1]
            elif result < inrange[0]:
                return inrange[0]
            else:
                return result
        else:
            # indicating starting character is a word
            return 0