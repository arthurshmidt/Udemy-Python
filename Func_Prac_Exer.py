# ********************************************************************* #

#
# 				LEVEL WARMUP PROBLEMS
#

# ********************************************************************* #

# Write a function that returns the lessor of two given numbers if
# both numbers are even, but returne the greate if one or both are
# odd.
# Hint: use the min() function
def lessor_of_two_evens(a,b):
	# if even
	if (a % 2 == 0) and (b % 2 == 0):
		if a < b:
			return a
		else: 
			return b
	elif a > b:
		return a
	else:
		return b

# Testing lessor_of_two_evens() function
print("*Testing Warmup lessor_of_two_evens()*")
print("lessor of 2,4: {}".format(lessor_of_two_evens(2,4)))
print("lessor of 2,5: {}\n".format(lessor_of_two_evens(2,5)))

# ******************************************************************** # 

# Write a function that takes a two-word string and returns True if
# both words begin with the same letter
def animal_crackers(text):
	split_words = text.lower().split()
	return split_words[0][0] == split_words[1][0]

# Testing animal_crackers() function
print("*Testing Warmup animal_crackers()*")
print("Levelheaded Llama: {}".format(animal_crackers("Levelheaded Llama")))
print("Crazy Kangarro: {}\n".format(animal_crackers("Crazy Kangarro")))

# ********************************************************************* #

# Write a function given two integers, return True if the sum of the 
# of the integers is 20 or if one of the integers is 20.  If not, 
# return False
def makes_twenty(n1,n2):
	if n1 == 20 or n2 == 20:
		return True
	elif n1 + n2 ==20:
		return True
	else:
		return False

# Testing makes_twenty() function
print("*Testing Warmup makes_twenty()*")
print("Makes twenty for 20,10: {}".format(makes_twenty(20,10)))
print("Makes twenty for 12,8: {}".format(makes_twenty(12,8)))
print("Makes twenty for 2,3: {}\n".format(makes_twenty(2,3)))

# ********************************************************************* #

#
# 				LEVEL 1 PROBLEMS
#

# ********************************************************************* #

# Write a function that capitalizes the first and fourth letter of a name
# Hint: you can use .capitalize()
def old_macdonald(name):
	temp_string = ""
	for index,letter in enumerate(name):
		if index == 0 or index == 3:
			letter = letter.upper()
		temp_string = temp_string + letter
	return temp_string

# Testing old_macdonld() function
print("*Testing Level 1 old_macdonald()*")
print("Input of macdonald: {}\n".format(old_macdonald("macdonld")))

# ********************************************************************* #

# Given a sentence, return a sentence with the words reversed
# Hint: use .join() ex. "==".join(["a","b","c"])  -> a--b--c
def master_yoda(text):
	split_string = text.split()
	return " ".join(list(split_string[::-1]))

# Testing master_yoda() function
print("*Testing Level 1 master_yoda()*")
print("Input of 'I am home': {}".format(master_yoda("I am home")))
print("Input of 'we are ready': {}\n".format(master_yoda("we are ready")))

# ********************************************************************* #

# Given and integer n, return True if n is within 10 of either 100 or 200
# Hint: the abs() function can be used.  ex. (abs(100-n) <= 10)
def almost_there(n):
	return ((n >= 90) and (n <= 110)) or ((n >= 190) and (n <= 210))

# Testing almost_there() function
print("*Testing Level 1 almost_there()*")
print("Almost There 90: {}".format(almost_there(90)))
print("Almost There 104: {}".format(almost_there(104)))
print("Almost There 150: {}".format(almost_there(150)))
print("Almost There 209: {}\n".format(almost_there(209)))

# ********************************************************************* #

#
# 				LEVEL 2 PROBLEMS
#

# ********************************************************************* #

# Given a list of ints, return True if the array contains a 3 next to a 3
# somewhere
def has_33(nums):
	last_number = 0
	for index,number in enumerate(nums):
		if (number == 3) and (last_number == 3):
			return True
		last_number = number
	return False

# Testing has_33() function
print("*Testing Level 2 has_33()*")
print("Has 33 ([1,3,3]): {}".format(has_33([1,3,3])))
print("Has 33 ([1,3,1,3]): {}".format(has_33([1,3,1,3])))
print("Has 33 ([3,1,3]): {}\n".format(has_33([3,1,3])))

# ********************************************************************* #

# Givin a string, return a string where for every character in the
# original there are three characters
def paper_doll(text):
	temp_string = ""
	for x in text:
		temp_string = temp_string + x*3
	return temp_string

# Testing paper_doll() function
print("*Testing Level 2 paper_doll*")
print("Input Hello: {}".format(paper_doll("Hello")))
print("Input Mississippi: {}\n".format(paper_doll("Mississippi")))

# ********************************************************************* #

# Given three integers between 1 and 11, if their sum is less than or 
# equal to 21, return their sum.  If their sum exceeds 21 and there's
# an eleven, reduce the total sum by 10.  finally, if the sum (even after 
# adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
	if sum([a,b,c]) <= 21:
		return sum([a,b,c])
	# elif 11 in [a,b,c] and sum([a,b,c]) <= 31	
	elif (a == 11) or (b == 11) or (c == 11):
		if sum([a,b,c]) - 10 <= 21:
			return sum([a,b,c]) - 10
		else:
			return "Bust"
	return "Bust"


# Testing blackjack() function
print("*Testing Level 2 blackjack()*")
print("Blackjack 5,6,7: {}".format(blackjack(5,6,7)))
print("Blackjack 9,9,9: {}".format(blackjack(9,9,9)))
print("Blackjack 9,9,11: {}\n".format(blackjack(9,9,11)))

# ********************************************************************* #

# Return the sum of the numbers in the array, except ignore sections of 
# numbers starting with a 6 and extending to the next 9 (every 6 will be
# followed by a least one 9).  return 0 for no numbers.
def summer_69(arr):
	last_number = 0
	flag = False

	for x in arr:
		if x == 9:
			flag = False
		elif (flag == True) or (x == 6):
			flag = True
		else:
			last_number = last_number + x
	return last_number

# Testing summer_69() function
print("*Testing Level 2 summer_69()*")
print("Input [1,3,5]: {}".format(summer_69([1,3,5])))
print("Input [4,5,6,7,8,9]: {}".format(summer_69([4,5,6,7,8,9])))
print("Input [2,1,6,9,11]: {}".format(summer_69([2,1,6,9,11])))