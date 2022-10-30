class Solution:
    def digitSum(self, num):
        tsum = 0
        while num > 0:
            div, mod = divmod(num, 10)
            tsum += mod
            num = div
        return tsum
    def convertToInt(self, numStrList, flag):
        # print(numStrList, flag)
        return int("".join(numStrList))
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        # print(self.digitSum(467))
        numLen = len(str(n))
        temp = ['0'] + ['0'] * numLen
        root = n
        while self.digitSum(n) > target:
            curNum = ['0']+ list(str(n))
            for i in range(len(curNum)-1, -1, -1):
                if curNum[i] != '0':
                    temp[i] = str(10 - int(curNum[i]))
                    break
            n = root + self.convertToInt(temp, "temp")
            # print("n value: ", n)
        
        return self.convertToInt(temp, "temp")