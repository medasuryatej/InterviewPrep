class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import string
        lower_case = string.ascii_lowercase
        alpha_map = {}
        for eachStr in strs:
            alpha_count = [0]*26
            for eachChar in eachStr:
                alpha_count[lower_case.index(eachChar)] += 1
            alpha_map[tuple(alpha_count)] = alpha_map.get(tuple(alpha_count), []) + [eachStr]
        result = []
        return alpha_map.values()
        
        