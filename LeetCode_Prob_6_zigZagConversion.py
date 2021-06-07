def convert(s, numRows):
        if numRows == 1:
            return s
        data = []
        flag = False
        n = 0
        while n < len(s):
            # extracing full text
            if not flag:
                extraction = s[n:n+numRows]
                n += numRows
                data.append(list(extraction))
                # alternate flag value
                flag = True 
            # extracing zigzag text
            else:
                # -2 here is for subtracting top and bottom row
                extraction = s[n:(n+numRows-2)]
                n += (numRows - 2)
                # next set
                next_set = [0] + list(extraction) + [0]
                # print(next_set)
                # zeros here are for padding top and bottom row
                for j in range(1,len(next_set)-1):
                    append_value = [0]*numRows
                    append_value[j] = next_set[j]
                    # print("append_value", append_value)
                    # reverse the appending value
                    data.append(append_value[::-1])
                # alternate flag value
                flag = False
        result = ""
        for i in range(numRows):
            for eachRow in data:
                if len(eachRow) > 0:
                    value = eachRow.pop(0)
                else:
                    value = ""
                result +=  value if value != 0 else ""
        return result

s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))
numRows = 4
print(convert(s, numRows))
s = "A"
numRows = 1
print(convert(s, numRows))
s = "AB"
numRows = 1
print(convert(s, numRows))