class Solution:
    def largestPalindromic(self, num: str) -> str:
        if num.strip("0") == "":
            return "0"
        counter = Counter(num)
        evens, oddNum, oddFreq = [], -1, -1
        for num, freq in counter.items():
            num = int(num)
            if freq % 2 == 0:
                evens.extend([num]*(freq//2))
            else:
                if num > oddNum:
                    oddNum = num
                evens.extend([num]*((freq-1)//2))
        revSort = sorted(evens, reverse=True)
        forSort = sorted(evens)
        if oddNum > -1:
            return ("".join(map(str, revSort)) + f"{oddNum}" + "".join(map(str, forSort))).strip("0")
        else:
            return ("".join(map(str, revSort))  + "".join(map(str, forSort))).strip("0")