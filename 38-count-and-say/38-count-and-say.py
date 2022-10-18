class Solution:
    def countAndSay(self, n: int) -> str:
        dataMap = {}
        dataMap[1] = "1"
        dataMap[2] = "11"
        dataMap[3] = "21"
        dataMap[4] = "1211"
        for i in range(5,n+1,1):
            groupedNums = self.groupNums(dataMap[i-1])
            countAndSay = []
            for each in groupedNums:
                countAndSay.extend([str(len(each)), each[0]])
            dataMap[i] = "".join(countAndSay)
        return dataMap[n]
    
    def groupNums(self, string):
        output =[]
        stack = []
        for each in string:
            if not stack:
                stack.append(each)
            elif stack[-1] != each:
                output.append("".join(stack))
                stack = [each]
            else:
                stack.append(each)
        output.append("".join(stack))
        return output
        