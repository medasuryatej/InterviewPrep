def firstUniqChar(s):
        from collections import OrderedDict
        dataMap = OrderedDict()
        visited = set()
        for index, char in enumerate(s):
            if char not in dataMap:
                dataMap[char] = index
            else:
                visited.add(char)
                del dataMap[char]
        print(dataMap)
        for key, value in dataMap.items():
            if key not in visited:
                return value
        return -1

s = "aadadaad"
print(firstUniqChar(s))