class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # referrred online youtube
        all_indexes = defaultdict(list)
        
        for i in range(len(s)):
            all_indexes[s[i]].append(i)
            
        # print(all_indexes)
        summ = 0
        
        for charList in all_indexes.values():
            print(charList)
            for i in range(len(charList)):
                left  = charList[i] + 1 if i == 0 else charList[i] - charList[i-1]
                right = len(s) - charList[i] if i == len(charList)-1 else charList[i+1] - charList[i]
                # print(left, right, i)
                summ += left * right
                
        return summ