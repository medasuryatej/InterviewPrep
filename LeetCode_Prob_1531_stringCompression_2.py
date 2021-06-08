def runLengthEncode(string):
	result = ""
	prev = ""
	counter = 0
	string += " "
	for eachchar in string:
		if eachchar == prev:
			counter += 1
		else:
			result += prev
			result += str(counter)
			counter = 1
			prev = eachchar
	return result[1:]

string = "aaabcccd"
print(string)
print(runLengthEncode(string))

string = "http://gooooooooooooooooooooooooooooooooooooooooooooooooooooooooooogle.com/"
print(string)
print(runLengthEncode(string))