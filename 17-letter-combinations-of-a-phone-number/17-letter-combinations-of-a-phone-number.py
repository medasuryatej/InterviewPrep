class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        data_dict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        output = []
        if digits == "":
            return output
        digits = list(digits)
        if len(digits) == 1:
            return list(data_dict[digits[0]])
        elif len(digits) == 2:
            for first in data_dict[digits[0]]:
                s = first
                for second in data_dict[digits[1]]:
                    s += second
                    output.append(s)
                    s = first
            return output
        elif len(digits) == 3:
            for first in data_dict[digits[0]]:
                s = first
                for second in data_dict[digits[1]]:
                    s += second
                    for third in data_dict[digits[2]]:
                        s += third
                        output.append(s)
                        s = first + second
                    s = first
            return output
        else:
            for first in data_dict[digits[0]]:
                s = first
                for second in data_dict[digits[1]]:
                    s += second
                    for third in data_dict[digits[2]]:
                        s += third
                        for fourth in data_dict[digits[3]]:
                            s += fourth
                            output.append(s)
                            s = first + second + third
                        s = first + second
                    s =  first
            return output
            