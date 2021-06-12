class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        database = {}
        for eachPath in paths:
            subPaths = eachPath.split(" ")
            directory = subPaths[0]
            for eachFile in subPaths[1:]:
                content = eachFile[eachFile.index("(") + 1:-1]
                if content not in database:
                    database[content] = [directory + "/" + eachFile[:eachFile.index("(")]]
                else:
                    database[content].extend([directory + "/" + eachFile[:eachFile.index("(")]])
        return [ duplicates for duplicates in database.values() if len(duplicates) > 1 ] 