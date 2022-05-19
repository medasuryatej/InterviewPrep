class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = -1
        
        for i in range(0, len(num)-2, 1):
            subStr = num[i:i+3]
            if len(set(subStr)) == 1:
                result = max(result, int(subStr))
                
        if result == -1:
            return ""
        elif result == 0:
            return "000"
        else:
            return str(result)
        