class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dataMap = {}
        counter = 0
        from collections import defaultdict
        for item in zip(*items):
            if counter == 0:
                key = "type"
            elif counter == 1:
                key = "color"
            else:
                key = "name"
            dataMap[key] = defaultdict(int)
            for _it in item:
                dataMap[key][_it] += 1
            counter += 1
        return dataMap[ruleKey][ruleValue]
