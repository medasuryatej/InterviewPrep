def minimumLengthEncoding(words):
        result = ""
        for eachword in words:
            if result.endswith(eachword):
                pass
            else:
                result += "#" + eachword
        result += "#"
        # print(result)
        return len(result[1:])

# words = ["time", "me", "bell"]
words = ["t"]
print(minimumLengthEncoding(words))