def intToRoman(num):
        data = {
                0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",9:"IX",10:"X",40:"XL",
                50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"
               }
        if num in data.keys():
            return data[num]
        n = num
        result = ""
        while num > 0:
            for keys in sorted(data.keys(),reverse=True):
                if num > keys:
                    div, num = divmod(num, keys)
                    result += data[keys] * div
                elif num == keys:
                    result += data[keys]
                    num -= keys
        return result

print(intToRoman(3))
print(intToRoman(4))
print(intToRoman(9))
print(intToRoman(58))
print(intToRoman(1994))