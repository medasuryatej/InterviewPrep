def reorderSpaces(text):
        newWord = True
        numSpaces = 0
        numWords = 0
        for eachChar in text:
            if newWord and eachChar != " ":
                numWords += 1
                newWord = False
            if eachChar == " ":
                if not newWord:
                    newWord = True
                numSpaces += 1
        # when no spaces
        if numSpaces == 0:
            return text
        # when only one word
        if numWords == 1:
            return text.strip() + " "*numSpaces
        print("numSpaces: ", numSpaces, "numWords: ", numWords)
        equalSpaces = numSpaces // (numWords-1)
        result = ""
        remaining = numSpaces
        newSpace = False
        for eachChar in text:
            if remaining < 0:
                break
            if eachChar != " ":
                result += eachChar
                newSpace = True
            else:
                if newSpace and remaining > 0:
                    result += " "*equalSpaces
                    remaining -= equalSpaces
                    newSpace = False
        # print("Remaining: ", remaining)
        if remaining > 0:
            result += " "*remaining
        print("Result length: ",len(result), " Text length: ", len(text))
        print("-"*30)
        print(f"text  : '{text}'")
        print(f"Result: '{result}'")
        # just ignore any additional stuff at end and submit remaining text
        return (result[:len(text)])

text = "    k               bwgbsqq    rhjrm    "
print(reorderSpaces(text) == "k             bwgbsqq             rhjrm ")
# print("#"*30)
"""
text = " practice   makes   perfect"
print(reorderSpaces(text) == "practice   makes   perfect ")
text = "hello   world"
print(reorderSpaces(text) == "hello   world")
text = "  walks  udp package   into  bar a"
print(reorderSpaces(text) == "walks  udp  package  into  bar  a ")
text = "a"
print(reorderSpaces(text) == "a")
"""