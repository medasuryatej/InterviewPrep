class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # create a dict of knowledge base
        dataMap = {value[0]:value[1] for value in knowledge}
        pointer = 0
        result = ""
        # parse until end of string is reached
        while pointer < len(s):
            # until ( is seen add chars to result
            if s[pointer] != "(":
                result += s[pointer]
                pointer += 1
            else:
                temp = ""
                pointer += 1
                # when ( is seen create a temp of chars until ) is seen
                while s[pointer] != ")":
                    temp += s[pointer]
                    pointer += 1
                # if temp not in dataMap replace value with ?
                result += dataMap[temp] if temp in dataMap else "?"
                pointer += 1
                temp = ""
        return result