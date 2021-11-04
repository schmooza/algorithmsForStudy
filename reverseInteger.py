# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.





def reverse_int(inputVal):
	
	makeString = str(inputVal)
	# catch the minus. make a shallow copy which removes the minus.
	# reverse the number using -1. add the minus back on. return as int.
	if makeString[0] == "-":
		return int("-" + makeString[:0:-1])
	else:
		return makeString[::-1]
	
	
print(reverse_int(-122))
print(reverse_int(122))
