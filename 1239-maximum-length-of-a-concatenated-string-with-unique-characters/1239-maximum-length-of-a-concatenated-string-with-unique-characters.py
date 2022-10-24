class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = [set()]
        for eachString in arr:
            s_set = set(eachString)
            if len(s_set) < len(eachString):
                # duplicate chars
                continue
            for eachSet in result[:]:
                if s_set & eachSet:
                    # duplicate characts amongst set
                    continue
                result.append(s_set | eachSet)
        
        return max([len(each) for each in result])
        