import string

# *********************************************************************** #

#
# Home Work
#

# *********************************************************************** #

# Write a function that computes the volume of a sphere given its radius
def vol(rad):
	pi = 3.14
	return (4/3) * pi * rad ** 3

print("Testing vol() function")
print("Input 2: {}\n".format(vol(2)))

# *********************************************************************** #

# Wrtie a function that checks whether a number is in a given range
# (inclusive of high and low)
# output: "5 is in the range between 2 and 7"
def ran_check(num, low, high):
	if (num > low) and (num < high):
		print("{} is in the range between {} and {}".format(num, low, high))
	else:
		print("{} is NOT in the range between {} and {}".format(num, low, high))

print("Testing ran_check() function")
ran_check(5,2,7)
print("\n")

# *********************************************************************** #

# Same as above but a boolean output:
def ran_bool(num, low, high):
	return (num > low) and (num < high)

print("Testing ran_check() function (boolean output)")
print("Input 3,1,10: {}\n".format(ran_bool(3,1,10)))

# *********************************************************************** #

# Write a Python function that accepts a string and calculates the number
# of upper case letters and lower case letters.
# Sample String: 'Hellow Mr. Rogers, how are you this fine Tuesday?'
#				 'Expected output: '
#				 'No. of Upper case characters: 4'
#				 'No. of lower case characters: 33'
#Hint: use .isupper() .islower
def up_low(s):
	upper_letter = 0
	lower_letter = 0
	alpha = string.ascii_lowercase
	for letter in s:
		if letter.isupper():
			upper_letter += 1
		elif letter in alpha:
			lower_letter += 1
	print("No. of Upper case characters: {}".format(upper_letter))
	print("No. of Lower case characters: {}\n".format(lower_letter))

print("Testing up_low() function")
s = "Hello Mr. Rogers, how are you this fine Tuesday?"
up_low(s)

# *********************************************************************** #

# Write a Python function that takes a list and returns a new list with
# unique elements of the first list.
# Sample list: [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List: [1,2,3,4,5]

def unique_list(lst):
	return list(set(lst))

lst = [1,1,1,1,2,2,3,3,3,3,4,5]
print("Testing unique_list() function")
print("Input [1,1,1,1,2,2,3,3,3,3,4,5]: {}\n".format(unique_list(lst)))

# *********************************************************************** #

# Write a Python function to multiply all the nubmer in a list.
# Sample list: [1,2,3,-4]
# Expected output: -24
def multiply(numbers):
	num = 1
	for x in numbers:
		num = num * x
	return num   

print("Testing multiply() function")
print("Input [1,2,3,-4]: {}\n".format(multiply([1,2,3,-4])))

# *********************************************************************** #

#
# Home Work - Hard
#

# *********************************************************************** #

# write a Python function to chekc whether a string is panagram or not.
# Note: Panagrams are words or sentences containing every letter of the 
# alphabet at least onece.  
# Example: "The quick brown fox jumps over the lazy dog"
# Hint: Look at the string module
#	string.ascii_lowercase = 'abcdefghijklmnopqrstuvwzy'
import string
input_string = "The quick brown fox jumps over the lazy dog"
def ispangram(str1,alphabet=string.ascii_lowercase):
	flag = False
	for alpha_letter in alphabet:
		for string_letter in str1:
			if string_letter  == alpha_letter:
				flag = True
				continue
		if flag == False:
			return flag
		flag = False
	return True

print("Testing ispangram() function")
print("Input '{}': {}".format(input_string,ispangram(input_string)))