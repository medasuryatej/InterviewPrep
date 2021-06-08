def lengthOfLongestSubstring(s):
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        
        max_length = 0
        data_dict = {}
        start = 0
        
        for index, character in enumerate(s):
            if character in data_dict:
                # if a duplicate character is encountered
                # update the max length
                max_length = max(max_length, index-start)
                # start position would be max(prevoccurence, curroccurance)
                start = max(start, data_dict[character]+1)
            data_dict[character] = index
            print(index, start)
        return max(max_length, len(s)-start)

print("#\n", lengthOfLongestSubstring("abcabcbb"))
print("#\n", lengthOfLongestSubstring("dvdf"))