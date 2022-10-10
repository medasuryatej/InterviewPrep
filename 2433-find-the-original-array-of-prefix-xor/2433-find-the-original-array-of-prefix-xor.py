class Solution:
    def _findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 1:
            return pref
        
        prev = pref[0]
        output = [pref[0]]
        for p in pref[1:]:
            binRepPrev = bin(prev)[2:].zfill(32)
            binRepCur = bin(p)[2:].zfill(32)
            temp = ""
            for _p, _c in zip(binRepPrev, binRepCur):
                if _c == "0":
                    temp += _p
                else:
                    if _p == "1":
                        temp += "0"
                    else:
                        temp += "1"
            output.append(int(temp, 2))
            prev ^= output[-1]
        return output
    
    def findArray(self, pref):
        if len(pref) == 1:
            return pref
        output = [pref[0]]
        prev = pref[0]
        for i in range(1, len(pref)):
            output.append(pref[i] ^ pref[i-1])
        return output
                
        
        