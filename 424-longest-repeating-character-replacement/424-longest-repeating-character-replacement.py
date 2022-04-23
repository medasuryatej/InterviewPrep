class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # a means to store the freq of every element
        hashMap = defaultdict(int)
        # left pointer
        left = 0
        # output storage
        output = 0
        # storing maxfreq of an element
        maxFreq = 0
        # iterating over every character
        for right in range(len(s)):
            # increase the freq of a character
            hashMap[s[right]] += 1
            # update the maxFreq element
            maxFreq = max(maxFreq, hashMap[s[right]])
            # window length = (right - left + 1)
            # if the window_length - maxFreq == 0 (window contains only one elment)
            # else: there are other characters
            #   if the other char count > allowable replacements then reduce the window size
            while (right - left + 1 - maxFreq > k):
                hashMap[s[left]] -= 1
                left += 1
            # update the current longest string
            output = max(output, right - left + 1)
        return output