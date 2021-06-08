def compress(chars):
        # a variable to track previous character
        # you need a counter to keep track of current group legth
        if not chars:
            return 0
        mychar = chars[0]
        count = 0
        length = len(chars)
        chars.append(" ") # Append a space so last char group is not left out in loop
        for i in range(length+1): #+1 for extra space char we added
            char = chars.pop(0)
            if char == mychar: #if same character then just increase the count
                count += 1
            else:
                if count == 1: #if not same then append the char to chars
                    chars.append(mychar) #if count is 1 don't append count
                elif count > 1:
                    chars.append(mychar)
                    chars += (list(str(count))) #if count > 1 append count as a string
                mychar = char #update mychar as the new different char in chars
                count = 1 #reset count to 1 as we have already read the new char
        print(chars)
        return len(chars)

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars))