from IPython.display import clear_output
from os import system
import random

# Global Initializaions
board = ["1","2","3","4","5","6","7","8","9"]
test_board = [" ","X","O","X","O","X","O","X","O","X"]

# player 0 - no player selected
# player 1 - 'X'
# player 2 - 'O'
player_flag = True
player1 = ""
player2 = ""
game_on = True

def clear():
	_ = system("clear")

# Write a function that can print out a board.  Setup your board as a
# list, where each index 1-9 correspondes with a number on a number pad, 
# so you get a 3 x 3 board representation.
def display_board(board):
	# print top
	print("   |   |   ")
	print(" {} | {} | {} ".format(board[0],board[1],board[2]))
	print("   |   |   ")
	print("-----------")

	# print middle
	print("   |   |   ")
	print(" {} | {} | {} ".format(board[3],board[4],board[5]))
	print("   |   |   ")
	print("-----------")

	#print bottom
	print("   |   |   ")
	print(" {} | {} | {} ".format(board[6],board[7],board[8]))
	print("   |   |   \n")

# Write a function that can take a player input and assign their mark
# "x" or "O".  Think about using while loops to continually ask until 
# you get a correct answer.
# Output: string for player1 player2 of either X or O
def player_input():
	player1 = ""
	player2 = ""
	while player1 not in ["X","O"]:
		player1 = input("Player 1, please pick a marker 'X' or 'O': ").upper()
	if player1 == "X":
		player2 = "O"
	else:
		player2 = "X"
	
	return player1,player2

# Testing
# player1,player2 = player_input()
# print(player1)
# print(player2)
# _ = input()

# Write a function that takes the board list object, a marker ("X" and 
# "O"), and a desired positions (number 1-9) and assigns it to the board
# output: board [list]
def place_marker(board, marker, position):
	board[position-1] = marker
	return board

# testing
# board = place_marker(test_board,"$",8)
# display_board(board)

# Write a function that takes in a board and mark(X or O) and the checks
# to see if that mark has won.
def win_check(board,mark):
	#Check Rows
	if (board[0] == mark) and (board[1] == mark) and (board[2] == mark):
		return True
	if (board[3] == mark) and (board[4] == mark) and (board[5] == mark):
		return True	
	if (board[6] == mark) and (board[7] == mark) and (board[8] == mark):
		return True

	#Check Columns	
	if (board[0] == mark) and (board[3] == mark) and (board[6] == mark):
		return True
	if (board[1] == mark) and (board[4] == mark) and (board[7] == mark):
		return True	
	if (board[2] == mark) and (board[5] == mark) and (board[8] == mark):
		return True

	#Check Diaginals	
	if (board[0] == mark) and (board[4] == mark) and (board[8] == mark):
		return True	
	if (board[2] == mark) and (board[4] == mark) and (board[6] == mark):
		return True
	else:
		return False

# Testing
# print(win_check(test_board,"X"))

# Write a function that uses the random module to randomly decide which 
# player goes first.  You may want to lookup random.randint()  Return a 
# string of which player went first.  
def choose_first():
	rand_selection = random.randint(1,2)
	if rand_selection == 1:
		return "player 1"
	elif rand_selection == 2:
		return "player 2"

# testing
#print(choose_first())

# Write a function that returns a boolean indicating whether a space on
# the bard is freely available.
# Output: True if  x or O in position
def space_check(board,position):
	return (board[position] == "X") or (board[position] == "O")

# Testing
# display_board(test_board)
# print(space_check(test_board,0))

# Write a function that checks if the board is full and returns a boolean
# value.  True if full, False otherwise.
# Output: Boolean.
def full_board_check(board):
	flag = True
	for position in board:
		if (position != "X") and (position !="O"):
			flag = False
			return flag
	if flag == True:
		print("\nSTALEMATE!!")
	return flag

# Testing
# display_board(test_board)
# print(full_board_check(test_board))

# Write a function that asks for a player's next position (as a number
# 1-9) and then uses the function from step 6 to check if it's a free
# position.  If it is, then return the position for later use.
def player_choice(board,player_str):
	input_number = 0
	while (input_number not in [1,2,3,4,5,6,7,8,9]) or space_check(board,input_number-1):
		input_number = int(input("{} Input board position 1-9: ".format(player_str)))
	return input_number

# Testing
# display_board(test_board)
# print(player_choice(test_board))

# Write a function that asks the player if they want to play again and
# returns a boolean True if they do want to play again.
# Output: Boolean true if yes.
def replay():
	input_replay = ""
	while ((input_replay != "N") or (input_replay != "Y")):
		input_replay = input("Would you like to play again? (Y or N): ").upper()
		if input_replay == "Y":
			return True
		elif input_replay == "N":
			return False

# Testing
# print(replay())

# A.S. Write a function that clears the board
# Output: return (list) filled " " items.
def clear_board(board):
	temp_board = board
	for x in range(0,9):
		temp_board[x] = " "
	return temp_board

# Testing
# print(board)
# print(clear_board(board))

# A.S. Wite a function to display instructions
# Output: printed instructions
def display_instructions():
	print("\nInstructions\n")
	print("1. First player selects what they want to be 'X' or 'O'.")
	print("2. The first player selects which position they want (1-9)")
	print("   See the board above for layout.")
	print("3. The next player selects which position they want.  This")
	print("   continues until a player has won, or the board is filled.")
	print("4. Press Ctrl-c to quick the game mid-game.")
	print("5. Party like its 1999.\n\n")
	print("Are you ready to play!?\n")


# **************************************************************** #

#																   #
# 							Main Program						   #
# 																   #

# **************************************************************** #

clear()

# Welcome Message 

print("Welcome to Tick Tac Toe!\n")
display_board(board)
print("\nLets Select which player will go first!. Woo hoo!\n")
_ = input()

# Instructions

clear()
display_board(board)
display_instructions()
_  = input()

# Begin gameplay 

clear()
display_board(board)
player1,player2 = player_input()
board = clear_board(board)
display_board(board)
while(game_on):
	# Clear and redisplay board
	clear()
	display_board(board)

	if player_flag == True:

		# Player 1 Turn
		if player1 == "X":
			input_number = player_choice(board,player1)
			place_marker(board,"X",input_number)
		elif player1 =="O":
			input_number = player_choice(board,player1)
			place_marker(board,"O",input_number)
		clear()
		display_board(board)

	elif player_flag == False:

		# Player 2 Turn
		if player2 == "X":
			input_number = player_choice(board,player2)
			place_marker(board,"X",input_number)
		elif player2 =="O":
			input_number = player_choice(board,player2)
			place_marker(board,"O",input_number)
		clear()
		display_board(board)

	# Game continuations
	if (full_board_check(board) or win_check(board,"X") or win_check(board,"O")):
		game_on = False
		if win_check(board,"X"):
			print("\nX WINS!!!!")
		elif win_check(board,"O"):
			print("\nO WINS!!!!")

	# Switch player flag
	if player_flag == True:
		player_flag = False
	else:
		player_flag = True

# clear()