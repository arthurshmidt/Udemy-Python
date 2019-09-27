# Challange HW assigned for Object Oriented Programming

# Problem: Bank account problem: Create a bank account class
# that has two attributes:
# 	*Owner
#	*balance
# and two methods:
#	*deposit
#	*withdraw
#
# as an added requirement, withdrawals may not exceed the availble
# balance.
class Account:
	
	def __init__(self,owner,balance=0):
		self.owner = owner
		self.balance = balance

	def deposit(self,desposit_amt):
		self.balance = self.balance + desposit_amt
		print("Deposit Accepted")

	def withdraw(self,withdraw_amt):
		if withdraw_amt <= self.balance:
			self.balance = self.balance - withdraw_amt
			print("Funds Accepted")
		else:
			print("Funds Unavailable!")

	def __str__(self):
		return "Account owner: {}\nAccount balance: {}".format(self.owner,self.balance)

# Testing Account Class
acct1 = Account("Jose",100)
print(acct1) # str representation
acct1.owner
acct1.balance
acct1.deposit(50) # print "Deposit Accepted"
acct1.withdraw(75) # print "Withdrawal Accepted"
acct1.withdraw(500) # print "Funds Unavailable!"