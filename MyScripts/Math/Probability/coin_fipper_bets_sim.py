# Modules
# random is used to flip the imaginary coin.
import random

# Settings
# This changes how much money is bet each time. Note that if not enough money is owned to bet this amount, all current money will be bet.
MONEY_BET = 1
# This changes how much money is started with.
START_MONEY = 10

# Variables
# This stores how much money is currently owned.
current_money = START_MONEY
# This stores how much money is bet for the current iteration.
current_bet_money = MONEY_BET
# This stores how many iterations have passed so far.
iterations = 0

# Helper functions
# This is a function to flip a coin and return the result. This is mostly for readability.
def flip_coin():
	"""Flips a coin."""
	
	# Gets a single random bit (same as getting random boolean).
	return random.getrandbits(1)


# Main (runs when not imported as a module)
if __name__ == "__main__":
	# Looping until no money is left.
	while current_money != 0:
		# Checking if enough money is owned to bet amount.
		if current_money > MONEY_BET:
			# Betting the amount put into the settings.
			current_bet_money = MONEY_BET
		else:
			# Betting all the money.
			current_bet_money = current_money
		
		# Flipping a coin and seeing if the bet was successful.
		if flip_coin():
			# Increasing money.
			current_money += current_bet_money
		else:
			# Decreasing money.
			current_money -= current_bet_money
		
		# Incrementing the iterations counter.
		iterations += 1
	
	# Printing the number of iterations.
	print(iterations)
