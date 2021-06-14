class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # A method to validate subSequence
        # use binary search to find the optimal k in removable
        l, r = 0, len(removable) - 1
        result = 0
        # binary search
        while l <= r:
            # middle value
            m = l + ((r-l) // 2)
            # creating a set of removable characters
            removed = set(removable[:m+1])
            if self.isSubSq(s, p, removed):
                result = max(result, m + 1)
                # if subsq there could be more removable chars
                l = m + 1
            else:
                # if not subsq check in the left portion of m
                r = m - 1
        return result
        
        
    def isSubSq(self, s, p, removed):
        # intialize pointers to 0
        i,j = 0,0
        # check while end of string is reached
        while i < len(s) and j < len(p):
            # if skipple char or non match
            # increment i
            if i in removed or s[i] != p[j]:
                i += 1
                continue
            # if match increment both i and j
            i += 1
            j += 1
        # return True if j reaches end of p indicating
        # subsequnce presence
        return j == len(p)