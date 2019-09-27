# Udemy backjack program
# incorporate: 
#	1. Regular gameplay
#	2. Error handling
#	3. Classes
#	4. Make program a package
#	5. Use pylint to check formating and rate code
#	6. Use Unit Test to check functions

import random
from os import system
import BlackJack.blackjack as bj

# Declare Global variables 

continue_playing = True				# Set flag to enter tournament loop

# ----------------------------------------------------------------------------
# Function declarations
# ----------------------------------------------------------------------------

# Clear screen
def clear_screen():
	_ = system("clear")

# Welcome Message
def welcome_message():
	print("Welcome to BlackJack!\n")

# Check to see if a player is out of funds.  
def lose_check(player1,player2):
	return (player1.chips == 0) or (player2.chips == 0)

# Input the user and error check
def input_player():
	return input("What is your name? ")

# Print the current chip position and cards for each player
def display_board(player1,player2):
	clear_screen()
	print("Player {}".format(player1.player_name))
	print("Chips: {}".format(player1.chips))
	print("Total ({}) Cards: {}".format(player1.card_count(),player1.cards))
	print("Bet: {}".format(player1.bet))
	print("------")
	print("Player {}".format(player2.player_name))
	print("Chips: {}".format(player2.chips))
	print("Total ({}) Cards: {}\n".format(player2.card_count(),player2.cards))

# ----------------------------------------------------------------------------
# Main Program
# ----------------------------------------------------------------------------

# Welcome Message
welcome_message()

# call input user function
player_name = input_player()

# Create / Initialize Users
dealer = bj.bj_player(player_name="Computer",is_computer=True,chips=0)
player1 = bj.bj_player(player_name,is_computer=False,chips=0)

deck = bj.bj_deck()

# Testing - Start with 100 chips for testing
dealer.add_chips(100)
player1.add_chips(100)
# print(player1.cards)

# Enter in BlackJack Game
while continue_playing:

	# Testing - print balances
#	dealer.print_chips()
#	player1.print_chips()

	display_board(player1,dealer)

	player1.place_bet()					# Place player 1 bet
	player1.add_chips(-player1.bet)		# Remove bet from chips

	player1.add_cards(deck.draw_card())	# First round Cards
	dealer.add_cards(deck.draw_card())	# First round cards	
	player1.add_cards(deck.draw_card())	# Second round cards
	
	player1_turn = True					# Set turn flags
	dealer_turn = True					# set turn flags
	bust_flag = False					# Set Bust flag

	# Player1 Turn
	while player1_turn:

		display_board(player1,dealer)

		# Blackjack Check
		if (player1.card_count() == 21) and (len(player1.cards) == 2):
			Print("BLACKJACK!")
			player1.add_chips(player1.bet*1.5)
			player1_turn = False
			dealer_turn = False
			break						# Break out of loop

		# Hit / Hold
		hit_hold = input("Would you like Hit/Hold: ").upper()
		if hit_hold == "HIT":
			player1.add_cards(deck.draw_card())
			
			# Check if Bust
			if player1.card_count() > 21:		# Complete
				display_board(player1,dealer)
				print("\n{} has gone BUST!".format(player1.player_name))
				dealer.add_chips(player1.bet)
				player1_turn = False
				dealer_turn = False
				bust_flag = True
			else:
				player1_turn = True
		elif hit_hold == "HOLD":
			player1_turn = False

	# Dealer Turn
	while dealer_turn and (bust_flag == False):

		display_board(player1,dealer)

		# Blackjack Check
		if (dealer.card_count() == 21) and (len(dealer.cards) == 2):
			print("BLACKJACK!")
			dealer.add_chips(player1.bet)
			dealer_turn = False
			break						# Break out of loop

		# Hit / Hold
		if dealer.card_count() < 16:
			hit_hold = "HIT"
		else:
			hit_hold = "HOLD"
		if hit_hold == "HIT":
			dealer.add_cards(deck.draw_card())
			
			# Check if Bust
			if dealer.card_count() > 21:		# Complete
				display_board(player1,dealer)
				print("\n{} has gone BUST!".format(dealer.player_name))
				player1.add_chips(player1.bet*2)
				dealer.add_chips(-player1.bet)
				dealer_turn = False
				bust_flag = True
			else:
				dealer_turn = True
		elif hit_hold == "HOLD":
			dealer_turn = False

	# Tally the round
	if (player1.card_count() > dealer.card_count()) and (bust_flag == False):
		print("{} has won the round".format(player1.player_name))
		player1.add_chips(player1.bet*2)
		dealer.add_chips(-player1.bet)
	elif (dealer.card_count() > player1.card_count()) and (bust_flag == False):
		print("{} has won the round".format(dealer.player_name))
		dealer.add_chips(player1.bet)
	elif (dealer.card_count() == player1.card_count()) and (bust_flag == False):
		print("It's a TIE!")
		player1.add_chips(player1.bet)

	# Reset Round
	player1.bet = 0
	player1.cards = []
	dealer.cards = []
	deck.deck_shuffle()

	# check to see if player is out of funds.   
	# !! note: consider consolidating into lose_check() function.
	if lose_check(player1,dealer):
		continue_playing = False
		if player1.chips <= 0:
			print("{} has gone broke!".format(player1.player_name))
		elif dealer.chips <= 0:
			print("{} has gone broke!".format(dealer.player_name))
	else:
		continue_playing = True

	# Testing pause and hit enter between rounds
	_ = input("")
