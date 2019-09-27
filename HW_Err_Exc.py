# Error handling HW.  

# Problem 1: Handle the exception trhown by the code below
# by using try and except blocks.

try:
	for i in ['a','b','c']:
		print(i**2)
except:
	print("An error occurred with the for loop!\n")

# Problem 2: Handle the exception thrown by the code below
# by using try and except blocks.  Then use a finally block
# to print "All Done"
x = 5
y = 0

try:
	z = x/y
except:
	print("Division error!")
finally:
	print("All Done\n")

# Problem 3: Write a function that asks for an integer and 
# prints the square of it.  Use a while loop with a try,
# except, else block to account for incorrect inputs.
def ask():
	number = 0
	while True:
		try:
			number = int(input("Input an integer: "))
		except:
			print("An error occurred! Please try again!")
		else:
			print("Thank you, your number squared is: {}".format(number**2))
			break

# Testing ask() Function
ask()