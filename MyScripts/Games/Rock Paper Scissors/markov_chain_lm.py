# NOTE: doesn't work (yet)

import itertools
import random

# Settings
# This changes how many moves are stored in the move counts.
MOVE_DEPTH = 2
# This changes how long a move is remembered.
MEMORY_LENGTH = 10

# Constants
# This is a list of valid moves.
MOVES = ["R", "P", "S"]
# This is a dictionary for the move that beats a specific move.
WINNING_MOVE = {"R": "P", "P": "S", "S": "R"}

# Variables
# This stores the move counts for each combination of moves by the opponent and self.
move_counts = {"".join(combo): {"R": 0, "P": 0, "S": 0} for combo in itertools.product("RPS", repeat=MOVE_DEPTH * 2)}
# This is the list of moves that the computer "remembers".
move_history = ""
# These three variables store the wins, losses, and ties of the game.
computer_wins = 0
ties = 0
user_wins = 0

# Helper functions
# This function gets the user move, checks who won, and returns the input.
def play_move(computer_move):
	# Making sure the global variables aren't confused for local variables.
	global computer_wins, ties, user_wins
	
	# Input loop (to insure valid input)
	while True:
		# Getting input and changing to uppercase.
		user_move = input("Choose a move (R, P, or S): ").upper()
		# Checking if input is R, P, or S.
		if user_move in MOVES:
			# Adding a line break for readability.
			print()
			# Breaking from the input loop.
			break
		# Telling the user that their input is invalid.
		print("That isn't R, P, or S!")
	
	# Telling the user what the computer played, along with an extra line break.
	print("I played " + computer_move + "!\n")
	# Checking who won (or if it's a tie).
	if WINNING_MOVE[user_move] == computer_move:
		# Telling the user that the computer wins.
		print("I win!")
		# Incrementing the computer wins counter.
		computer_wins += 1
	elif WINNING_MOVE[computer_move] == user_move:
		# Telling the user that they won.
		print("You win.")
		# Incrementing the user wins counter.
		user_wins += 1
	else:
		# Telling the user that it was a tie.
		print("Tie!")
		# Incrementing the ties counter.
		ties += 1
	
	# Printing the number of wins, ties, and losses.
	print("I won:", computer_wins)
	print("Ties:", ties)
	print("You won:", user_wins)
	# Adding two line breaks for readability.
	print("\n")
	
	# Returning the user's move.
	return user_move

# Main (runs when not imported as module)	
if __name__ == "__main__":
	# Looping through moves to fill up history + enough history before to fully utilize memory.
	for move in range(MOVE_DEPTH * 2):
		# Choosing a random move.
		computer_move = random.choice(MOVES)
		# Getting the user's move.
		user_move = play_move(computer_move)
		# Storing in the move history.
		move_history += computer_move + user_move
		
	# Main game loop
	while True:
		# Getting the last few moves and finding the user's tendencies. These will be the numerators in the probability fractions.
		numerators = move_counts[move_history[-(MOVE_DEPTH*2):]]
		# Getting the sum of the move counts. This will be the denominator in the probability fractions.
		denominator = sum(numerators.values())
		
		# Making sure that the denominator is at least 1 (to avoid division by zero).
		if denominator > 0:
			# Getting a random decimal between 0 and 1. This will be what chooses the move, along with the move counts.
			random_decimal = random.random()
			# Array to store the decimal values.
			decimals = []
			# Variable to store the sum that's used to make the decimals increase.
			decimal_sum = 0
			# Looping through numerator keys.
			for key in numerators:
				# Getting the probability decimal value.
				probability_decimal = numerators[key] / denominator
				# Adding the probability decimal to the sum.
				decimal_sum += probability_decimal
				# Checking if the sum is greater than the random decimal.
				if decimal_sum > random_decimal:
					# Using the current key as the predicted user move.
					predicted_user_move = key
					# Breaking out of the loop.
					break
			
			# Choosing the move that beats the user's predicted move.
			computer_move = WINNING_MOVE[predicted_user_move]
		else:
			# Choosing a random move.
			computer_move = random.choice(MOVES)
		
		# Getting the user's move.
		user_move = play_move(computer_move)
		
		# Updating the move history.
		move_history = move_history[-((MEMORY_LENGTH + MOVE_DEPTH) * 2 - 2):] + computer_move + user_move
		# Resetting the move counts.
		move_counts = {"".join(combo): {"R": 0, "P": 0, "S": 0} for combo in itertools.product("RPS", repeat=MOVE_DEPTH * 2)}
		# Looping through the move history.
		for move in range((MEMORY_LENGTH - MOVE_DEPTH) * 2 - 2):
			# Storing the set of moves in the move counts.
			print(move, move_history, move_counts)
			move_counts[move_history[move:move+(MOVE_DEPTH*2)]][move_history[move + (MOVE_DEPTH * 2) + 1]] += 1
