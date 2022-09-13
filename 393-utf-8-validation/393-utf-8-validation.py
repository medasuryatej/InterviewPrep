class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            skip, mask = 0, 1 << 7 # 1 << 7 = 128
            # Mask helps in identifying which bit is set
            while data[i] & mask:
                skip += 1
                mask >>= 1 # keep checking how many ones are set in the MSB position
    
            if skip == 1 or skip > 4: return False # if there is only one 1 or more than 4 then its not a valid encoding
            if any((not x & 1<<7) or x & 1<<6 for x in data[i+1:i+skip]): return False
            
            i += max(1, skip) # increment n bytes
        return i == len(data) # check if we reached end